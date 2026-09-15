import pandas as pd

# Load accounting transactions
df = pd.read_csv("data/transactions.csv")

# Calculate total debits and credits
total_debit = df["debit"].sum()
total_credit = df["credit"].sum()

print("=" * 60)
print("RHINETECH GMBH - SAP FI RECONCILIATION")
print("=" * 60)

print(f"\nTotal Debit : EUR {total_debit:,.2f}")
print(f"Total Credit: EUR {total_credit:,.2f}")

difference = total_debit - total_credit

print(f"Difference  : EUR {difference:,.2f}")

if abs(difference) < 0.01:
    print("\nPASS: General Ledger is balanced.")
else:
    print("\nFAIL: General Ledger is not balanced.")

# Check each accounting document individually
document_check = (
    df.groupby("document_no")
    .agg(
        total_debit=("debit", "sum"),
        total_credit=("credit", "sum")
    )
)

document_check["difference"] = (
    document_check["total_debit"]
    - document_check["total_credit"]
)

document_check["status"] = document_check["difference"].apply(
    lambda x: "PASS" if abs(x) < 0.01 else "FAIL"
)

print("\nDOCUMENT LEVEL RECONCILIATION")
print("-" * 60)
print(document_check)

failed_documents = document_check[
    document_check["status"] == "FAIL"
]

print("\n" + "=" * 60)

if failed_documents.empty:
    print("CONTROL RESULT: All accounting documents are balanced.")
else:
    print("CONTROL RESULT: Unbalanced documents detected.")
    print(failed_documents)

print("=" * 60)