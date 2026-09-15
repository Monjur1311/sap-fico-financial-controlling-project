# SAP FI/CO Chart of Accounts

## 1. Overview

RhineTech GmbH uses the operating Chart of Accounts:

**RTCOA — RhineTech Operating Chart of Accounts**

The Chart of Accounts provides the structure for recording all financial transactions within Company Code DE01.

Each business transaction is posted to one or more General Ledger accounts.

For example, when RhineTech receives an office rent invoice, the transaction affects both a rent expense account and an accounts payable account.

---

## 2. Account Number Structure

For this portfolio project, the following account-number ranges are used.

| Range | Account Category |
|---|---|
| 100000–199999 | Assets |
| 200000–299999 | Liabilities |
| 300000–399999 | Equity |
| 400000–499999 | Revenue |
| 500000–599999 | Operating Expenses |

These ranges are project-specific and are used to create a clear and consistent financial structure.

---

## 3. Asset Accounts

| G/L Account | Account Name | Type |
|---|---|---|
| 100000 | Bank Account | Asset |
| 110000 | Accounts Receivable | Asset |
| 120000 | Input VAT 19% | Asset |
| 130000 | Prepaid Expenses | Asset |
| 150000 | Office & IT Equipment | Asset |
| 159000 | Accumulated Depreciation | Contra Asset |

Assets represent economic resources owned or controlled by RhineTech GmbH.

For example, customer receivables are recorded in Accounts Receivable until the customer makes payment.

---

## 4. Liability Accounts

| G/L Account | Account Name | Type |
|---|---|---|
| 200000 | Accounts Payable | Liability |
| 210000 | Output VAT 19% | Liability |
| 220000 | Payroll Liabilities | Liability |
| 230000 | Accrued Expenses | Liability |

Liabilities represent obligations RhineTech must pay to suppliers, employees, tax authorities, or other parties.

---

## 5. Equity Accounts

| G/L Account | Account Name | Type |
|---|---|---|
| 300000 | Share Capital | Equity |
| 310000 | Retained Earnings | Equity |

Equity represents the residual financial interest of the owners in RhineTech GmbH.

---

## 6. Revenue Accounts

| G/L Account | Account Name | Profit Center |
|---|---|---|
| 400000 | Consulting Revenue | PC100 |
| 410000 | Software Revenue | PC200 |
| 420000 | Support Revenue | PC300 |

Revenue accounts are normally credited when RhineTech provides services to customers.

Example:

RhineTech provides consulting services worth €10,000.

```text
Dr Accounts Receivable        10,000
    Cr Consulting Revenue             10,000