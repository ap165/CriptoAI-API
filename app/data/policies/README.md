# Vistara Global Systems — Internal Policy Library

> **IMPORTANT DISCLAIMER**: Vistara Global Systems is an entirely fictional company. All employees, names, internal rules, approval thresholds, policies, locations, organizational relationships, and operational details in this dataset are fictional. These documents do not represent authentic policies from any real organization. This dataset was created for demonstration and testing of AI-powered enterprise knowledge assistants and Retrieval-Augmented Generation (RAG) systems.

---

## Company Profile

| Attribute | Details |
|---|---|
| **Company Name** | Vistara Global Systems |
| **Legal Name** | Vistara Global Systems Pvt. Ltd. |
| **Company Type** | Indian-origin mid-size multinational technology company |
| **Industry** | Enterprise Software, Cloud Computing, AI, Data Platforms, Cybersecurity, Digital Transformation |
| **Headquarters** | Bengaluru, India |
| **Employee Count** | 1,087 |
| **Operating Countries** | India, Singapore, UAE, United Kingdom, United States |

### Office Locations

**India:** Bengaluru (HQ), Hyderabad, Pune, Mumbai, Gurugram, Chennai, Kolkata, New Delhi

**International:** Singapore, Dubai, London, Austin

### Organizational Structure

| Department | Approx. Headcount |
|---|---|
| Engineering & Product | 340 |
| Sales & Marketing | 130 |
| Data & AI | 120 |
| Operations & Administration | 115 |
| Customer Success & Support | 110 |
| IT & Information Security | 85 |
| Finance & Procurement | 75 |
| HR & People | 60 |
| Legal & Compliance | 40 |
| Executive Leadership | 12 |
| **Total** | **1,087** |

---

## Dataset Overview

This dataset contains **65 standalone internal corporate policy documents** organized into 8 categories, forming a comprehensive enterprise knowledge base.

### Policy Categories

| # | Category | Policy Count | Folder |
|---|---|---|---|
| 01 | HR & People | 12 | `01_HR_and_People/` |
| 02 | Information Security | 12 | `02_Information_Security/` |
| 03 | Data & Privacy | 8 | `03_Data_and_Privacy/` |
| 04 | Finance & Procurement | 8 | `04_Finance_and_Procurement/` |
| 05 | Engineering & IT | 9 | `05_Engineering_and_IT/` |
| 06 | Legal & Compliance | 7 | `06_Legal_and_Compliance/` |
| 07 | Corporate & Administration | 5 | `07_Corporate_and_Administration/` |
| 08 | AI & Emerging Technology | 4 | `08_AI_and_Emerging_Technology/` |
| | **Total** | **65** | |

---

## Directory Structure

