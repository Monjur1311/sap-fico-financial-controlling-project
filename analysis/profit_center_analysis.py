import pandas as pd

PERIOD = "2026-01"

transactions = pd.read_csv(
    "data/transactions.csv",
    parse_dates=["posting_date"]
)

profit_centers = pd.read_csv(
    "data/profit_centers.csv"
)

allocations = pd.read_csv(
    "data/profit_center_allocations.csv"
)

# Create accounting period
transactions["period"] = (
    transactions["posting_date"]
    .dt.to_period("M")
    .astype(str)
)

period_data = transactions[
    transactions["period"] == PERIOD
].copy()

# -------------------------------------------------
# REVENUE
# -------------------------------------------------

revenue_transactions = period_data[
    (period_data["gl_account"] >= 400000)
    & (period_data["gl_account"] < 500000)
    & (period_data["profit_center"].notna())
].copy()

revenue_transactions["revenue"] = (
    revenue_transactions["credit"]
    - revenue_transactions["debit"]
)

revenue_summary = (
    revenue_transactions
    .groupby("profit_center", as_index=False)
    ["revenue"]
    .sum()
)

# -------------------------------------------------
# EXPENSES
# -------------------------------------------------

expense_transactions = period_data[
    (period_data["gl_account"] >= 500000)
    & (period_data["gl_account"] < 600000)
].copy()

expense_transactions["expense_amount"] = (
    expense_transactions["debit"]
    - expense_transactions["credit"]
)

expense_by_gl = (
    expense_transactions
    .groupby(
        ["gl_account", "account_name"],
        as_index=False
    )["expense_amount"]
    .sum()
)

# Merge expenses with allocation rules
allocated_costs = expense_by_gl.merge(
    allocations,
    on=["gl_account", "account_name"],
    how="left"
)

# Validate that every expense has an allocation
missing_allocations = allocated_costs[
    allocated_costs["profit_center"].isna()
]

if not missing_allocations.empty:
    print("WARNING: Some expenses have no profit-center allocation:")
    print(missing_allocations)

allocated_costs["allocated_cost"] = (
    allocated_costs["expense_amount"]
    * allocated_costs["allocation_pct"]
    / 100
)

cost_summary = (
    allocated_costs
    .groupby("profit_center", as_index=False)
    ["allocated_cost"]
    .sum()
)

# -------------------------------------------------
# PROFIT CENTER REPORT
# -------------------------------------------------

report = (
    profit_centers
    .merge(
        revenue_summary,
        on="profit_center",
        how="left"
    )
    .merge(
        cost_summary,
        on="profit_center",
        how="left"
    )
)

report["revenue"] = report["revenue"].fillna(0)

report["allocated_cost"] = (
    report["allocated_cost"].fillna(0)
)

report["operating_profit"] = (
    report["revenue"]
    - report["allocated_cost"]
)

report["operating_margin_pct"] = report.apply(
    lambda row:
    (
        row["operating_profit"]
        / row["revenue"]
        * 100
    )
    if row["revenue"] != 0
    else 0,
    axis=1
)

total_profit = report["operating_profit"].sum()

report["profit_contribution_pct"] = (
    report["operating_profit"]
    / total_profit
    * 100
)

report = report[
    [
        "profit_center",
        "profit_center_name",
        "revenue",
        "allocated_cost",
        "operating_profit",
        "operating_margin_pct",
        "profit_contribution_pct"
    ]
]

print("=" * 95)
print("RHINETECH GMBH - PROFIT CENTER PERFORMANCE REPORT")
print(f"Reporting Period: {PERIOD}")
print("=" * 95)

print(report.to_string(index=False))

total_revenue = report["revenue"].sum()
total_cost = report["allocated_cost"].sum()

print("\n" + "-" * 95)

print(
    f"Total Revenue: EUR "
    f"{total_revenue:,.2f}"
)

print(
    f"Total Allocated Cost: EUR "
    f"{total_cost:,.2f}"
)

print(
    f"Operating Profit: EUR "
    f"{total_profit:,.2f}"
)

company_margin = (
    total_profit / total_revenue * 100
)

print(
    f"Company Operating Margin: "
    f"{company_margin:.2f}%"
)

# -------------------------------------------------
# RECONCILIATION CONTROL
# -------------------------------------------------

fi_expense_total = (
    expense_transactions["expense_amount"].sum()
)

allocation_difference = (
    fi_expense_total - total_cost
)

print("\nPROFIT CENTER COST RECONCILIATION")
print("-" * 95)

print(
    f"FI Expense Total: EUR "
    f"{fi_expense_total:,.2f}"
)

print(
    f"Profit Center Allocated Cost: EUR "
    f"{total_cost:,.2f}"
)

print(
    f"Difference: EUR "
    f"{allocation_difference:,.2f}"
)

if abs(allocation_difference) < 0.01:
    print("PASS: Profit-center costs reconcile with FI.")
else:
    print("FAIL: Profit-center cost allocation does not reconcile.")

# Highest profit center
highest_profit = report.loc[
    report["operating_profit"].idxmax()
]

print("\nTOP PROFIT CENTER")
print("-" * 95)

print(
    f"{highest_profit['profit_center']} - "
    f"{highest_profit['profit_center_name']}"
)

print(
    f"Operating Profit: EUR "
    f"{highest_profit['operating_profit']:,.2f}"
)

print(
    f"Operating Margin: "
    f"{highest_profit['operating_margin_pct']:.2f}%"
)

# Export report
report.to_csv(
    "reports/profit_center_report.csv",
    index=False
)

allocated_costs.to_csv(
    "reports/profit_center_cost_allocations.csv",
    index=False
)

print(
    "\nReports exported to reports/"
)

print("=" * 95)