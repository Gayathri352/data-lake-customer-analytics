# Data Lake Architecture for Customer Analytics (AWS)

This project demonstrates the implementation of a scalable Data Lake architecture using Amazon Web Services (AWS) to store, process, and analyze large-scale customer transaction data.

---

## Features

- Utilizes **Amazon S3** for storing raw and processed data
- Implements **ETL pipelines** using **AWS Glue** and **PySpark** for data transformation and schema enforcement
- Automates workflows with **AWS Lambda** to trigger ETL jobs
- Uses **Amazon Redshift** for data warehousing and analytics
- Designed to handle over **50GB of structured and semi-structured** customer transaction data

---

## Folder Structure

data-lake-customer-analytics/
├── scripts/
│   ├── etl_pipeline_glue.py     # Glue ETL script
│   ├── lambda_trigger.py        # Lambda trigger script
│   └── redshift_load.sql        # Load script for Redshift
├── data/                        # Sample CSV data
├── glue-job-config/            # Job parameters
└── requirements.txt            # Python dependencies

## Technologies Used

- Python, PySpark
- AWS S3, AWS Glue, AWS Lambda
- Amazon Redshift
- SQL, JSON

---

## Project Outcome

- Enabled real-time analytics on customer data using AWS services
- Reduced query latency by **35%**
- Successfully processed and structured over **50GB of raw data** for business insights

---

## How to Run (Local Simulation)

> Note: This project was designed for deployment in AWS but can be simulated locally in google colab for demonstration purposes.

1. Place sample CSV data in the `/data` folder
2. Run the ETL script (`scripts/etl_pipeline_glue.py`) using a local PySpark environment or simulate via Google Colab
3. Trigger the Lambda script (`scripts/lambda_trigger.py`) to simulate automation
4. Use `redshift_load.sql` to load the data into Redshift or a compatible SQL environment

---

## Author

**Sai Gayathri Makineni**  
Graduate Student – M.S. Computer Science  
University of North Texas  
Email: saigayathri18@gmail.com  
LinkedIn: https://www.linkedin.com/in/sai-gayathri-makineni/