```
Vistara_Global_Systems_Policies/
│
├── README.md                          ← This file
├── POLICY_INDEX.md                    ← Complete policy index with metadata
├── policy_catalog.json                ← Machine-readable catalog (JSON)
├── policy_catalog.csv                 ← Machine-readable catalog (CSV)
├── rag_test_questions.md              ← 100+ RAG test questions
├── vistara_global_systems_employee_roster.xlsx  ← Employee directory (1,087 employees)
│
├── 01_HR_and_People/
│   ├── HR-001_Employee_Handbook.docx
│   ├── HR-002_Code_of_Conduct.docx
│   ├── HR-003_Leave_and_Time_Off_Policy.docx
│   ├── HR-004_Attendance_and_Working_Hours_Policy.docx
│   ├── HR-005_Remote_and_Hybrid_Work_Policy.docx
│   ├── HR-006_Employee_Privacy_Policy.docx
│   ├── HR-007_Anti-Harassment_and_Equal_Opportunity_Policy.docx
│   ├── HR-008_Employee_Grievance_and_Disciplinary_Policy.docx
│   ├── HR-009_Performance_Management_Policy.docx
│   ├── HR-010_Learning_and_Development_Policy.docx
│   ├── HR-011_Recruitment_and_Background_Verification_Policy.docx
│   └── HR-012_Onboarding_and_Offboarding_Policy.docx
│
├── 02_Information_Security/
│   ├── SEC-001_Information_Security_Policy.docx
│   ├── SEC-002_Access_Control_Policy.docx
│   ├── SEC-003_Password_and_Authentication_Policy.docx
│   ├── SEC-004_Multi-Factor_Authentication_Policy.docx
│   ├── SEC-005_Data_Classification_and_Handling_Policy.docx
│   ├── SEC-006_Acceptable_Use_Policy.docx
│   ├── SEC-007_Endpoint_Security_Policy.docx
│   ├── SEC-008_Network_Security_Policy.docx
│   ├── SEC-009_Email_and_Communications_Security_Policy.docx
│   ├── SEC-010_Remote_Access_Security_Policy.docx
│   ├── SEC-011_Security_Incident_Response_Policy.docx
│   └── SEC-012_Third-Party_Security_Policy.docx
│
├── 03_Data_and_Privacy/
│   ├── DATA-001_Data_Protection_and_Privacy_Policy.docx
│   ├── DATA-002_Data_Retention_and_Deletion_Policy.docx
│   ├── DATA-003_Data_Subject_Request_Policy.docx
│   ├── DATA-004_Cross-Border_Data_Transfer_Policy.docx
│   ├── DATA-005_Data_Breach_and_Notification_Policy.docx
│   ├── DATA-006_Records_Management_Policy.docx
│   ├── DATA-007_Data_Loss_Prevention_Policy.docx
│   └── DATA-008_Customer_Data_Handling_Policy.docx
│
├── 04_Finance_and_Procurement/
│   ├── FIN-001_Expense_Reimbursement_Policy.docx
│   ├── FIN-002_Business_Travel_Policy.docx
│   ├── FIN-003_Procurement_and_Purchasing_Policy.docx
│   ├── FIN-004_Vendor_Management_Policy.docx
│   ├── FIN-005_Purchase_Approval_and_Delegation_Policy.docx
│   ├── FIN-006_Corporate_Card_Policy.docx
│   ├── FIN-007_Invoice_Processing_Policy.docx
│   └── FIN-008_Financial_Reporting_and_Records_Policy.docx
│
├── 05_Engineering_and_IT/
│   ├── ENG-001_Secure_Software_Development_Policy.docx
│   ├── ENG-002_Production_Access_Policy.docx
│   ├── ENG-003_Change_Management_Policy.docx
│   ├── ENG-004_Code_Review_Policy.docx
│   ├── ENG-005_Open_Source_Software_Policy.docx
│   ├── ENG-006_Cloud_Security_Policy.docx
│   ├── ENG-007_Database_Security_Policy.docx
│   ├── ENG-008_Backup_and_Disaster_Recovery_Policy.docx
│   └── ENG-009_IT_Asset_and_Configuration_Management_Policy.docx
│
├── 06_Legal_and_Compliance/
│   ├── LEGAL-001_Anti-Bribery_and_Anti-Corruption_Policy.docx
│   ├── LEGAL-002_Conflict_of_Interest_Policy.docx
│   ├── LEGAL-003_Gifts_and_Entertainment_Policy.docx
│   ├── LEGAL-004_Whistleblower_Policy.docx
│   ├── LEGAL-005_Intellectual_Property_Policy.docx
│   ├── LEGAL-006_Confidential_Information_and_NDA_Policy.docx
│   └── LEGAL-007_Regulatory_Compliance_Policy.docx
│
├── 07_Corporate_and_Administration/
│   ├── CORP-001_Business_Continuity_Policy.docx
│   ├── CORP-002_Workplace_Health_and_Safety_Policy.docx
│   ├── CORP-003_Physical_Security_and_Office_Access_Policy.docx
│   ├── CORP-004_Corporate_Communications_and_Media_Policy.docx
│   └── CORP-005_Crisis_Management_Policy.docx
│
└── 08_AI_and_Emerging_Technology/
    ├── AI-001_Responsible_AI_Policy.docx
    ├── AI-002_Generative_AI_Usage_Policy.docx
    ├── AI-003_AI_Data_Privacy_Policy.docx
    └── AI-004_AI-Assisted_Software_Development_Policy.docx
```

