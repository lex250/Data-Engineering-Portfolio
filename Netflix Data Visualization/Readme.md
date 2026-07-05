
---

# 🎬 Netflix Data Visualization Project

## 🌟 Project Overview

This project dives into **Netflix’s vast dataset** to uncover insights about:

* 📊 Which genres dominate viewership
* ⭐ How ratings are distributed across shows and movies

To make the analysis versatile, it’s implemented in **both Python and R**:

* **Python:** Handles data extraction, cleaning, and visualization of both genres and ratings.
* **R:** Focuses on a streamlined visualization of ratings distribution using ggplot2.

---

## 📂 Project Files

* **`netflix_analysis.py`** → Extracts, cleans, and visualizes Netflix data (genres + ratings).
* **`netflix_ratings_distribution.R`** → R-based script for ratings visualization.
* **`netflix_data.zip`** → Compressed raw Netflix dataset.
* **`Netflix_shows_movies.csv`** → Cleaned dataset generated for analysis.

---

## ▶️ Execution Flow

1. **Run `netflix_analysis.py` (Python):** Extract, clean, and prepare the dataset + visualize genres & ratings.
2. **Run `netflix_ratings_distribution.R` (R):** Load the cleaned dataset and generate ratings distribution plots.

---

## ⚙️ Requirements

* **Python 3.x** → Install `pandas`, `seaborn`, `matplotlib`
* **R** → Install `ggplot2`, `dplyr`

---

## 🐍 Python Script Workflow (`netflix_analysis.py`)

1. **Data Prep** → Extracts `netflix_data.csv` from the ZIP and renames it to `Netflix_shows_movies.csv`.
2. **Data Cleaning** → Fills missing values (director, cast, country, rating, date\_added).
3. **Exploration** → Generates descriptive stats to understand the dataset.
4. **Visualization** → Creates insightful plots (most watched genres + ratings distribution).

---

## 📊 R Script Workflow (`netflix_ratings_distribution.R`)

1. **Load Data** → Reads in `Netflix_shows_movies.csv`.
2. **Data Cleaning** → Handles missing values in key fields.
3. **Visualization** → Builds clear, engaging ratings distribution charts with ggplot2.

---

## 📝 Notes

* Keep all files (`netflix_analysis.py`, `netflix_ratings_distribution.R`, `netflix_data.zip`, `Netflix_shows_movies.csv`) in the **same directory** before running.
* The Python script **generates the cleaned CSV**, which is then used as input for the R script.

---

✨ This project demonstrates **data wrangling, visualization, and cross-language analytics** — skills that directly translate into real-world business intelligence and data science roles.

---

