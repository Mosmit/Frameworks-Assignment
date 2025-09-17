# Frameworks-Assignment

# python-plp-corvid

# 📊 CORD-19 Data Explorer

This project is a simple data analysis and visualization tool built with **Streamlit** to explore the **CORD-19 research dataset**. It focuses on COVID-19 research publications using the `metadata.csv` file provided by the [CORD-19 Kaggle Challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).

---

## 🚀 Project Overview

The application demonstrates fundamental data science steps:

1. **Loading and exploring data**
2. **Cleaning and preparing data**
3. **Performing simple analysis**
4. **Creating meaningful visualizations**
5. **Building an interactive Streamlit app**

This simplified workflow is ideal for beginners learning how to handle real-world datasets.

---

## 🧾 Features

- Load and clean metadata from COVID-19 research papers  
- Handle missing values and extract publication years  
- Create a new feature: **abstract word count**  
- Interactive filters (year slider in the sidebar)  
- Visualizations:
  - Publications by year (bar chart)  
  - Top 10 publishing journals (bar chart)  
  - Word cloud of research paper titles  
- Display of sample research paper data  

---

## 📂 Project Structure

```text
Frameworks_Assignment/
│
├── metadata.csv        # Dataset file (downloaded from Kaggle)
├── corvid.py           # Main Streamlit application
├── README.md           # Project documentation (this file)

```

## ⚙️ Installation
1. Clone this repository
git clone https://github.com/<your-username>/Frameworks_Assignment.git
cd Frameworks_Assignment

2. Create and activate a virtual environment
python -m venv corvid
source corvid/bin/activate   # macOS/Linux
corvid\Scripts\activate      # Windows (PowerShell)

3. Install dependencies
pip install pandas matplotlib seaborn streamlit wordcloud

## ▶️ Usage

Place the metadata.csv file in the project directory.

Run the Streamlit app:

streamlit run corvid.py


Open your browser at http://localhost:8501
 to explore the app.

## 📊 Visualizations Included

Publications by Year – Bar chart showing trends in COVID-19 publications.

Top 10 Journals – Bar chart of journals with the most publications.

Word Cloud of Titles – Highlights frequent words in research paper titles.

Sample Data – Displays a table of titles, journals, and publication years.

## 📘 Learning Objectives

By completing this project, I practiced:

Loading and cleaning real-world datasets with Pandas

Creating new features (e.g., abstract word count)

Visualizing data with Matplotlib and WordCloud

Building an interactive dashboard with Streamlit

Documenting and presenting results clearly

## 📝 Reflection

**Challenges:**

Handling missing data and ensuring clean parsing of dates.

Managing large datasets — the metadata file is big, so focusing on a subset is useful.

**Key Learnings:**

Streamlit makes it easy to turn Python scripts into interactive apps.

Basic cleaning and simple plots can already provide valuable insights.

Organizing code and documenting steps improves clarity and reproducibility.

## 📌 Requirements

Python 3.7+

pandas

matplotlib

seaborn

streamlit

wordcloud
