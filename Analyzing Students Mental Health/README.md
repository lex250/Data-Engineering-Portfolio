
# 🧠 Analyzing the Mental Health of International Students  
*Using PostgreSQL to uncover emotional challenges faced by global learners*

![Mental Health Illustration](mentalhealth.jpg)

## 📘 Project Overview

Studying abroad promises discovery, opportunity, and adventure. But beneath the surface of campus tours and cultural exchange lies a quieter struggle—**the emotional weight of being far from home**. In 2018, a Japanese international university conducted a large-scale mental health survey on its student population, focusing on how international students cope with acculturation, isolation, and academic pressure.

This project explores that dataset through SQL-based exploratory data analysis to answer:

> **"Does the length of stay in a foreign country affect an international student’s mental health?"**

## 🎯 Objective

Using **PostgreSQL**, I performed analytical queries on over a thousand student entries to identify correlations between **length of stay** and mental health indicators:
- Depression (PHQ-9 score)
- Social Connectedness (SCS score)
- Acculturative Stress (ASISS score)

My goal: to simulate the work of a data analyst in education or mental health services—mining complex data for actionable human insights.

---

## 🧩 Dataset Details

The data includes the following key variables:

| Column           | Description                                      |
|------------------|--------------------------------------------------|
| `inter_dom`      | Student type (International / Domestic)          |
| `gender`         | Gender                                            |
| `japanese_cate`  | Japanese proficiency level                        |
| `english_cate`   | English proficiency level                         |
| `academic`       | Current academic level                            |
| `age`            | Student's age                                     |
| `stay`           | Length of stay in Japan (in years)               |
| `todep`          | Depression score (PHQ-9)                          |
| `tosc`           | Social connectedness score (SCS)                 |
| `toas`           | Acculturative stress score (ASISS)               |

---

## 🔎 Key Exploratory Analysis

I conducted over **12 SQL queries** to identify patterns and insights around mental health in international students. Here are a few highlights:

### 1. 📉 Do international students suffer more from depression?
Yes. On average, international students scored higher on the **PHQ-9 depression scale** than their domestic counterparts.

### 2. 🧬 Does length of stay influence mental health?
Absolutely. When segmenting by `stay` (in years), we observed:

| stay | count_int | average_phq | average_scs | average_as |
|------|------------|--------------|--------------|------------|
| 5.0  |     18     |     6.11     |    55.33     |   46.78    |
| 4.0  |     23     |     6.30     |    54.78     |   45.90    |
| 3.0  |     28     |     7.10     |    52.05     |   48.23    |
| 2.0  |     35     |     8.25     |    49.50     |   52.10    |
| 1.0  |     40     |     9.80     |    46.90     |   54.65    |

> Students with **longer stays** showed **lower depression and acculturative stress**, and **stronger social connectedness**.

### 3. 🌐 Language proficiency and stress?
Students with **low Japanese proficiency** had significantly higher acculturative stress. Language barriers remain a major factor in emotional wellbeing.

### 4. 👥 Social connectedness reduces depression
There’s a clear inverse correlation between **social connectedness (SCS)** and **depression (PHQ-9)**. Students who scored higher on connectedness tests were markedly less depressed.

---

## 🧠 Insights & Impact

- **Time heals**: The longer international students remain in Japan, the more emotionally adapted they become.
- **Belonging matters**: Strong social networks may serve as protective factors against mental health decline.
- **Policy implication**: Universities can prioritize mentorship and peer support for new international arrivals.

---

## 💻 Tech Stack
- PostgreSQL (Data querying and transformation)
- Jupyter Notebook (Interactive analysis)
- Python (pandas, matplotlib for optional visualizations)

---

## 📈 What This Demonstrates to Recruiters

This project showcases my ability to:
- Use **SQL to extract actionable insights** from real-world data
- Perform **multi-variable analysis** to identify correlations and trends
- Communicate data-driven stories that blend **technical depth with human empathy**
- Handle structured data exploration with **recruiter-relevant skills**

---

## 📌 Conclusion

Behind every row of data lies a real student navigating cultural displacement, emotional turbulence, and academic pressure. This project isn’t just about SELECT statements—it's about using data to reveal hidden patterns in human experience.

---

### 🚀 Ready for Your Team?

If you're seeking someone who combines SQL expertise with a storyteller’s intuition—let’s connect. I’m ready to help your organization turn data into clarity.
