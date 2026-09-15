import pandas as pd

REPORTING_PERIOD = "2026-01"

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

transactions = pd.read_csv(
    "data/transactions.csv",
    parse_dates=["posting_date"]
)

coa = pd.read_csv("data/chart_of_accounts.csv")

ar = pd.read_csv("data/ar_open_items.csv")
ap = pd.read_csv("data/ap_open_items.csv")
assets = pd.read_csv("data/assets.csv")

transactions["period"] = (
    transactions["posting_date"]
    .dt.to_period("M")
    .astype(str)
)

period_data = transactions[
    transactions["period"] == REPORTING_PERIOD
].copy()

# --------------------------------------------------
# TRIAL BALANCE
# --------------------------------------------------

trial_balance = (
    period_data
    .groupby(
        ["gl_account", "account_name"],
        as_index=False
    )
    .agg(
        total_debit=("debit", "sum"),
        total_credit=("credit", "sum")
    )
)

trial_balance["net_balance"] = (
    trial_balance["total_debit"]
    - trial_balance["total_credit"]
)

trial_balance["debit_balance"] = (
    trial_balance["net_balance"]
    .clip(lower=0)
)

trial_balance["credit_balance"] = (
    (-trial_balance["net_balance"])
    .clip(lower=0)
)

trial_balance.to_csv(
    "reports/trial_balance.csv",
    index=False
)

# --------------------------------------------------
# GENERAL LEDGER CONTROL
# --------------------------------------------------

total_debit = period_data["debit"].sum()
total_credit = period_data["credit"].sum()

gl_difference = total_debit - total_credit

# --------------------------------------------------
# ACCOUNT BALANCE HELPER
# --------------------------------------------------

def get_net_balance(account):
    row = trial_balance[
        trial_balance["gl_account"] == account
    ]

    if row.empty:
        return 0

    return row["net_balance"].iloc[0]


# --------------------------------------------------
# ACCOUNTS RECEIVABLE RECONCILIATION
# --------------------------------------------------

ar_gl_balance = get_net_balance(110000)

ar_open = ar[
    ar["status"] == "Open"
].copy()

ar_open["outstanding"] = (
    ar_open["invoice_amount"]
    - ar_open["paid_amount"]
)

ar_subledger = ar_open["outstanding"].sum()

ar_difference = (
    ar_gl_balance - ar_subledger
)

# --------------------------------------------------
# ACCOUNTS PAYABLE RECONCILIATION
# --------------------------------------------------

# AP has a normal credit balance, therefore reverse sign
ap_gl_balance = -get_net_balance(200000)

ap_open = ap[
    ap["status"] == "Open"
].copy()

ap_open["outstanding"] = (
    ap_open["invoice_amount"]
    - ap_open["paid_amount"]
)

ap_subledger = ap_open["outstanding"].sum()

ap_difference = (
    ap_gl_balance - ap_subledger
)

# --------------------------------------------------
# VAT
# --------------------------------------------------

input_vat = get_net_balance(120000)

output_vat = -get_net_balance(210000)

net_vat_payable = (
    output_vat - input_vat
)

# --------------------------------------------------
# ASSET ACCOUNTING
# --------------------------------------------------

asset_cost = get_net_balance(150000)

accumulated_depreciation = (
    -get_net_balance(159000)
)

asset_nbv = (
    asset_cost
    - accumulated_depreciation
)

# --------------------------------------------------
# INCOME STATEMENT
# --------------------------------------------------

coa_lookup = coa[
    [
        "gl_account",
        "account_type"
    ]
]

tb_with_type = trial_balance.merge(
    coa_lookup,
    on="gl_account",
    how="left"
)

revenue_accounts = tb_with_type[
    tb_with_type["account_type"] == "Revenue"
].copy()

expense_accounts = tb_with_type[
    tb_with_type["account_type"] == "Expense"
].copy()

revenue_accounts["amount"] = (
    revenue_accounts["total_credit"]
    - revenue_accounts["total_debit"]
)

expense_accounts["amount"] = (
    expense_accounts["total_debit"]
    - expense_accounts["total_credit"]
)

total_revenue = revenue_accounts["amount"].sum()
total_expenses = expense_accounts["amount"].sum()

net_profit = (
    total_revenue - total_expenses
)

income_statement = pd.concat(
    [
        revenue_accounts[
            ["gl_account", "account_name", "amount"]
        ],
        expense_accounts[
            ["gl_account", "account_name", "amount"]
        ]
    ]
)

income_statement.to_csv(
    "reports/income_statement.csv",
    index=False
)

# --------------------------------------------------
# BALANCE SHEET
# --------------------------------------------------

bank = get_net_balance(100000)
accounts_receivable = get_net_balance(110000)
prepaid_expenses = get_net_balance(130000)

accounts_payable = -get_net_balance(200000)
output_vat_liability = -get_net_balance(210000)
payroll_liabilities = -get_net_balance(220000)
accrued_expenses = -get_net_balance(230000)

share_capital = -get_net_balance(300000)
retained_earnings = -get_net_balance(310000)

total_assets = (
    bank
    + accounts_receivable
    + input_vat
    + prepaid_expenses
    + asset_cost
    - accumulated_depreciation
)

