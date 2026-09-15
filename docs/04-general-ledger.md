# SAP FI General Ledger

## 1. Purpose

The General Ledger is the central accounting record of RhineTech GmbH.

All financial transactions ultimately affect one or more G/L accounts. The General Ledger therefore provides the foundation for the Balance Sheet, Income Statement and financial reporting.

Company Code: DE01  
Chart of Accounts: RTCOA  
Currency: EUR  
Fiscal Year: January–December

---

## 2. Double-Entry Accounting

Every accounting document must satisfy:

Debit = Credit

For example, the initial capital contribution of €100,000 is recorded as:

Dr 100000 Bank Account        €100,000  
Cr 300000 Share Capital       €100,000

The accounting document is therefore balanced.

---

## 3. SAP Accounting Documents

Transactions are stored using accounting document numbers.

Examples from this project:

| Document | Type | Description |
|---|---|---|
| 100001 | SA | Initial capital contribution |
| 100002 | KR | Vendor rent invoice |
| 100003 | KR | Software supplier invoice |
| 100004 | DR | Consulting customer invoice |
| 100005 | DR | Software customer invoice |
| 100006 | DR | Support customer invoice |
| 100007 | SA | Salary posting |
| 100008 | KR | Asset purchase |
| 100009 | KR | Marketing invoice |
| 100010 | DZ | Customer incoming payment |
| 100011 | KZ | Vendor outgoing payment |
| 100012 | AA | Depreciation posting |

Document types are used here as a simplified representation of common SAP FI document categories.

---

## 4. Vendor Invoice Example

RhineTech receives an office rent invoice:

Net rent: €8,000  
VAT: €1,520  
Total payable: €9,520

Posting:

Dr 510000 Rent Expense        €8,000  
Dr 120000 Input VAT           €1,520  
Cr 200000 Accounts Payable    €9,520

Cost Center:

CC5000 — Operations

The FI component records the accounting transaction while CO captures the organizational responsibility for the expense.

---

## 5. Customer Invoice Example

RhineTech provides consulting services:

Net revenue: €35,000  
VAT: €6,650  
Customer receivable: €41,650

Posting:

Dr 110000 Accounts Receivable    €41,650  
Cr 400000 Consulting Revenue     €35,000  
Cr 210000 Output VAT              €6,650

Profit Center:

PC100 — Consulting

---

## 6. Customer Payment

When the customer pays the €41,650 invoice:

Dr 100000 Bank Account           €41,650  
Cr 110000 Accounts Receivable    €41,650

The Accounts Receivable balance associated with the invoice is cleared.

---

## 7. Vendor Payment

When the rent supplier is paid:

Dr 200000 Accounts Payable       €9,520  
Cr 100000 Bank Account           €9,520

The vendor liability is cleared.

---

## 8. Asset Acquisition

RhineTech purchases IT equipment for €12,000 plus VAT.

Dr 150000 Office & IT Equipment    €12,000  
Dr 120000 Input VAT                 €2,280  
Cr 200000 Accounts Payable         €14,280

The asset increases the company's non-current assets.

---

## 9. Depreciation

Monthly depreciation of €500 is posted as:

Dr 570000 Depreciation Expense       €500  
Cr 159000 Accumulated Depreciation   €500

Cost Center:

CC3000 — IT

Depreciation therefore affects both financial accounting and internal cost reporting.

---

## 10. FI/CO Integration

A transaction can contain several dimensions simultaneously.

Example:

G/L Account: 520000 Software Subscription Expense  
Company Code: DE01  
Cost Center: CC3000  
Currency: EUR  
Amount: €4,000

The G/L account determines what type of expense occurred.

The cost center identifies where the cost occurred.

This integration allows the same accounting information to support both external financial reporting and internal management analysis.

---

## 11. Data Validation

A core control requirement is that every accounting document must balance.

For every document:

Total Debit - Total Credit = 0

The project includes a Python reconciliation script that automatically checks this condition for all journal entries contained in `data/transactions.csv`.