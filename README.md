Enterprise Batch Data Pipeline (AWS Architecture Simulation)
Project Overview

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
