# SAP FI Accounts Receivable

## 1. Overview

Accounts Receivable (AR) manages amounts owed to RhineTech GmbH by customers.

Customer transactions are recorded in customer subledger accounts while the total receivable balance is reflected in the General Ledger through the reconciliation account.

Company Code: DE01

Reconciliation Account:

110000 — Accounts Receivable

---

## 2. Customer Master Data

RhineTech uses the following customers:

| Customer | Name | Payment Terms | Credit Limit |
|---|---|---:|---:|
| C1000 | Alpha Consulting AG | 30 days | €75,000 |
| C2000 | Nova Digital GmbH | 30 days | €100,000 |
| C3000 | WestBridge Services GmbH | 14 days | €40,000 |

Customer data includes:

- Customer ID
- Customer name
- Address
- Payment terms
- Credit limit
- Risk classification
- Reconciliation account

In SAP S/4HANA, customer master information is generally managed through the Business Partner framework.

---

## 3. Customer Reconciliation Account

All customer receivables in this project are linked to:

110000 — Accounts Receivable

Individual customer balances are maintained in the customer subledger.

Conceptually:

Customer C1000
Customer C2000
Customer C3000
       ↓
Customer Subledger
       ↓
110000 Accounts Receivable
       ↓
General Ledger

---

## 4. Customer Invoice

RhineTech provides consulting services worth €35,000 net.

VAT at 19%:

€6,650

Total customer invoice:

€41,650

Posting:

Dr 110000 Accounts Receivable       €41,650  
Cr 400000 Consulting Revenue        €35,000  
Cr 210000 Output VAT                 €6,650

Customer:

C1000 — Alpha Consulting AG

Profit Center:

PC100 — Consulting

---

## 5. Incoming Customer Payment

When Alpha Consulting AG pays the invoice:

Dr 100000 Bank Account              €41,650  
Cr 110000 Accounts Receivable       €41,650

The customer invoice is then cleared.

Invoice Document:

100004

Clearing Document:

100010

---

## 6. Open Item Management

Open-item management allows the finance department to distinguish between paid and unpaid customer invoices.

Current open receivables include:

| Customer | Outstanding |
|---|---:|
| Nova Digital GmbH | €59,500 |
| WestBridge Services GmbH | €23,800 |

Total Open Accounts Receivable:

€83,300

---

## 7. Customer Aging

Receivables aging groups unpaid customer invoices by how long they have been overdue.

The following aging buckets are used:

| Aging Bucket | Definition |
|---|---|
| Not Due | Payment deadline has not passed |
| 1–30 Days | Up to 30 days overdue |
| 31–60 Days | 31 to 60 days overdue |
| 61–90 Days | 61 to 90 days overdue |
| 90+ Days | More than 90 days overdue |

Aging analysis supports:

- Collection management
- Working-capital monitoring
- Liquidity planning
- Customer-risk assessment

---

## 8. Credit Management

Customer credit limits help RhineTech control exposure to individual customers.

Example:

Nova Digital GmbH

Credit Limit:

€100,000

Outstanding Receivable:

€59,500

Credit Utilization:

59.5%

Management can use this information to determine whether additional sales should be approved.

---

## 9. Credit Exposure

Credit exposure represents the amount currently owed by a customer.

A simple utilization measure is:

Credit Utilization = Outstanding Receivable / Credit Limit

A customer approaching or exceeding its credit limit may require additional review.

---

## 10. Accounts Receivable Controls

Important AR controls include:

### Customer Credit Limit Check

New sales should be reviewed when customer exposure approaches the approved credit limit.

### Invoice Accuracy

Customer invoices should contain correct prices, VAT, and payment terms.

### Incoming Payment Matching

Payments should be matched to the correct customer invoice.

### Open-Item Review

Overdue receivables should be reviewed regularly.

### Customer Subledger Reconciliation

The sum of customer balances should reconcile with the Accounts Receivable G/L account.

---

## 11. Order-to-Cash Connection

Accounts Receivable forms part of the Order-to-Cash process.

Typical flow:

Customer Order  
→ Service Delivery  
→ Customer Invoice  
→ Accounts Receivable  
→ Incoming Payment  
→ Clearing

---

## 12. AR Analytics

Python is used to calculate:

- Outstanding customer receivables
- Days overdue
- Aging categories
- Customer credit utilization
- Customer credit exposure
- Total Accounts Receivable

This demonstrates how financial accounting information can be combined with automated analytical controls.