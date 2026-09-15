# SAP FI Accounts Payable

## 1. Overview

Accounts Payable (AP) manages financial obligations of RhineTech GmbH toward suppliers and service providers.

In SAP FI, vendor transactions are recorded in vendor subledger accounts while the corresponding total balance is automatically reflected in the Accounts Payable reconciliation account in the General Ledger.

Company Code: DE01

Reconciliation Account:

200000 — Accounts Payable

---

## 2. Vendor Master Data

RhineTech uses the following vendors:

| Vendor | Supplier | Category | Payment Terms |
|---|---|---|---:|
| V1000 | RheinOffice Immobilien GmbH | Property Services | 14 days |
| V2000 | CloudStack Software GmbH | Software | 14 days |
| V3000 | TechSource GmbH | IT Equipment | 30 days |
| V4000 | MarketBoost GmbH | Marketing | 30 days |

Vendor master data allows SAP to store information such as:

- Vendor name
- Address
- Payment terms
- Currency
- Reconciliation account
- Bank details
- Tax information

---

## 3. Vendor Reconciliation Account

All project vendors use:

200000 — Accounts Payable

Individual transactions are maintained in the vendor subledger.

The General Ledger therefore contains the aggregate Accounts Payable balance rather than a separate G/L account for every supplier.

Conceptually:

Vendor V1000
Vendor V2000
Vendor V3000
Vendor V4000
        ↓
Accounts Payable Subledger
        ↓
200000 Accounts Payable
        ↓
General Ledger

---

## 4. Vendor Invoice Posting

RhineTech receives a software invoice from CloudStack Software GmbH.

Net amount:

€4,000

Input VAT:

€760

Total invoice:

€4,760

Posting:

Dr 520000 Software Subscription Expense     €4,000  
Dr 120000 Input VAT                           €760  
Cr 200000 Accounts Payable                  €4,760

Vendor:

V2000 — CloudStack Software GmbH

Cost Center:

CC3000 — IT

---

## 5. Payment Terms

Payment terms determine when a vendor invoice becomes due.

Example:

Invoice date:

08 January 2026

Payment terms:

14 days

Due date:

22 January 2026

If the invoice remains unpaid after the due date, it becomes overdue.

---

## 6. Vendor Payment

The office rent invoice was originally recorded as:

Dr Rent Expense             €8,000  
Dr Input VAT                €1,520  
Cr Accounts Payable         €9,520

When RheinOffice Immobilien GmbH is paid:

Dr Accounts Payable         €9,520  
Cr Bank                     €9,520

The vendor open item is then cleared.

Invoice Document:

100002

Payment / Clearing Document:

100011

---

## 7. Open Item Management

As of the AP reporting date, open invoices include:

| Vendor | Amount |
|---|---:|
| CloudStack Software GmbH | €4,760 |
| TechSource GmbH | €14,280 |
| MarketBoost GmbH | €7,140 |

Total Open Accounts Payable:

€26,180

Open-item management helps the finance department determine:

- Which invoices remain unpaid
- Which invoices are overdue
- When payments are due
- Which vendor liabilities require attention

---

## 8. AP Aging

Vendor aging classifies unpaid invoices according to the number of days they are overdue.

The project uses the following buckets:

| Aging Bucket | Definition |
|---|---|
| Not Due | Payment deadline has not passed |
| 1–30 Days | Up to 30 days overdue |
| 31–60 Days | 31 to 60 days overdue |
| 61–90 Days | 61 to 90 days overdue |
| 90+ Days | More than 90 days overdue |

AP aging supports liquidity management and payment planning.

---

## 9. Accounts Payable Controls

Several controls are important within the AP process.

### Duplicate Invoice Control

Invoices should be checked for duplicate vendor invoice numbers and amounts.

### Payment-Term Control

Due dates should correspond to agreed vendor payment terms.

### Invoice Accuracy

Invoice amounts and VAT calculations should be validated.

### Open-Item Reconciliation

The vendor subledger should reconcile with the Accounts Payable G/L reconciliation account.

### Payment Authorization

Vendor payments should follow appropriate approval procedures.

---

## 10. Procure-to-Pay Connection

Accounts Payable forms a major part of the Procure-to-Pay process.

Typical flow:

Purchase Requirement  
→ Purchase Order  
→ Goods / Service Receipt  
→ Vendor Invoice  
→ Accounts Payable  
→ Payment  
→ Clearing

Later stages of this project will document this complete process separately.

---

## 11. AP Analytics

Python is used in this project to analyze vendor liabilities.

The analysis calculates:

- Outstanding vendor balances
- Invoice due dates
- Days overdue
- Aging categories
- Total Accounts Payable
- Vendor exposure

This demonstrates how SAP FI data can be combined with financial analytics and automated controls.