# 🏬 RetailLakehouse: End-to-End Databricks Lakehouse Architecture

An end-to-end Data Engineering project built on the **Databricks Lakehouse Platform** using the **Medallion Architecture (Bronze → Silver → Gold)**. This project demonstrates how raw CRM and ERP data is ingested, transformed, governed, and prepared for analytics using **Apache Spark (PySpark)**, **Delta Lake**, **Unity Catalog**, and **Databricks Workflows**.

---

## 📖 Project Overview

This project implements a modern **Data Lakehouse** architecture where raw data from multiple source systems is stored in cloud object storage, processed using Apache Spark, and transformed into analytics-ready Delta Tables.

The pipeline includes:

- Data ingestion from CRM & ERP source systems
- Raw data storage using Databricks Volumes
- Data transformation using Apache Spark (PySpark)
- Delta Lake for reliable storage
- Medallion Architecture (Bronze → Silver → Gold)
- Unity Catalog for centralized governance
- Automated ETL pipelines using Databricks Workflows
- Analytics-ready dimensional model for reporting

---

# 🏗️ Architecture

> **RetailLakehouse – End-to-End Databricks Lakehouse Architecture**

<p align="center">
<img src="docs/Databricks Lakehouse Architecture.png" width="1000">
</p>

---

# ⚙️ Technology Stack

| Category | Technology |
|-----------|------------|
| Platform | Databricks |
| Processing Engine | Apache Spark (PySpark) |
| Storage Framework | Delta Lake |
| Governance | Unity Catalog |
| Raw Data Storage | Databricks Volumes |
| Workflow Orchestration | Databricks Workflows |
| Architecture | Medallion Architecture |
| Language | Python (PySpark) |
| Source Systems | CRM & ERP |

---

# 🏛️ Medallion Architecture

## 🥉 Bronze Layer

The Bronze layer ingests raw CRM and ERP datasets from Databricks Volumes into Delta Tables without applying business transformations.

### Tables

- crm_cust_info
- crm_prd_info
- crm_sales_details
- erp_cust_az12
- erp_loc_a101
- erp_px_cat_g1v2

---

## 🥈 Silver Layer

The Silver layer cleanses, validates, standardizes, and transforms raw datasets into trusted business-ready datasets.

### Transformations

- Data type conversions
- Column renaming
- Null handling
- Invalid date correction
- Country standardization
- Gender standardization
- Product categorization
- Duplicate handling
- Business rule validation
- Sales & pricing corrections

### Tables

- crm_customers
- crm_products
- crm_sales
- erp_customers_info
- erp_locations
- erp_product_category

---

## 🥇 Gold Layer

The Gold layer contains analytics-ready dimensional models designed for reporting and business intelligence.

### Tables

- dim_customers
- dim_products
- fact_sales

---

# 🔄 Data Flow

```text
CRM & ERP Source Systems
        │
        ▼
Cloud Object Storage
        │
        ▼
Databricks Volumes
        │
        ▼
Apache Spark (PySpark)
        │
        ▼
Bronze Delta Tables
        │
        ▼
Silver Delta Tables
        │
        ▼
Gold Delta Tables
        │
        ▼
Power BI / Tableau / Machine Learning
```

---

# 🚀 Pipeline Automation

The complete ETL pipeline is orchestrated using **Databricks Workflows**.

### Schedule

- Daily Execution
- **02:00 AM (UTC+05:30)**

### Execution Order

```text
Bronze
   │
   ▼
Silver
   │
   ▼
Gold
```

---

# 🔐 Data Governance

The project leverages **Unity Catalog** to provide:

- Centralized metadata management
- Fine-grained access control
- Data lineage
- Secure data discovery
- Governance across the Lakehouse

---

# 📂 Repository Structure

```text
RetailLakehouse/
│
├── notebooks/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── architecture/
│   └── lakehouse_architecture.png
│
├── datasets/
│
├── README.md
│
└── LICENSE
```

---

# ⭐ Key Features

- End-to-End Databricks Lakehouse implementation
- Medallion Architecture (Bronze → Silver → Gold)
- Apache Spark (PySpark) transformations
- Delta Lake for ACID-compliant storage
- Unity Catalog for governance
- Databricks Volumes for raw data management
- Automated ETL using Databricks Workflows
- Analytics-ready dimensional model
- Production-style project structure


# 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Ravi Teja**

If you found this project helpful, consider giving it a ⭐ on GitHub!
