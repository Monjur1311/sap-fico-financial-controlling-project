# SAP FI Asset Accounting

## 1. Overview

Asset Accounting is used to manage the fixed assets of RhineTech GmbH.

The project uses SAP FI-AA concepts to track:

- Asset acquisition
- Asset master information
- Acquisition value
- Useful life
- Depreciation
- Accumulated depreciation
- Net book value
- Cost-center assignment

Company Code:

DE01 — RhineTech GmbH Germany

---

## 2. Asset Master

The first fixed asset in the project is:

| Attribute | Value |
|---|---|
| Asset ID | A1000 |
| Asset Name | IT Equipment |
| Asset Class | IT Equipment |
| Acquisition Date | 22 January 2026 |
| Acquisition Cost | €12,000 |
| Useful Life | 24 months |
| Depreciation Method | Straight-Line |
| Cost Center | CC3000 — IT |
| Profit Center | PC200 — Software |

The useful life is a simplified project assumption used for this portfolio simulation.

---

## 3. Asset Accounts

The following General Ledger accounts are used:

| G/L Account | Description |
|---|---|
| 150000 | Office & IT Equipment |
| 159000 | Accumulated Depreciation |
| 570000 | Depreciation Expense |

---

## 4. Asset Acquisition

RhineTech purchases IT equipment for:

Net purchase price:

€12,000

Input VAT:

€2,280

Total vendor invoice:

€14,280

Accounting entry:

Dr 150000 Office & IT Equipment       €12,000  
Dr 120000 Input VAT                    €2,280  
Cr 200000 Accounts Payable            €14,280

The asset is capitalized rather than immediately expensed because it provides economic benefits over multiple accounting periods.

---

## 5. Depreciation

RhineTech uses straight-line depreciation for the simulated IT asset.

Formula:

Annual / Monthly Depreciation = Depreciable Amount / Useful Life

For Asset A1000:

€12,000 / 24 months = €500 per month

Monthly accounting entry:

Dr 570000 Depreciation Expense          €500  
Cr 159000 Accumulated Depreciation      €500

Cost Center:

CC3000 — IT

---

## 6. Accumulated Depreciation

Accumulated depreciation records the total depreciation recognized since the asset was placed in service.

After one month:

Acquisition Cost:

€12,000

Accumulated Depreciation:

€500

Net Book Value:

€11,500

After twelve months:

Accumulated Depreciation:

€6,000

Net Book Value:

€6,000

After twenty-four months:

Accumulated Depreciation:

€12,000

Net Book Value:

€0

---

## 7. Net Book Value

Net Book Value is calculated as:

Net Book Value = Acquisition Cost - Accumulated Depreciation

For example, after six months:

Acquisition Cost = €12,000

Accumulated Depreciation = €3,000

Net Book Value = €9,000

---

## 8. FI and CO Integration

Asset depreciation affects both FI and CO.

FI records:

Depreciation Expense  
Accumulated Depreciation

CO records:

Cost Center CC3000 — IT

This allows RhineTech to identify both the financial-statement impact and the department responsible for using the asset.

---

## 9. Balance Sheet Impact

The original asset appears on the Balance Sheet at its acquisition cost.

Example:

Office & IT Equipment:

€12,000

Less:

Accumulated Depreciation:

€500

Net Book Value:

€11,500

Accumulated depreciation is presented as a contra-asset account in this project.

---

## 10. Income Statement Impact

Depreciation Expense is recognized in the Income Statement.

The monthly depreciation expense is:

€500

The expense reduces accounting profit but does not represent a new cash payment during the depreciation posting.

The cash outflow occurred when the asset supplier was paid.

---

## 11. Asset Accounting Controls

Important asset controls include:

- Asset purchases must be properly authorized.
- Capital expenditures should be distinguished from operating expenses.
- Acquisition costs should be recorded accurately.
- Useful life and depreciation methods should be defined consistently.
- Depreciation postings should reconcile with the asset register.
- Retired or disposed assets should be removed from active asset records.
- Asset balances should reconcile with the General Ledger.

---

## 12. Asset Lifecycle

The simplified lifecycle used in this project is:

Asset Purchase  
→ Capitalization  
→ Asset Master Record  
→ Depreciation  
→ Net Book Value Monitoring  
→ Eventual Retirement / Disposal

The Python component of this project automatically creates the depreciation schedule and calculates accumulated depreciation and net book value.