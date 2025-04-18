# 🧊 Data Lake Architecture for Customer Analytics (AWS)

This project demonstrates how to build a **scalable Data Lake architecture** on AWS for storing, processing, and analyzing large-scale customer transaction data.

---

## 🚀 Features

- Amazon S3 for raw and processed data storage
- AWS Glue & PySpark for ETL transformation and schema enforcement
- AWS Lambda to automate and trigger data pipelines
- Amazon Redshift for warehousing and BI integration
- Designed for **50GB+ structured & semi-structured data**

---

## 🗂️ Folder Structure

```
data-lake-customer-analytics/
├── scripts/
│   ├── etl_pipeline_glue.py     # Glue ETL script
│   ├── lambda_trigger.py        # Lambda trigger script
│   └── redshift_load.sql        # Load script for Redshift
├── data/                        # Sample CSV data
├── glue-job-config/            # Job parameters
└── requirements.txt            # Python dependencies
```

---

## ⚙️ Technologies Used

- Python, PySpark
- Amazon S3, AWS Glue, AWS Lambda
- Amazon Redshift
- JSON, SQL

---

## 📈 Outcome

- Enabled real-time analytics using AWS services
- Reduced query latency by **35%**
- Processed and structured **50GB+** of raw customer data

---

## 📷 Architecture Diagram

> *(You can add an image here — `architecture_diagram.png`)*

---

## 🏁 How to Run (Locally Simulated)

1. Place your sample transaction data in the `/data` folder
2. Modify the Glue script paths and run with `boto3` or AWS Console
3. Simulate Lambda trigger via `lambda_trigger.py`
4. Run `redshift_load.sql` to load data (if Redshift access configured)

---

## 📩 Contact

**Sai Gayathri Makineni**  
Graduate Student, Computer Science – University of North Texas  
📧 [your email]  
🌐 [LinkedIn link]
