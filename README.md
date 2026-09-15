# IBM Data Engineering Capstone Project: SoftCart Platform

[![IBM Data Engineering](https://img.shields.io/badge/IBM-Data%20Engineering%20Capstone-blue)]([https://www.coursera.org/professional-certificates/ibm-data-engineer](https://www.coursera.org/learn/data-enginering-capstone-project))
[![Apache Airflow](https://img.shields.io/badge/Orchestration-Apache%20Airflow-017CEE?logo=apacheairflow&logoColor=white)](https://airflow.apache.org/)
[![Database](https://img.shields.io/badge/Databases-MySQL%20%7C%20PostgreSQL%20%7C%20Db2-informational)](https://www.postgresql.org/)

An end-to-end data platform built for **SoftCart**, an e-commerce enterprise. This project covers transactional data modeling, automated ETL pipelines, orchestration, big data streaming analytics, and executive business intelligence dashboards.

---

## 🏗️ Architecture & Modules

### 1. Data Warehousing & Dimensional Modeling
- Designed a **Star Schema** to optimize analytical querying across sales events.
- Created dimension tables: `softcartDimDate`, `softcartDimCategory`, `softcartDimItem`, and `softcartDimCountry`.
- Implemented the central `softcartFactSales` table referencing surrogate keys.

### 2. Automated Incremental ETL (`automation.py`)
- Programmed a Python utility to bridge transactional data (MySQL staging) with the enterprise analytical warehouse (PostgreSQL/Db2).
- Extracts the latest `last_rowid` recorded in the warehouse and queries only new incremental records (`WHERE rowid > last_rowid`).
- Performs batch inserts via `cursor.executemany` with transaction safety.

### 3. Workflow Orchestration with Apache Airflow (`process_web_log.py`)
- Automated daily processing of web server access logs using a custom Airflow DAG.
- **`extract_data`**: Pulls client IP addresses using Linux command-line utilities (`cut`).
- **`transform_data`**: Filters out anomalous internal/bot traffic (`grep -v "198.46.149.143"`).
- **`load_data`**: Compresses and archives cleaned payloads into `weblog.tar`.
- Managed task retries, error alerting parameters, and pipeline execution dependencies (`extract_data >> transform_data >> load_data`).

### 4. Big Data Analytics with Apache Spark
- Processed high-volume clickstream and transaction feeds.
- Implemented Spark DataFrames and Spark SQL transformations to calculate rolling metrics and top-performing merchandise.

### 5. BI Dashboards (IBM Cognos Analytics)
- Built interactive management dashboards visualizing:
  - Month-wise gross sales progression for the year 2020.
  - Category-level sales splits and regional distribution.

---

## 🛠️ Tech Stack
- **Languages:** Python 3.10+, Bash, SQL
- **Orchestration:** Apache Airflow
- **Databases & Warehouses:** MySQL, PostgreSQL, IBM Db2
- **Big Data Engine:** Apache Spark / PySpark
- **Business Intelligence:** IBM Cognos Analytics
