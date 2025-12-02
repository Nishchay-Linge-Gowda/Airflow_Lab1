# 🚀 Airflow Lab 1 — Employee Productivity Clustering Pipeline

This project demonstrates an end-to-end **MLOps workflow using Apache Airflow**, where a Machine Learning pipeline automatically:

1. **Loads an Employee Productivity dataset**
2. **Preprocesses & scales the numeric features**
3. **Builds a KMeans clustering model**
4. **Generates the SSE curve for the Elbow Method**
5. **Saves the final model**
6. **Loads the model and makes a test prediction**

All tasks are orchestrated using **Apache Airflow DAGs**, containerized via **Docker Compose**, and the ML logic is fully modular inside `lab.py`.

---

## 📂 Project Structure

```
LAB_1/
│
├── dags/
│   ├── airflow.py                       # Main Airflow DAG
│   │
│   ├── data/
│   │   └── employee_productivity.csv     # Your custom dataset
│   │
│   ├── model/
│   │   └── employee_model.sav            # Auto-generated model file
│   │
│   └── src/
│       ├── __init__.py
│       └── lab.py                        # All ML logic (ETL + ML pipeline)
│
├── logs/                                  # Airflow logs
├── plugins/
│
├── docker-compose.yaml                     # Airflow infra
├── setup.sh
└── README.md
```

---

## 📊 Dataset Used — Employee Productivity

Your dataset contains employee performance metrics:

| Column Name          | Description                         |
|----------------------|-------------------------------------|
| Hours_Worked         | Total hours worked in a week        |
| Tasks_Completed      | Number of finished tasks            |
| Errors_Made          | Mistakes made by the employee       |
| Productivity_Score   | Calculated performance score        |

This dataset is used for **unsupervised clustering**.

---

## 🎯 Workflow Steps (DAG Logic)

### **1️⃣ load_data_task**
- Reads `employee_productivity.csv`
- Serializes dataframe using pickle → Base64
- Pushes it to XCom

### **2️⃣ data_preprocessing_task**
- Drops missing values
- Selects numeric columns:
  - Hours_Worked  
  - Tasks_Completed  
  - Errors_Made  
  - Productivity_Score
- Scales using MinMaxScaler
- Returns Base64-encoded scaled array

### **3️⃣ build_save_model_task**
- Runs KMeans for `k = 1 to 10`
- Stores SSE values for Elbow Method
- Saves final model (`employee_model.sav`)

### **4️⃣ load_model_task**
- Loads saved model
- Runs the Elbow Method (KneeLocator)
- Loads test row from dataset
- Outputs a predicted cluster

---

## 🐳 Running the Project (Full Steps)

### **1️⃣ Start Airflow environment**
```bash
docker compose up airflow-init
```

### **2️⃣ Start all Airflow services**
```bash
docker compose up
```

### **3️⃣ Open Airflow UI**
```
http://localhost:8080
```

Login:
- Username: `airflow`
- Password: `airflow`

### **4️⃣ Trigger DAG**
- Go to **DAGs → Airflow_Lab1 → Trigger DAG**
- Watch each task turn **green**

---

## 📦 Model Output

After DAG runs, the model is saved at:

```
dags/model/employee_model.sav
```

A predicted cluster label appears in the logs of `load_model_task`.

---

## 🧠 Technologies Used

- **Apache Airflow**
- **Docker & Docker Compose**
- **Python 3.12**
- **Pandas**
- **Scikit-Learn**
- **KMeans Clustering**
- **KneeLocator (Elbow Method)**
- **XCom with Base64 Encoding**

---

## 📝 Example DAG Graph

```
load_data_task  
        ↓  
data_preprocessing_task  
        ↓  
build_save_model_task  
        ↓  
load_model_task
```


