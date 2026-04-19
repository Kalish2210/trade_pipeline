# 📊 Data Pipeline Project

A modular Python-based data pipeline for processing trade data from raw CSV files into a validated and cleaned dataset stored in PostgreSQL.

---

## 🚀 Project Overview

This project processes financial trade data through a structured ETL pipeline:

**Raw Data → Ingestion → Cleaning → Validation → Storage (PostgreSQL)**

---

## 📁 Project Structure


data_pipeline/
│
├── ingestion.py # Loads raw CSV data
├── cleaning.py # Cleans and transforms trade data
├── validation.py # Validates trade schema and rules
├── storage.py # Inserts data into PostgreSQL
├── run_pipeline.py # Main pipeline entry point
├── init.py # Package initializer
│
data/
└── trades.csv # Raw trade dataset


---

## ⚙️ Pipeline Flow

1. **Ingestion**
   - Reads `trades.csv`
   - Converts data into Python objects

2. **Cleaning**
   - Removes extra spaces
   - Fixes timestamps
   - Handles missing values

3. **Validation**
   - Checks required fields
   - Validates data types and ranges

4. **Storage**
   - Inserts cleaned data into PostgreSQL
   - Stores final structured trades table

---

## ▶️ How to Run

Run the pipeline using:

```bash
python data_pipeline/run_pipeline.py
🗄️ Database Setup

Make sure PostgreSQL is running and update credentials in storage.py or .env:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
📊 Output

After execution, cleaned trade data is stored in PostgreSQL table:

trades

You can view it using pgAdmin:

SELECT * FROM trades;
🧠 Key Features
Modular ETL pipeline design
Data validation layer
Automated cleaning logic
PostgreSQL integration
Scalable architecture for financial data
🛠️ Tech Stack
Python
PostgreSQL
Pandas (if used in ingestion)
psycopg2
