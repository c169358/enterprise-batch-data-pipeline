## Enterprise Batch Data Pipeline 
## Project Overview

This project simulates an enterprise-grade batch data pipeline designed for processing daily banking transaction data.

The pipeline demonstrates structured ETL (Extract, Transform, Load) implementation aligned with AWS-based data architecture principles.

Business Problem

Retail banking systems generate large volumes of daily transaction data.
To support reporting, fraud monitoring, and analytics, this data must be processed in batch mode and loaded into a centralized warehouse.

This project simulates:

Daily transaction ingestion

Data validation and transformation

Structured warehouse loading

Scalable enterprise architecture design

Architecture (Conceptual Flow)

Raw Transaction File →
Data Extraction Layer →
Transformation & Validation →
Warehouse Load →
Analytics & Reporting

Tech Stack

Python

Pandas

AWS Architecture Concepts (S3, Redshift simulation)

Git (SSH-based version control)

Modular Project Structure

Project Structure
dags/       - Workflow orchestration (Airflow - future phase)
scripts/    - ETL logic
data/       - Raw input files
sql/        - Warehouse queries
docs/       - Architecture diagrams
## Pipeline Architecture

Raw Data (CSV)
      ↓
Extraction Layer (extract.py)
      ↓
Transformation Layer (transform.py)
      ↓
Load Layer (load.py)
      ↓
SQLite Warehouse (warehouse.db)

Orchestrated by: pipeline.py
### Production-Style Features Implemented

- Modular transformation functions
- Duplicate detection
- Structured logging
- Basic anomaly detection
- Idempotent load behavior
- Orchestration separation

## Enterprise Batch Data Pipeline Architecture

Raw Data (CSV)
      ↓
Extraction Layer (extract.py)
      ↓
Transformation Layer (transform.py)
      - Duplicate removal
      - Data validation
      - Classification logic
      - Anomaly detection
      ↓
Staging Table (transactions_staging)
      ↓
Merge / Upsert Logic
      ↓
Main Warehouse Table (transactions)

Orchestrated via: pipeline.py
Config-driven: config/config.json
Tested with: pytest

## Key Engineering Features

- Modular ETL architecture
- Environment-based configuration (dev/prod)
- CLI-driven execution
- Structured logging
- Basic anomaly detection
- Staging + merge (idempotent load)
- Unit testing with pytest
- 
## How to Run

1. Install dependencies:
   pip install pandas pytest

2. Run pipeline:
   python scripts/pipeline.py data/transactions_raw.csv dev

3. Run unit tests:
   pytest