---

## Naming Convention

All policy documents follow the format:

```
{POLICY_ID}_{Policy_Title_With_Underscores}.docx
```

**Policy ID Format:**
- `HR-XXX` — HR & People
- `SEC-XXX` — Information Security
- `DATA-XXX` — Data & Privacy
- `FIN-XXX` — Finance & Procurement
- `ENG-XXX` — Engineering & IT
- `LEGAL-XXX` — Legal & Compliance
- `CORP-XXX` — Corporate & Administration
- `AI-XXX` — AI & Emerging Technology

---

## Information Classification System

All documents use a consistent four-level classification:

| Level | Description | Handling |
|---|---|---|
| **PUBLIC** | Intended for public distribution | No restrictions |
| **INTERNAL** | For internal Vistara use only | Share within Vistara employees |
| **CONFIDENTIAL** | Sensitive business information | Need-to-know, encrypted, no external sharing without approval |
| **RESTRICTED** | Highest sensitivity | Named-individual access, CISO approval, full audit trail |

Most policy documents are classified as **Internal**. Security-sensitive documents are classified as **Confidential**.

---

## Cross-Reference Format

Policies cross-reference each other using their Policy IDs. Example:

> "Employees working outside India require approval under **HR-005 Remote and Hybrid Work Policy** and must comply with **SEC-010 Remote Access Security Policy** and **DATA-004 Cross-Border Data Transfer Policy**."

This creates deliberate dependencies between policies, enabling multi-document retrieval questions.

---

## RAG Usage Recommendations

### Ingestion

1. **Extract text** from DOCX files using appropriate parsers (python-docx, Apache Tika, Unstructured, etc.)
2. **Preserve structure** — section headings, tables, and lists are semantically important
3. **Chunk strategically** — recommended chunk size: 500-1000 tokens with overlap, respect section boundaries
4. **Include metadata** — policy ID, title, category, classification, version, and effective date in each chunk's metadata
5. **Use the catalog** — `policy_catalog.json` provides structured metadata for all 65 policies

### Retrieval

- Cross-reference questions often require retrieval from 2-5 policies
- Policy IDs serve as strong retrieval signals
- Tables contain critical threshold/approval information
- FAQ sections are high-value retrieval targets
- Scenarios provide contextual examples

### Testing

- Use `rag_test_questions.md` for evaluation
- Questions are categorized by complexity and cross-document requirements
- At least 40 questions require multi-document retrieval

---

## Employee Directory

The file `vistara_global_systems_employee_roster.xlsx` contains the complete directory of 1,087 fictional employees with:

- Employee ID (VGS-XXXXX format)
- Name, Department, Role
- Location, Country
- Employment Type (Full-Time / Contract)
- Join Date

---

## Dataset Generation Notes

- All content is synthetically generated
- No real company's confidential information was used
- Employee names are randomly generated Indian and international names
- Financial thresholds are in Indian Rupees (₹) unless otherwise specified
- Legal references are to actual legislation but all internal rules are fictional
- Approval hierarchies and organizational structures are internally consistent
- The dataset is designed to test enterprise RAG capabilities including:
  - Single-document factual retrieval
  - Multi-document reasoning
  - Cross-department policy resolution
  - Exception handling and edge cases
  - Approval workflow understanding
  - Scenario-based question answering

---

*This README is part of the Vistara Global Systems Internal Policy Library — a fictional enterprise RAG dataset.*
