import pandas as pd

REPORTING_DATE = pd.Timestamp("2026-02-28")

vendors = pd.read_csv("data/vendors.csv")
ap = pd.read_csv(
    "data/ap_open_items.csv",
    parse_dates=["invoice_date", "due_date", "clearing_date"]
)

# Keep only open invoices
open_items = ap[ap["status"] == "Open"].copy()

# Calculate outstanding balance
open_items["outstanding_amount"] = (
    open_items["invoice_amount"] - open_items["paid_amount"]
)

# Calculate overdue days
open_items["days_overdue"] = (
    REPORTING_DATE - open_items["due_date"]
).dt.days

# Prevent future invoices from showing negative overdue days
open_items["days_overdue"] = open_items["days_overdue"].clip(lower=0)


def aging_bucket(days):
    if days == 0:
        return "Not Due"
    elif days <= 30:
        return "1-30 Days"
    elif days <= 60:
        return "31-60 Days"
    elif days <= 90:
        return "61-90 Days"
    else:
        return "90+ Days"


open_items["aging_bucket"] = open_items["days_overdue"].apply(
    aging_bucket
)

# Add vendor information
report = open_items.merge(
    vendors[["vendor_id", "vendor_name"]],
    on="vendor_id",
    how="left"
)

report = report[
    [
        "vendor_id",
        "vendor_name",
        "invoice_document",
        "invoice_date",
        "due_date",
        "outstanding_amount",
        "days_overdue",
        "aging_bucket"
    ]
]

print("=" * 75)
print("RHINETECH GMBH - ACCOUNTS PAYABLE AGING REPORT")
print(f"Reporting Date: {REPORTING_DATE.date()}")
print("=" * 75)

print(report.to_string(index=False))

total_ap = report["outstanding_amount"].sum()

print("\n" + "-" * 75)
print(f"Total Outstanding Accounts Payable: EUR {total_ap:,.2f}")

aging_summary = (
    report.groupby("aging_bucket")["outstanding_amount"]
    .sum()
    .reset_index()
)

print("\nAP AGING SUMMARY")
print("-" * 75)
print(aging_summary.to_string(index=False))

# Export report
report.to_csv("reports/vendor_aging.csv", index=False)

print("\nReport exported to reports/vendor_aging.csv")
print("=" * 75)