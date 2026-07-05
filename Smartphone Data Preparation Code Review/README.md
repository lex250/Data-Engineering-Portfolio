# Smartphone Data Preparation & Code Review

> A production-focused Python data engineering project demonstrating code review, data cleaning, testing, visualization, and software engineering best practices.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green)
![Pytest](https://img.shields.io/badge/Pytest-Tested-success)
![PEP8](https://img.shields.io/badge/PEP--8-Compliant-blueviolet)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## Project Overview

This project demonstrates how software engineering principles can be applied within a practical data engineering workflow.

The original notebook contained issues affecting readability, maintainability, testing reliability, and code quality. Acting as a Senior Data Engineer performing a production code review, I refactored the implementation to improve documentation, enforce coding standards, eliminate duplicated logic, and ensure automated tests passed successfully.

The final solution is a clean, testable, and maintainable data preparation workflow suitable for analytics and visualization.

---

## Business Scenario

A university procurement department needs insights into smartphone specifications before selecting devices for employees.

The workflow focuses on:

- ingesting raw smartphone CSV data
- cleaning and preparing records for analysis
- validating key data quality requirements
- supporting exploratory visualization
- improving code quality for production readiness

---

## Objectives

- Review existing Python code for readability and maintainability
- Improve documentation and inline comments
- Refactor code according to PEP 8 standards
- Remove duplicated logic using reusable helper functions
- Validate transformation logic with unit tests
- Produce a cleaned dataset ready for visualization

---

## Dataset

The project expects a smartphone CSV dataset containing fields such as:

- `brand_name`
- `os`
- `price`
- `avg_rating`
- `processor_speed`
- `battery_capacity`
- `screen_size`

Expected local path:

```text
data/smartphones.csv
```

The dataset file is not included in this package unless you add it manually.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Pytest
- iPytest
- Jupyter Notebook

---

## Key Engineering Improvements

### 1. Code Review and Readability

The project improves variable naming, spacing, docstrings, comments, and overall code structure to make the workflow easier to understand and maintain.

### 2. PEP 8 Compliance

The reviewed solution follows common Python style standards including:

- descriptive snake_case variable names
- consistent indentation
- proper whitespace
- clear function boundaries
- readable docstrings
- safer DataFrame assignment using `.loc`

### 3. Data Cleaning Pipeline

The `prepare_smartphone_data()` function performs the following transformations:

- reads raw CSV data
- keeps only required analysis columns
- removes rows missing `battery_capacity` or `os`
- converts `price` from cents to dollars
- returns a cleaned pandas DataFrame

### 4. DRY Refactoring

Duplicated label-formatting logic was removed from the visualization function by reusing:

```python
column_to_label()
```

This improves maintainability and makes the plotting workflow easier to extend.

### 5. Automated Testing

The notebook includes a unit test using `pytest` and `ipytest` to confirm that cleaned data contains no missing values in critical fields.

Expected successful result:

```text
test_nan_values PASSED [100%]
ExitCode.OK
```

---

## Project Structure

```text

├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── notebooks/
│   └── code_review.ipynb
│
├── data/
│   └── smartphones.csv              # Add dataset here
│
└── assets/
    └── screenshots/                 # Optional charts/images for README
```

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/lex250/Smartphone-Data-Preparation-Code-Review
cd smartphone-code-review-project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the dataset

Place the dataset at:

```text
data/smartphones.csv
```

### 5. Open the notebook

```bash
jupyter notebook notebooks/code_review.ipynb
```

Run all cells from top to bottom.

---

## Testing

The notebook uses `ipytest` to run unit tests directly inside Jupyter.

Recommended test command inside the notebook:

```python
ipytest.run("-v")
```

Expected output:

```text
test_nan_values PASSED [100%]
```

---

## Data Engineering Skills Demonstrated

- Python programming
- Data ingestion
- Data cleaning
- Data validation
- ETL transformation
- Unit testing
- Code review
- PEP 8 compliance
- DRY principle refactoring
- Documentation
- Error handling
- Reusable function design
- Visualization support
- Production-readiness mindset

---

## Focused Highlights

This project demonstrates more than notebook-based analysis. It shows practical engineering habits that are valuable in a production data team:

- writing maintainable Python code
- reviewing and improving existing code
- validating data quality with tests
- preparing clean datasets for downstream analytics
- using reusable functions instead of duplicated logic
- documenting work clearly for team collaboration

These are core skills expected from a data engineer working with analytics, reporting, and pipeline reliability.

---

