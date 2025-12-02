**MLOps Airflow Lab — Employee Productivity Clustering Pipeline**
1. Project Overview

This project implements a complete MLOps pipeline using Apache Airflow, Docker, and Machine Learning (KMeans).
The workflow automates data ingestion, preprocessing, model training, evaluation, and prediction using a custom Employee Productivity dataset.

The goal of this lab is to demonstrate:

How Airflow orchestrates ML tasks

How to modularize ML logic

How to serialize data through XCom

How to containerize workflows using Docker

How to adopt MLOps principles in a real pipeline

🎯 2. Problem Statement

Organizations often track employee productivity metrics such as working hours, number of tasks completed, and error rates.
This project clusters employees into groups using unsupervised learning (KMeans) to identify productivity patterns.

The pipeline answers:

How many natural clusters exist among employees?

Which cluster does a specific employee belong to?

How can we automate the entire ML workflow with Airflow?

🧠 3. Machine Learning Workflow

The ML logic (inside lab.py) performs:

Step 1 — Load Data

Reads the custom dataset:

dags/data/employee_productivity.csv

Step 2 — Preprocessing

Drops missing values

Selects numeric features:

Hours_Worked

Tasks_Completed

Errors_Made

Productivity_Score

Applies MinMaxScaler

Step 3 — Train Model

Runs KMeans for k = 1 to 10

Calculates SSE for each k (Elbow Curve)

Saves final model as:

dags/model/wholesale_model.sav

Step 4 — Evaluate Model

Uses KneeLocator to find optimal cluster count

Loads saved model

Performs a prediction using the first row of the dataset

📊 4. Dataset Description

File: employee_productivity.csv
Rows: 100
Type: Numeric only

Columns Used
Feature	Description
Hours_Worked	Total working hours per week
Tasks_Completed	Number of tasks completed
Errors_Made	Mistakes made during tasks
Productivity_Score	Performance metric (0–100)

This dataset replaces the default dataset from the original lab (customization requirement).

🧩 5. Project Architecture
LAB_1/
│
├── config/
│   └── airflow.cfg
│
├── dags/
│   ├── data/
│   │   └── employee_productivity.csv
│   │
│   ├── model/
│   │   └── wholesale_model.sav
│   │
│   ├── src/
│   │   ├── __init__.py
│   │   └── lab.py
│   │
│   └── airflow.py
│
├── logs/
├── plugins/
│
├── docker-compose.yaml
├── setup.sh
└── README.md

⚙️ 6. Technology Stack
Orchestration

Apache Airflow

Airflow Scheduler, Webserver, Worker

Docker & Docker Compose

Machine Learning

scikit-learn

MinMaxScaler

KMeans

kneed (for elbow detection)

Data Processing

pandas

pickle

base64 (for Airflow XCom passing)

Backend Infrastructure

PostgreSQL (Airflow metadata DB)

Redis (for CeleryExecutor)

🏗️ 7. Airflow DAG Breakdown

The DAG (airflow.py) defines 4 tasks:

1️⃣ load_data_task

Reads CSV

Serializes using pickle → base64

2️⃣ preprocess_data_task

Decodes

Drops NA

Scales numeric fields

3️⃣ build_model_task

Runs KMeans for k = 1 to 10

Saves final model

4️⃣ evaluate_model_task

Loads model

Computes Elbow method

Makes 1 prediction

DAG Graph Example

(Replace with actual screenshot)

load_data_task → preprocess_data_task → build_model_task → evaluate_model_task

🚀 8. How to Run the Project
STEP 1 — Start Docker Containers

Inside the lab folder:

docker compose up --build


This will start:

Airflow Scheduler

Webserver

Worker

Triggerer

Redis

Postgres

Wait until logs show:
Airflow webserver is ready

STEP 2 — Open Airflow

Go to:

👉 http://localhost:8080

Login

Username: Nishchay

Password: Nishchay@123

STEP 3 — Enable and Trigger the DAG

Find the DAG named:
employee_productivity_pipeline

Click ON

Click Trigger DAG

STEP 4 — Check Logs

Each task will show:

Prints

SSE list

Optimal K

Predicted cluster

📤 9. Outputs Generated
✔ Model Saved
dags/model/wholesale_model.sav

✔ SSE Values

Used for elbow curve.

✔ Optimal K

Calculated using kneed.

✔ Prediction Output

Cluster number for first employee row.

✔ Airflow Task Logs

All visible inside Airflow UI.

🖼️ 10. Screenshots (Add yours)
Airflow DAG View

Task Success

(You can upload your screenshots later.)

🔧 11. Customizations Done (Required for Lab Submission)

You successfully customized the project:

✔ Replaced dataset with Employee Productivity dataset
✔ Modified lab.py logic for new features
✔ Updated airflow.py according to new workflow
✔ Set Airflow dependencies via _PIP_ADDITIONAL_REQUIREMENTS
✔ Ran Airflow end-to-end successfully
✔ Fixed DAG errors
✔ Pushed to your GitHub repo

This confirms the lab is not identical to the template.

🚀 12. Future Improvements

If continuing the project, recommended enhancements:

Add visual elbow curve plotting

Store artifacts in S3 or MinIO

Add data validation (Great Expectations)

Include CI/CD (GitHub Actions)

Serve predictions using FastAPI

Add model monitoring

🏁 13. Conclusion

This project demonstrates a complete containerized MLOps pipeline using Airflow and Docker.
The workflow integrates:

Automated orchestration

Data pipelines

ML training and evaluation

End-to-end reproducibility

This lab replicates a real-world industry MLOps workflow and showcases strong understanding of Airflow-based ML orchestration.
