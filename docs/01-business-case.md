# SAP FI/CO Business Case

## 1. Company Background

RhineTech GmbH is a fictional mid-sized German technology and consulting company headquartered in Düsseldorf. The company provides business consulting, software implementation, and technical support services to corporate clients across Germany.

As the company grows, management requires a more structured financial accounting and controlling system to improve financial transparency, cost control, reporting accuracy, and management decision-making.

The company therefore implements SAP S/4HANA Finance using the Financial Accounting (FI) and Controlling (CO) modules.

---

## 2. Business Problem

RhineTech GmbH currently manages several financial processes using separate spreadsheets and disconnected accounting records.

This creates several challenges:

- Limited visibility into company-wide financial performance
- Difficulty tracking expenses by department
- Manual reconciliation between customer, vendor, and general ledger accounts
- Limited budget-versus-actual analysis
- Weak integration between operational transactions and financial reporting
- Slow month-end closing
- Difficulty identifying profitable and unprofitable business areas
- Increased risk of accounting errors and duplicate transactions

Management therefore requires an integrated financial management system.

---

## 3. Project Objective

The objective of this project is to simulate an SAP FI/CO implementation for RhineTech GmbH and demonstrate how financial transactions can be captured, classified, controlled, and analyzed within an integrated ERP environment.

The project focuses on four main objectives:

1. Establish a structured financial accounting environment.
2. Track costs and revenues across organizational units.
3. Simulate core SAP FI/CO business processes.
4. Produce financial and management reports for decision-making.

---

## 4. SAP Modules in Scope

### Financial Accounting — SAP FI

The FI component will cover:

- General Ledger Accounting
- Accounts Payable
- Accounts Receivable
- Asset Accounting
- Bank Accounting
- VAT accounting
- Financial statement reporting
- Period-end closing

SAP FI will provide the external accounting view of RhineTech GmbH.

---

### Controlling — SAP CO

The CO component will cover:

- Cost Center Accounting
- Profit Center Accounting
- Internal cost allocation
- Budget versus actual analysis
- Departmental cost analysis
- Management reporting

SAP CO will provide the internal management accounting view of the company.

---

## 5. Organizational Structure

The SAP environment will use the following organizational structure.

### Company

RhineTech Group

### Company Code

DE01 — RhineTech GmbH Germany

### Country

Germany

### Local Currency

EUR

### Fiscal Year

January to December

### Chart of Accounts

RTCOA — RhineTech Operating Chart of Accounts

### Controlling Area

RT01 — RhineTech Controlling Area

---

## 6. Cost Center Structure

The following cost centers will be used to track operating expenses.

| Cost Center | Department |
|---|---|
| CC1000 | Finance |
| CC2000 | Sales |
| CC3000 | IT |
| CC4000 | Human Resources |
| CC5000 | Operations |

Cost centers allow management to identify which departments are responsible for company expenses.

For example, software infrastructure expenses may be assigned to the IT cost center, while recruitment expenses may be assigned to Human Resources.

---

## 7. Profit Center Structure

RhineTech GmbH generates revenue through three main business areas.

| Profit Center | Business Area |
|---|---|
| PC100 | Consulting |
| PC200 | Software |
| PC300 | Support |

Profit centers allow management to evaluate the financial performance of individual business areas.

This makes it possible to determine whether Consulting, Software, or Support activities contribute most strongly to overall company profitability.

---

## 8. Main Business Processes

The project will simulate several end-to-end SAP business processes.

### Procure-to-Pay

The Procure-to-Pay process covers the purchase of goods and services from vendors.

Typical process:

Purchase requirement  
→ Purchase order  
→ Goods or service receipt  
→ Vendor invoice  
→ Accounts payable  
→ Vendor payment

Example:

RhineTech purchases IT equipment for €5,000 from a technology supplier.

The transaction creates an expense or asset posting and a corresponding vendor liability.

---

### Order-to-Cash

The Order-to-Cash process covers revenue generated from customers.

Typical process:

Customer order  
→ Service delivery  
→ Customer invoice  
→ Accounts receivable  
→ Customer payment

Example:

RhineTech provides consulting services worth €35,000.

The transaction creates consulting revenue and a customer receivable.

---

### Record-to-Report

Record-to-Report covers the accounting and reporting cycle.

Typical activities include:

- Journal entries
- Account reconciliation
- Expense classification
- Depreciation posting
- Accruals
- Period closing
- Financial statement preparation

The final outputs include the Income Statement and Balance Sheet.

---

### Asset Acquisition

The company will also simulate the acquisition of fixed assets.

Example:

RhineTech purchases computer equipment for €12,000.

The asset is capitalized and depreciation expense is recognized over its useful economic life.

---

## 9. Sample Transactions

The project dataset will contain realistic simulated transactions such as:

| Transaction | Amount |
|---|---:|
| Consulting Revenue | €35,000 |
| Software Revenue | €50,000 |
| Support Revenue | €20,000 |
| Employee Salaries | €40,000 |
| Office Rent | €8,000 |
| Software Subscriptions | €4,000 |
| Marketing Expense | €6,000 |
| IT Equipment Purchase | €12,000 |
| Travel Expense | €3,500 |
| Depreciation Expense | €500 |

Each transaction will be assigned to appropriate General Ledger accounts, cost centers, and profit centers.

---

## 10. Example Accounting Entry

Suppose RhineTech receives an office rent invoice of €8,000.

The accounting entry is:

```text
Dr Rent Expense               €8,000
    Cr Vendor Payable                 €8,000
```

The expense can additionally be assigned to:

```text
Cost Center: CC5000
Department: Operations
```

When the vendor is paid:

```text
Dr Vendor Payable             €8,000
    Cr Bank Account                    €8,000
```

This demonstrates how SAP FI records the financial accounting impact while SAP CO tracks the internal cost responsibility.

---

## 11. Management Reporting

The system will produce several management reports.

These include:

- Income Statement
- Balance Sheet
- General Ledger summary
- Accounts Payable report
- Accounts Receivable report
- Customer aging report
- Vendor aging report
- Cost center expense report
- Profit center profitability report
- Budget-versus-actual analysis

These reports allow management to evaluate financial performance and identify areas requiring corrective action.

---

## 12. Analytics Integration

In addition to the SAP FI/CO simulation, Python will be used to analyze the financial data.

The analytics component will include:

- Expense analysis
- Revenue analysis
- Profitability analysis
- Cost-center comparison
- Budget variance analysis
- Customer receivable analysis
- Vendor payment analysis
- Financial reconciliation

Python libraries such as pandas and matplotlib will be used for data processing and visualization.

This provides an additional analytics layer on top of the SAP FI/CO business logic.

---

## 13. Expected Project Outcome

At the end of the project, the repository will demonstrate an end-to-end understanding of how SAP FI and CO support financial management within an organization.

The project will show how transactions flow from operational business activities into accounting records and management reports.

The final repository will demonstrate practical knowledge of:

- SAP FI/CO concepts
- Financial accounting
- Management accounting
- Business process integration
- Cost-center accounting
- Profit-center accounting
- Financial reporting
- Data reconciliation
- Python-based financial analytics

---

## 14. Project Disclaimer

This project is a portfolio simulation developed for educational purposes.

RhineTech GmbH is a fictional company, and all financial data used in this repository is simulated.

The project demonstrates SAP FI/CO concepts and business-process understanding and does not represent a production SAP implementation.