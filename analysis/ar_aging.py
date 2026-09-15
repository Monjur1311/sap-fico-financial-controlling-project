import pandas as pd

REPORTING_DATE = pd.Timestamp("2026-02-28")

customers = pd.read_csv("data/customers.csv")

ar = pd.read_csv(
    "data/ar_open_items.csv",
    parse_dates=[
        "invoice_date",
        "due_date",
        "clearing_date"
    ]
)

# Select unpaid customer invoices
open_items = ar[ar["status"] == "Open"].copy()

# Outstanding balance
open_items["outstanding_amount"] = (
    open_items["invoice_amount"]
    - open_items["paid_amount"]
)

# Calculate days overdue
open_items["days_overdue"] = (
    REPORTING_DATE - open_items["due_date"]
).dt.days


def aging_bucket(days):
    if days <= 0:
        return "Not Due"
    elif days <= 30:
        return "1-30 Days"
    elif days <= 60:
        return "31-60 Days"
    elif days <= 90:
        return "61-90 Days"
    else:
        return "90+ Days"


open_items["aging_bucket"] = (
    open_items["days_overdue"]
    .apply(aging_bucket)
)

# Merge customer master data
report = open_items.merge(
    customers[
        [
            "customer_id",
            "customer_name",
            "credit_limit",
            "risk_class"
        ]
    ],
    on="customer_id",
    how="left"
)

# Calculate credit utilization
report["credit_utilization_pct"] = (
    report["outstanding_amount"]
    / report["credit_limit"]
    * 100
)

# Credit warning
report["credit_status"] = report[
    "credit_utilization_pct"
].apply(
    lambda x: (
        "High Exposure"
        if x >= 80
        else "Within Limit"
    )
)

report = report[
    [
        "customer_id",
        "customer_name",
        "invoice_document",
        "invoice_date",
        "due_date",
        "outstanding_amount",
        "days_overdue",
        "aging_bucket",
        "credit_limit",
        "credit_utilization_pct",
        "risk_class",
        "credit_status"
    ]
]

print("=" * 90)
print("RHINETECH GMBH - ACCOUNTS RECEIVABLE AGING REPORT")
print(f"Reporting Date: {REPORTING_DATE.date()}")
print("=" * 90)

print(report.to_string(index=False))

total_ar = report["outstanding_amount"].sum()

print("\n" + "-" * 90)
print(
    f"Total Outstanding Accounts Receivable: "
    f"EUR {total_ar:,.2f}"
)

aging_summary = (
    report.groupby("aging_bucket")[
        "outstanding_amount"
    ]
    .sum()
    .reset_index()
)

print("\nAR AGING SUMMARY")
print("-" * 90)
print(aging_summary.to_string(index=False))

credit_summary = report[
    [
        "customer_name",
        "outstanding_amount",
        "credit_limit",
        "credit_utilization_pct",
        "credit_status"
    ]
]

print("\nCUSTOMER CREDIT EXPOSURE")
print("-" * 90)
print(credit_summary.to_string(index=False))

# Export report
report.to_csv(
    "reports/customer_aging.csv",
    index=False
)

print(
    "\nReport exported to "
    "reports/customer_aging.csv"
)

print("=" * 90)