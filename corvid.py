import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st

# ----------------------
# Load data, from the downloaded metadata from kaggle
# ----------------------
df = pd.read_csv("metadata.csv")

st.title("CORD-19 Data Explorer")
st.write("📊 Interactive exploration of COVID-19 research metadata")

# ----------------------
# Data Cleaning
# ----------------------
df_clean = df.dropna(subset=['title', 'abstract', 'publish_time'])
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
df_clean['year'] = df_clean['publish_time'].dt.year
df_clean['abstract_word_count'] = df_clean['abstract'].astype(str).str.split().str.len()

# ----------------------
# Sidebar Filters
# ----------------------
st.sidebar.header("Filters")
years = st.sidebar.slider(
    "Select years",
    min_value=int(df_clean['year'].min()),
    max_value=int(df_clean['year'].max()),
    value=(2020, 2021)
)

filtered_df = df_clean[(df_clean['year'] >= years[0]) & (df_clean['year'] <= years[1])]

# ----------------------
# Visualizations
# ----------------------

# 1. Publications by Year
st.subheader("Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
ax1.bar(year_counts.index, year_counts.values, color="skyblue")
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Publications")
st.pyplot(fig1)

# 2. Top Journals
st.subheader("Top 10 Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
top_journals.plot(kind='bar', ax=ax2, color="orange")
ax2.set_ylabel("Count")
st.pyplot(fig2)

# 3. Word Cloud
st.subheader("Word Cloud of Titles")
title_text = " ".join(filtered_df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(title_text)
fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.imshow(wordcloud, interpolation="bilinear")
ax3.axis("off")
st.pyplot(fig3)

# ----------------------
# Data Sample
# ----------------------
st.subheader("Sample Data")
st.dataframe(filtered_df[['title', 'journal', 'year']].head(20))
