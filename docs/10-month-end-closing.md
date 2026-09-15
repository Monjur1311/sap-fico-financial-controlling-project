# SAP FI Month-End Closing and Record-to-Report

## 1. Overview

Month-end closing is the process of reviewing, reconciling and finalizing accounting information for a reporting period.

For RhineTech GmbH, the January 2026 close combines information from:

- General Ledger
- Accounts Payable
- Accounts Receivable
- VAT
- Asset Accounting
- Cost Center Accounting
- Profit Center Accounting

Company Code:

DE01 — RhineTech GmbH Germany

Reporting Period:

January 2026

---

## 2. Record-to-Report Process

The simplified Record-to-Report process used in this project is:

Business Transactions  
→ Journal Entries  
→ General Ledger  
→ Subledger Reconciliation  
→ Depreciation  
→ VAT Review  
→ Trial Balance  
→ Income Statement  
→ Balance Sheet  
→ Management Reporting

---

## 3. General Ledger Reconciliation

All accounting documents must satisfy:

Total Debit = Total Credit

For January 2026:

Total Debit:

€352,320

Total Credit:

€352,320

Difference:

€0

Therefore the General Ledger is balanced.

---

## 4. Accounts Receivable Reconciliation

The Accounts Receivable G/L balance is:

110000 Accounts Receivable

€83,300

Open customer balances are:

Nova Digital GmbH:

€59,500

WestBridge Services GmbH:

€23,800

Total customer open items:

€83,300

Therefore:

Customer Subledger = Accounts Receivable G/L

Reconciliation difference:

€0

---

## 5. Accounts Payable Reconciliation

The Accounts Payable G/L balance is:

200000 Accounts Payable

€26,180

Open vendor balances are:

CloudStack Software GmbH:

€4,760

TechSource GmbH:

€14,280

MarketBoost GmbH:

€7,140

Total vendor open items:

€26,180

Therefore:

Vendor Subledger = Accounts Payable G/L

Reconciliation difference:

€0

---

## 6. VAT Position

Input VAT:

€5,700

Output VAT:

€19,950

Net VAT payable:

€19,950 - €5,700 = €14,250

RhineTech therefore has a net VAT liability of:

€14,250

For simplicity, the project retains Input VAT and Output VAT in separate G/L accounts at month-end rather than posting a VAT clearing entry.

---

## 7. Asset Accounting Reconciliation

Asset acquisition cost:

€12,000

Accumulated depreciation:

€500

Net book value:

€11,500

January depreciation expense:

€500

The fixed-asset balance therefore agrees with the simulated asset register.

---

## 8. Income Statement

Revenue:

Consulting Revenue:

€35,000

Software Revenue:

€50,000

Support Revenue:

€20,000

Total Revenue:

€105,000

Operating Expenses:

Salary Expense:

€40,000

Rent Expense:

€8,000

Software Subscription Expense:

€4,000

Marketing Expense:

€6,000

Depreciation Expense:

€500

Total Operating Expenses:

€58,500

Operating Profit:

€105,000 - €58,500 = €46,500

---

## 9. Balance Sheet

### Assets

Bank:

€92,130

Accounts Receivable:

€83,300

Input VAT:

€5,700

Office & IT Equipment:

€12,000

Less Accumulated Depreciation:

€500

Total Assets:

€192,630

### Liabilities

Accounts Payable:

€26,180

Output VAT:

€19,950

Total Liabilities:

€46,130

### Equity

Share Capital:

€100,000

Current Period Profit:

€46,500

Total Equity:

€146,500

### Balance Check

Liabilities + Equity:

€46,130 + €146,500 = €192,630

Total Assets:

€192,630

Difference:

€0

The Balance Sheet is therefore balanced.

---

## 10. Month-End Closing Controls

The following controls are performed:

1. Verify that total debits equal total credits.
2. Verify that every accounting document balances.
3. Reconcile Accounts Receivable with customer open items.
4. Reconcile Accounts Payable with vendor open items.
5. Review Input VAT and Output VAT.
6. Confirm depreciation posting.
7. Reconcile fixed-asset book value.
8. Produce the Trial Balance.
9. Produce the Income Statement.
10. Produce the Balance Sheet.
11. Confirm that Assets equal Liabilities plus Equity.

---

## 11. Management Reporting

After financial closing, management can review:

- Revenue by business unit
- Profit-center profitability
- Cost-center budget variance
- Customer aging
- Vendor aging
- Working-capital exposure
- Operating profit
- Balance-sheet position

This demonstrates the integration between SAP FI and SAP CO.

---

## 12. Python Automation

Python is used to automate the month-end close by:

- Aggregating General Ledger balances
- Producing a Trial Balance
- Reconciling AP and AR subledgers
- Calculating VAT exposure
- Calculating asset net book value
- Producing the Income Statement
- Producing the Balance Sheet
- Running accounting control checks

The resulting reports are exported to the `reports` folder.