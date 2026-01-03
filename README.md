# Data Engineering ETL Pipeline (PostgreSQL)

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

## 📌 Project Overview

This project demonstrates a **robust ETL (Extract, Transform, Load) pipeline** built using **Python**, **Pandas**, and **PostgreSQL**. It simulates a real-world workflow where raw data is extracted from a CSV source, transformed to meet business requirements, and loaded into a relational database for analytics and reporting.

Designed for aspiring data engineers, this project showcases:

* Modular ETL architecture
* Database integration with PostgreSQL
* Environment variable management for security
* Clean, reproducible project structure

---

## 🏗 Architecture Diagram

```text
CSV File (Source)
     ↓
[ Extract ]  →  [ Transform ]  →  [ Load ]
     ↓              ↓               ↓
  Pandas         Pandas         PostgreSQL
```

---

## 📂 Project Structure

```text
data_engineering/
│── etl/
│   ├── __init__.py
│   ├── extract.py      # Extracts raw data
│   ├── transform.py    # Cleans & transforms data
│   ├── load.py         # Loads data into PostgreSQL
│   └── pipeline.py     # Orchestrates ETL steps
│
│── data/
│   └── employees.csv   # Source dataset
│
│── .env                # Environment variables (ignored in GitHub)
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
```

---

## 🛠️ Technologies Used

* **Python 3.13**
* **Pandas** – data manipulation
* **SQLAlchemy** – database engine/ORM
* **PostgreSQL** – relational database
* **psycopg2** – PostgreSQL driver
* **python-dotenv** – environment variable management
* **Git & GitHub** – version control

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Amon-Mugo/data-engineering-etl.git
cd data-engineering-etl
```

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=data_engineering_test
DB_USER=postgres
DB_PASSWORD=YOUR_PASSWORD
```

⚠️ `.env` is ignored from GitHub to protect sensitive data.

---

## 🚀 Running the ETL Pipeline

From the project root, run:

```bash
python -m etl.pipeline
```

Expected output:

```text
Starting ETL pipeline...
Data extracted
Data transformed
Data loaded into PostgreSQL
Pipeline finished successfully
```

---

## 🗄️ Database Verification

After running the pipeline, connect to PostgreSQL and run:

```sql
SELECT * FROM employees;
```

Expected result:

* Cleaned employee records
* `age` as integer
* `salary` increased by 10%

---

## 🔐 Security Best Practices

* Database credentials are stored in `.env`
* `.env` and `venv/` are excluded from GitHub via `.gitignore`
* Modular code avoids hardcoding sensitive data

---

## 📈 Skills Demonstrated

* ETL pipeline design and orchestration
* Data cleaning & transformation
* PostgreSQL integration
* Python project structuring
* Environment-based configuration
* Git version control best practices

---

## 🔮 Future Improvements

* Add logging instead of print statements
* Implement data validation checks
* Incremental data loading
* Dockerize the pipeline
* Schedule ETL with Airflow or Cron jobs

---

## 👤 Author

**Amon**
Aspiring Data Engineer | Data Science Background

---

## ⭐ Why This Project Matters

This project reflects **real entry-level data engineering work** and is suitable for:

* Portfolio presentation
* Internship applications
* Junior Data Engineer roles
