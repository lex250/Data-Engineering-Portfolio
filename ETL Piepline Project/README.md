# 🧠 Data Engineering ETL Pipeline — Multi-Source Data Integration

> **Date:** November 2025  

---

## 📘 Overview

This project demonstrates a **data engineering ETL (Extract, Transform, Load)** pipeline built in **Python**, integrating data from **multiple heterogeneous sources** — a structured CSV file and a public API — into a **unified, analytics-ready dataset**.

The project showcases real-world data engineering techniques such as:
- Data ingestion from both flat files and web APIs  
- Data cleaning and transformation  
- Merging multi-source datasets  
- Structured data export (CSV, JSON)  
- Exploratory data analysis and visualization  

---

## 🏗️ Project Architecture

```text
                  +-----------------------+
                  |   Source 1: CSV File  |
                  |  all_countries.csv    |
                  +-----------+-----------+
                              |
                              v
                  +-----------------------+
                  |   Source 2: API Data  |
                  |  (e.g., RestCount.)   |
                  +-----------+-----------+
                              |
                              v
        +------------------------------------------------+
        |                ETL Pipeline                    |
        |------------------------------------------------|
        |  Extract → Transform → Merge → Load → Analyze   |
        +------------------------------------------------+
                              |
                              v
              +-------------------------------+
              |   Output: CSV, JSON, Insights  |
              +-------------------------------+
```

---

## ⚙️ Technologies Used

| Category | Tools / Libraries |
|-----------|------------------|
| **Language** | Python 3 |
| **Data Processing** | pandas, numpy |
| **API Handling** | requests, json |
| **Visualization** | matplotlib, seaborn |
| **Storage Formats** | CSV, JSON |
| **Environment** | Jupyter Notebook / Python Script |

---

## 📂 Data Sources

### 1️⃣ **CSV File**
- **File:** `all_countries.csv`
- **Content:** Country-level data such as name, population, GDP, and area.

### 2️⃣ **Public API**
- **Source:** [RestCountries API](https://restcountries.com/v3.1/all)  

---

## 🧩 ETL Pipeline Stages

| Stage | Function | Description |
|--------|-----------|-------------|
| **Extract** | `extract_data()` | Reads data from CSV and API endpoints. Saves raw API data as JSON. |
| **Transform** | `transform_data()` | Cleans column names, handles missing values, and standardizes schema. |
| **Merge** | `merge_data()` | Joins both datasets on a common key (e.g., ISO3 code or country name). |
| **Load** | `load_data()` | Exports the unified dataset to structured formats (.csv, .json). |
| **Analyze (Bonus)** | — | Performs exploratory data analysis and visualization. |

---

## 📊 Sample Outputs

| File | Description |
|------|--------------|
| `extracted_api_data.json` | Extracted data from API before transformation |
| `transformed_api.csv` | Transformed JSON API to csv dataset |
| `merged_countries.csv` | Transformed and validated final dataset |

---

## 🔍 Exploratory Data Analysis (Bonus Section)

### 1. **Total Population by Region**
Visualizes global population distribution by region using a horizontal bar chart.

```python
plt.barh(pop_by_region.index, pop_by_region.values)
plt.title("Total Population by Region")
```

### 2. **Area vs Population (Log–Log Scatter Plot)**
Explores the relationship between country area and population.

```python
plt.scatter(df["area"], df["population"])
plt.xscale("log"); plt.yscale("log")
plt.title("Country Area vs Population (log–log)")
```

### 📈 Key Insights
- Asia and Africa dominate global population totals.  
- High-population countries tend to cluster within medium landmass regions.  
- The merged dataset provides a reliable foundation for population density analysis.

---

## 🚀 How to Run the Project

### 🧩 Prerequisites
Make sure you have:
- Python 3.9+  
- Jupyter Notebook (optional, for visualization)  
- Internet access for API extraction

### 🧰 Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/lex250/Data-Engineering-Portfolio/tree/main/ETL%20Piepline%20Project
cd ETL-DataEngineering-Project
pip install -r requirements.txt
```

### ▶️ Run the Notebook
```bash
jupyter notebook ETL_Project_Notebook.ipynb
```

Or run as a script:
```bash
python etl_pipeline.py
```

## 🧠 Lessons Demonstrated

- Building scalable ETL functions  
- Data standardization and schema alignment  
- Handling multi-source data quality issues  
- Using visualizations to validate merged datasets  
- Following software engineering best practices (versioning, modularity, documentation)

---

## 🧾 Repository Structure

```text
ETL-DataEngineering-Project/
│
├── all_countries.csv              # Input dataset
├── ETL_Project_Notebook.ipynb     # Main Jupyter notebook
├── transformed_api.csv            # Transformed Merged dataset
├── merged_countries.csv           # Final Cleaned Merged dataset
├── README.md                      # Project documentation
└── requirements.txt               # Dependencies
```

---


