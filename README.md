# IBM Data Engineering Capstone Project: SoftCart Platform

[![IBM Data Engineering](https://img.shields.io/badge/IBM-Data%20Engineering%20Capstone-blue)](https://www.coursera.org/learn/data-enginering-capstone-project)

An end-to-end data platform built for **SoftCart**, an e-commerce enterprise. This project covers transactional data modeling, automated ETL pipelines, orchestration, big data streaming analytics, and business intelligence dashboards.

---

## Architecture & Modules

### 1. Data Warehousing & Dimensional Modeling
- Designed a data warehouse using pgAdmin ERD design tool and created a **Star Schema** to optimize analytical querying across sales events.
- Created dimension tables: `softcartDimDate`, `softcartDimCategory`, `softcartDimItem`, and `softcartDimCountry`.
- Implemented the central `softcartFactSales` table referencing surrogate keys.

### 2. Automated Incremental ETL (`automation.py`)
- Set up an ETL process using Python to automate the extraction of daily transactional data from the MySQL database, transform it, and then load it into a data warehouse using PostgreSQL.
- Extracts the latest `last_rowid` recorded in the warehouse and queries only new incremental records (`WHERE rowid > last_rowid`).

### 3. Workflow Orchestration with Apache Airflow (`process_web_log.py`)
- Automated daily processing of web server access logs using a custom Airflow DAG and stored it in a format to prepare it for loading into the Big Data platform.
- **`extract_data`**: Pulls client IP addresses using Linux command-line utilities (`cut`).
- **`transform_data`**: Filters out anomalous internal traffic (`grep -v "198.46.149.143"`).
- **`load_data`**: Compresses and archives cleaned payloads into `weblog.tar`.

### 4. Big Data Analytics with Apache Spark (`spark_streaming.ipynb`)
- Implemented Spark DataFrames and Spark SQL transformations to analyse search terms.

### 5. BI Dashboards (IBM Cognos Analytics)
- Built dashboards visualizing:
  - Month-wise total sales for the year 2020.
  - Category-wise sales of electronic goods.
  - Month-wise total sales for a given year.

---

## 🛠️ Tech Stack
- **Languages:** Python, Bash, SQL
- **Orchestration:** Apache Airflow
- **Databases & Warehouses:** MySQL, PostgreSQL
- **Big Data Engine:** Apache Spark / PySpark
- **Business Intelligence:** IBM Cognos Analytics
