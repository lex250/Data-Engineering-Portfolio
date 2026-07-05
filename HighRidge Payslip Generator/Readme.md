
# 🏗️ Highridge Construction Payment Slip Generator

Welcome to the **Highridge Construction Payment Slip Generator** — a lightweight but powerful tool that takes the hassle out of creating employee payment slips. Whether you’re exploring automation with Python or R, this project demonstrates clean, practical code for generating structured payroll data at scale.

---

## 🚀 What It Does

This project automatically generates realistic employee records — complete with names, genders, job titles, and salaries — and assigns levels based on salary and gender criteria. Finally, it exports everything into a neat CSV file that can plug directly into payroll systems.

Perfect for:
✅ Learning data generation and automation techniques
✅ Showcasing how Python and R can handle real-world HR/payroll problems
✅ Anyone curious about scripting practical business workflows

---

## ✨ Key Features

* **Smart Data Generation**: Random but realistic employee data (Labourer, Engineer, Foreman, Electrician, Plumber, Carpenter) with salaries from 5,000 to 35,000.
* **Custom Employee Levels**:

  * Salary 10,000–20,000 → Level `A1`
  * Female employees earning 7,500–30,000 → Level `A5-F`
  * Everyone else → `Not disclosed`
* **CSV Export**: Clean, ready-to-use slips with columns for Employee Name, Gender, Job Title, Salary, and Level.

---

## 🐍 Python Version

### How to Run

1. **Setup**: Install Python 3.x.
2. **Install dependencies**:

   ```bash
   pip install names
   ```

   *(csv and random are built into Python)*
3. **Run the script**:

   ```bash
   python HighridgePaymentSlips.py
   ```

   Adjust the `num_workers` variable to choose how many employees to generate.
4. **Output**:
   Results are saved in `highridge_construction_payment_slips.csv`.

---

## 📊 R Version

### How to Run

1. **Setup**: Install R and RStudio.
2. **Install packages**:

   ```r
   install.packages("randomNames")
   ```
3. **Run the script**:

   ```r
   source("HighridgePaymentSlips.R")
   ```
4. **Output**:
   Results are saved in `highridge_payslip.csv`.

---

## 📂 Files in This Repo

* `HighridgePaymentSlips.py` → Python implementation
* `HighridgePaymentSlips.R` → R implementation
* `README.md` → You’re reading it!

---

## 💡 Why This Project Matters

This isn’t just a random data generator — it’s a **practical showcase of automation, logic-driven classification, and multi-language implementation**. 


---

👉 Want to test how automation can simplify HR tasks? Clone the repo, run the scripts, and watch your payroll data build itself.