total_liabilities = (
    accounts_payable
    + output_vat_liability
    + payroll_liabilities
    + accrued_expenses
)

total_equity = (
    share_capital
    + retained_earnings
    + net_profit
)

balance_difference = (
    total_assets
    - total_liabilities
    - total_equity
)

balance_sheet = pd.DataFrame(
    [
        ["Asset", "Bank Account", bank],
        ["Asset", "Accounts Receivable", accounts_receivable],
        ["Asset", "Input VAT", input_vat],
        ["Asset", "Prepaid Expenses", prepaid_expenses],
        ["Asset", "Office & IT Equipment", asset_cost],
        [
            "Contra Asset",
            "Accumulated Depreciation",
            -accumulated_depreciation
        ],
        ["Liability", "Accounts Payable", accounts_payable],
        ["Liability", "Output VAT", output_vat_liability],
        ["Liability", "Payroll Liabilities", payroll_liabilities],
        ["Liability", "Accrued Expenses", accrued_expenses],
        ["Equity", "Share Capital", share_capital],
        ["Equity", "Retained Earnings", retained_earnings],
        ["Equity", "Current Period Profit", net_profit]
    ],
    columns=[
        "category",
        "account",
        "amount"
    ]
)

balance_sheet.to_csv(
    "reports/balance_sheet.csv",
    index=False
)

# --------------------------------------------------
# CLOSING CONTROL REPORT
# --------------------------------------------------

controls = pd.DataFrame(
    [
        [
            "General Ledger",
            gl_difference,
            "PASS"
            if abs(gl_difference) < 0.01
            else "FAIL"
        ],
        [
            "Accounts Receivable Reconciliation",
            ar_difference,
            "PASS"
            if abs(ar_difference) < 0.01
            else "FAIL"
        ],
        [
            "Accounts Payable Reconciliation",
            ap_difference,
            "PASS"
            if abs(ap_difference) < 0.01
            else "FAIL"
        ],
        [
            "Balance Sheet",
            balance_difference,
            "PASS"
            if abs(balance_difference) < 0.01
            else "FAIL"
        ]
    ],
    columns=[
        "control",
        "difference",
        "status"
    ]
)

controls.to_csv(
    "reports/month_end_controls.csv",
    index=False
)

# --------------------------------------------------
# OUTPUT
# --------------------------------------------------

print("=" * 80)
print("RHINETECH GMBH - MONTH-END CLOSING")
print(f"Reporting Period: {REPORTING_PERIOD}")
print("=" * 80)

print("\nGENERAL LEDGER")
print("-" * 80)

print(
    f"Total Debit : EUR {total_debit:,.2f}"
)

print(
    f"Total Credit: EUR {total_credit:,.2f}"
)

print(
    f"Difference  : EUR {gl_difference:,.2f}"
)

print("\nSUBLEDGER RECONCILIATION")
print("-" * 80)

print(
    f"AR G/L Balance: EUR {ar_gl_balance:,.2f}"
)

print(
    f"AR Open Items : EUR {ar_subledger:,.2f}"
)

print(
    f"AR Difference : EUR {ar_difference:,.2f}"
)

print()

print(
    f"AP G/L Balance: EUR {ap_gl_balance:,.2f}"
)

print(
    f"AP Open Items : EUR {ap_subledger:,.2f}"
)

print(
    f"AP Difference : EUR {ap_difference:,.2f}"
)

print("\nVAT")
print("-" * 80)

print(
    f"Input VAT      : EUR {input_vat:,.2f}"
)

print(
    f"Output VAT     : EUR {output_vat:,.2f}"
)

print(
    f"Net VAT Payable: EUR {net_vat_payable:,.2f}"
)

print("\nFIXED ASSETS")
print("-" * 80)

print(
    f"Acquisition Cost        : EUR {asset_cost:,.2f}"
)

print(
    f"Accumulated Depreciation: EUR "
    f"{accumulated_depreciation:,.2f}"
)

print(
    f"Net Book Value          : EUR {asset_nbv:,.2f}"
)

print("\nINCOME STATEMENT")
print("-" * 80)

print(
    f"Revenue : EUR {total_revenue:,.2f}"
)

print(
    f"Expenses: EUR {total_expenses:,.2f}"
)

print(
    f"Profit  : EUR {net_profit:,.2f}"
)

print("\nBALANCE SHEET")
print("-" * 80)

print(
    f"Total Assets      : EUR {total_assets:,.2f}"
)

print(
    f"Total Liabilities : EUR {total_liabilities:,.2f}"
)

print(
    f"Total Equity      : EUR {total_equity:,.2f}"
)

print(
    f"Balance Difference: EUR {balance_difference:,.2f}"
)

print("\nCLOSING CONTROLS")
print("-" * 80)

print(controls.to_string(index=False))

if (
    controls["status"] == "PASS"
).all():
    print("\nMONTH-END CLOSE STATUS: PASS")
else:
    print("\nMONTH-END CLOSE STATUS: REVIEW REQUIRED")

print("\nReports created:")
print("- reports/trial_balance.csv")
print("- reports/income_statement.csv")
print("- reports/balance_sheet.csv")
print("- reports/month_end_controls.csv")

print("=" * 80)