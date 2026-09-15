# SAP S/4HANA FI/CO Enterprise Structure

## 1. Overview

This document defines the organizational structure used in the SAP FI/CO simulation for RhineTech GmbH.

The enterprise structure determines how financial transactions, costs, revenues, assets, and management reporting are organized within SAP S/4HANA.

The project uses the following hierarchy:

Client  
→ Company  
→ Company Code  
→ Controlling Area  
→ Profit Centers / Cost Centers

---

## 2. Client

### Client ID

100 — RhineTech SAP Environment

The client represents the highest organizational level in the SAP system.

A client contains organizational units, master data, configuration settings, and transaction data.

For this project, Client 100 represents the complete SAP environment used by RhineTech Group.

---

## 3. Company

### Company

RTG — RhineTech Group

A company represents an organizational unit used primarily for consolidated financial reporting.

RhineTech Group is assumed to operate one German legal entity in the initial project.

Future expansion could include additional subsidiaries in other European countries.

Example:

| Company | Description |
|---|---|
| RTG | RhineTech Group |

---

## 4. Company Code

### Company Code

DE01 — RhineTech GmbH Germany

The Company Code is one of the most important organizational units in SAP FI.

It represents the smallest organizational unit for which a complete set of financial statements can be produced.

Financial statements include:

- Balance Sheet
- Income Statement
- General Ledger
- Accounts Receivable
- Accounts Payable

### Configuration

| Attribute | Value |
|---|---|
| Company Code | DE01 |
| Company | RTG |
| Country | Germany |
| Currency | EUR |
| Language | English |
| Fiscal Year | January–December |
| Chart of Accounts | RTCOA |

All financial transactions in this project are recorded under Company Code DE01.

---

## 5. Chart of Accounts

### Chart of Accounts

RTCOA — RhineTech Operating Chart of Accounts

The Chart of Accounts contains the General Ledger accounts used by RhineTech GmbH.

Examples include:

- Cash
- Bank
- Accounts Receivable
- Accounts Payable
- Fixed Assets
- Revenue
- Salary Expense
- Rent Expense
- Marketing Expense
- Depreciation Expense

A detailed Chart of Accounts will be developed in the next stage of the project.

---

## 6. Fiscal Year

RhineTech GmbH uses a calendar fiscal year.

The financial year therefore runs from:

January 1  
to  
December 31

The fiscal year contains twelve normal posting periods.

Example:

| Period | Month |
|---|---|
| 01 | January |
| 02 | February |
| 03 | March |
| 04 | April |
| 05 | May |
| 06 | June |
| 07 | July |
| 08 | August |
| 09 | September |
| 10 | October |
| 11 | November |
| 12 | December |

Additional special periods may be used for year-end adjustment postings.

---

## 7. Controlling Area

### Controlling Area

RT01 — RhineTech Controlling Area

The Controlling Area is the central organizational unit used in SAP CO.

It enables RhineTech to perform internal management accounting.

The controlling area is used for:

- Cost Center Accounting
- Internal cost allocation
- Profitability monitoring
- Planning
- Budget control
- Management reporting

For this project:

| Attribute | Value |
|---|---|
| Controlling Area | RT01 |
| Description | RhineTech Controlling Area |
| Currency | EUR |
| Assigned Company Code | DE01 |

Company Code DE01 is assigned to Controlling Area RT01.

---

## 8. Cost Center Structure

Cost centers represent organizational areas where costs are incurred.

RhineTech uses the following cost centers:

| Cost Center | Department | Purpose |
|---|---|---|
| CC1000 | Finance | Accounting, reporting and financial administration |
| CC2000 | Sales | Customer acquisition and sales activities |
| CC3000 | IT | IT infrastructure and software systems |
| CC4000 | Human Resources | Recruitment and employee administration |
| CC5000 | Operations | General operational activities |

### Example

Suppose RhineTech receives an invoice for an HR recruitment platform:

```text
Recruitment Software Expense: €2,000
Cost Center: CC4000 — Human Resources