# 🎬 Movie Recommendation System

## 📌 Table of Contents
- [Overview](#overview)
- [Project Workflow](#project-workflow)
- [Business Problem](#business-problem)
- [Ingestion Script](#ingestion-script)
- [Tools & Technologies](#tools--technologies)
- [Project Structure](#project-structure)
- [Data Pipeline Overview](#data-pipeline-overview)
- [Dashboard Preview](#dashboard-preview)
- [Key Outcomes](#key-outcomes)
- [Business Insights](#business-insights)
- [How to Run This Project](#how-to-run-this-project)
- [Author & Contact](#author--contact)
- [License](#license)

---

## 🧩 Overview
The **Movie Recommendation System** is a **Streamlit-based web application** that helps users discover movies they might enjoy.  
It uses **content-based filtering** powered by machine learning to recommend movies similar to a user’s selection.

**✨ Key Features**
- 🎞️ Personalized movie recommendations  
- 🖼️ Movie posters for a visual preview  
- ⭐ Ratings and overviews  
- ▶️ Direct YouTube trailer links  
- 💡 Clean, interactive Streamlit interface  

---

## ⚙️ Project Workflow
1. Load preprocessed movie metadata (`movie_dict.pkl`) and similarity matrix (`similarity.pkl`).
2. User selects a movie from the dropdown.
3. The system calculates the top 5 most similar movies.
4. Fetch movie posters, ratings, and overviews using **TMDb API**.
5. Display results in a visually appealing interface.

---

## 💼 Business Problem
With thousands of movies released every year, users face **information overload** and often struggle to pick what to watch next.  
This project solves that by providing **personalized movie suggestions** based on similarity, enhancing **user experience**, and boosting **content discovery**.

---

## 📥 Ingestion Script

Here’s a simple example to generate your own `movie_dict.pkl` and `similarity.pkl` files using a movie dataset:

```python
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load your dataset
movies = pd.read_csv("movies.csv")

# Combine textual features into a single 'tags' column
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords']

# Convert text data to feature vectors
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Compute similarity
similarity = cosine_similarity(vectors)

# Save the data
pickle.dump(movies.to_dict(), open('movie_dict.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

---
