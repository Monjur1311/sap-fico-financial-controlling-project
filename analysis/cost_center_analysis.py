import pandas as pd

PERIOD = "2026-01"

# Load data
transactions = pd.read_csv(
    "data/transactions.csv",
    parse_dates=["posting_date"]
)

cost_centers = pd.read_csv(
    "data/cost_centers.csv"
)

budget = pd.read_csv(
    "data/budget.csv"
)

# Create accounting period
transactions["period"] = (
    transactions["posting_date"]
    .dt.to_period("M")
    .astype(str)
)

# Select January 2026 expense postings
expense_transactions = transactions[
    (transactions["period"] == PERIOD)
    & (transactions["gl_account"] >= 500000)
    & (transactions["gl_account"] < 600000)
    & (transactions["cost_center"].notna())
].copy()

# Calculate actual cost
expense_transactions["actual_cost"] = (
    expense_transactions["debit"]
    - expense_transactions["credit"]
)

actuals = (
    expense_transactions
    .groupby("cost_center", as_index=False)
    ["actual_cost"]
    .sum()
)

# Select budget for reporting period
period_budget = budget[
    budget["period"] == PERIOD
].copy()

# Merge cost center master, budget and actuals
report = (
    cost_centers
    .merge(
        period_budget[
            ["cost_center", "budget_amount"]
        ],
        on="cost_center",
        how="left"
    )
    .merge(
        actuals,
        on="cost_center",
        how="left"
    )
)

report["budget_amount"] = (
    report["budget_amount"].fillna(0)
)

report["actual_cost"] = (
    report["actual_cost"].fillna(0)
)

# Calculate variance
report["variance"] = (
    report["actual_cost"]
    - report["budget_amount"]
)

# Calculate variance percentage
report["variance_pct"] = report.apply(
    lambda row:
    (
        row["variance"]
        / row["budget_amount"]
        * 100
    )
    if row["budget_amount"] != 0
    else 0,
    axis=1
)

# Management status
report["status"] = report["variance"].apply(
    lambda x:
    "Unfavorable"
    if x > 0
    else "Favorable / On Budget"
)

# Share of total actual cost
total_actual = report["actual_cost"].sum()

report["share_of_total_cost_pct"] = (
    report["actual_cost"]
    / total_actual
    * 100
)

# Select reporting columns
report = report[
    [
        "cost_center",
        "cost_center_name",
        "budget_amount",
        "actual_cost",
        "variance",
        "variance_pct",
        "share_of_total_cost_pct",
        "status"
    ]
]

print("=" * 90)
print("RHINETECH GMBH - COST CENTER PERFORMANCE REPORT")
print(f"Reporting Period: {PERIOD}")
print("=" * 90)

print(report.to_string(index=False))

total_budget = report["budget_amount"].sum()
total_variance = total_actual - total_budget

print("\n" + "-" * 90)

print(
    f"Total Budget: EUR "
    f"{total_budget:,.2f}"
)

print(
    f"Total Actual Cost: EUR "
    f"{total_actual:,.2f}"
)

print(
    f"Total Variance: EUR "
    f"{total_variance:,.2f}"
)

if total_variance > 0:
    print("Overall Status: Unfavorable")
else:
    print("Overall Status: Favorable")

# Highest-cost department
highest_cost = report.loc[
    report["actual_cost"].idxmax()
]

print("\nHIGHEST COST CENTER")
print("-" * 90)

print(
    f"{highest_cost['cost_center']} - "
    f"{highest_cost['cost_center_name']}: "
    f"EUR {highest_cost['actual_cost']:,.2f}"
)

# Export report
report.to_csv(
    "reports/cost_center_report.csv",
    index=False
)

print(
    "\nReport exported to "
    "reports/cost_center_report.csv"
)

print("=" * 90)