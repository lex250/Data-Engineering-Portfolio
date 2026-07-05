# 🧬 Supplement Experiments Data Pipeline
### Professional Data Engineering Project | Multi-Source ETL • Data Cleaning • Feature Engineering • Analytics-Ready Dataset

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Pandas](https://img.shields.io/badge/Pandas-ETL-success)
![NumPy](https://img.shields.io/badge/NumPy-Data%20Processing-lightgrey)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## Project Overview

This project demonstrates a professional data engineering workflow for **1001-Experiments**, a supplement and health analytics company that combines wearable-device health data, supplement usage, experiment metadata, and user profile information.

The goal is to build a clean, structured, analytics-ready dataset by integrating multiple CSV sources, applying business rules, standardizing inconsistent fields, and preparing reliable outputs for reporting, experimentation, and downstream analysis.

This repository is designed to show recruiters and hiring managers evidence of practical Data Engineering capability using Python, Pandas, and reproducible notebook-based development.

---

## Business Problem

Health and supplement companies often collect data from multiple systems, including wearable devices, application feedback, user profiles, and experiment tracking tools. These datasets are usually fragmented and require transformation before they can support decision-making.

This project solves that problem by creating a repeatable ETL process that combines daily health metrics with supplement usage and experiment information, ensuring the final dataset is clean, consistent, and ready for analysis.

---

## Project Objectives

- Load and inspect multiple raw datasets.
- Standardize supplement dosage values into grams.
- Create meaningful user age groups for segmentation.
- Merge health, supplement, experiment, and profile datasets.
- Apply data quality checks and formatting rules.
- Produce a structured daily-level dataset for analysis.
- Demonstrate production-minded data preparation practices.

---

## Dataset Sources

The workflow is based on four related datasets:

| Dataset | Description |
|---|---|
| `user_health_data.csv` | Daily user health metrics, habits, and wearable-device data |
| `supplement_usage.csv` | Supplement intake records per user and date |
| `experiments.csv` | Experiment and supplement metadata |
| `user_profiles.csv` | User demographic profile information |

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data ingestion, cleaning, joining, and transformation |
| NumPy | Conditional logic and numerical processing |
| Jupyter Notebook | Exploratory and documented development workflow |
| GitHub | Portfolio documentation and version control |

---

## Data Engineering Workflow

```text
Raw CSV Files
     ↓
Data Loading
     ↓
Initial Inspection
     ↓
Data Standardization
     ↓
Feature Engineering
     ↓
Multi-Table Joins
     ↓
Data Quality Validation
     ↓
Analytics-Ready Dataset
```

---

## Key Transformations Implemented

### 1. Data Loading

The notebook loads all required CSV files into Pandas DataFrames and parses date columns to support accurate daily-level joins.

### 2. User Age Grouping

A custom age-grouping function classifies users into business-friendly demographic segments. This supports downstream segmentation and reporting.

### 3. Supplement Dosage Normalization

Supplement dosage values are standardized into grams using conditional logic. This ensures consistent measurement across records where dosage units differ.

### 4. Dataset Integration

The project combines user health data, supplement usage records, experiment metadata, and user profiles into a unified analytical dataset.

### 5. Analytics Preparation

The final structure is designed to support reporting on health outcomes, supplement participation, user demographics, and experiment performance.

---

## Skills Demonstrated

### Data Engineering

- Multi-source data integration
- ETL pipeline development
- Data cleaning and transformation
- Schema interpretation
- Business-rule implementation
- Dataset standardization

### Python Development

- Pandas DataFrame operations
- NumPy conditional logic
- Date parsing
- Function-based transformations
- Reproducible notebook workflow

### Analytics Engineering

- Feature engineering
- User segmentation
- Experiment-ready dataset design
- Clean output preparation for BI and reporting

---

## How to Run the Project

Clone the repository


Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
Supplement_Experiment_Data_Pipeline.ipynb
```

Ensure the following CSV files are available in the working directory before running the notebook:

```text
user_health_data.csv
supplement_usage.csv
experiments.csv
user_profiles.csv
```

---

## Suggested Repository Structure

```text
├── Supplement_Experiment_Data_Pipeline.ipynb
├── README.md
├── schema.png
├── requirements.txt
├── user_health_data.csv
├── supplement_usage.csv
├── experiments.csv
└── user_profiles.csv

```

## Professional Summary

This project reflects the type of real-world data engineering work required in organizations that depend on clean and reliable data pipelines. It demonstrates the ability to transform raw, fragmented operational data into a trusted analytical dataset that supports business intelligence, experimentation, and data-driven decision-making.

---

