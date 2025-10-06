# Movie Recommendation System

<em>The **Movie Recommendation System** is a **Streamlit-based web application** that helps users discover movies they might enjoy.  
It uses **content-based filtering** powered by machine learning to recommend movies similar to a user’s selection.</em>
  
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
- [How to Run This Project](#how-to-run-this-project)
- [License](#license)

---

## Overview

The **Movie Recommendation System** is a **Streamlit-based web application** designed to help users discover movies they might enjoy.
It uses **content-based filtering** powered by machine learning to recommend movies similar to a user’s selection.<br>
  
  <em>Utilized **TF-IDF Vectorization** and **cosine similarity** to match movie metadata for similarity scoring.</em><br>
  <em>Deployed as a web application using Streamlit for interactive user experience.</em>

**✨ Key Features**
- Personalized movie recommendations  
- Movie posters for a visual preview  
- Ratings and overviews  
- Direct YouTube trailer links  
- Clean, interactive Streamlit interface  

---

## Project Workflow
1. Load preprocessed movie metadata (`movie_dict.pkl`) and similarity matrix (`similarity.pkl`).
2. User selects a movie from the dropdown.
3. The system calculates the top 5 most similar movies.
4. Fetch movie posters, ratings, and overviews using **TMDb API**.
5. Display results in a visually appealing interface.

---

## Business Problem
With thousands of movies released every year, users face **information overload** and often struggle to pick what to watch next.  
This project solves that by providing **personalized movie suggestions** based on similarity, enhancing **user experience**, and boosting **content discovery**.

---

## Ingestion Script

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

```
## Tools & Technologies

  | Tool             | Purpose                                |
| ---------------- | -------------------------------------- |
| **Python**       | Core programming language              |
| **Streamlit**    | Web app development                    |
| **TMDb API**     | Fetches posters, ratings, and trailers |
| **Pandas**       | Data manipulation                      |
| **Pickle**       | Data serialization                     |
| **Scikit-learn** | Similarity computation                 |

## Project Structure
    Movie-Recommender-System/
    │
    ├── app.py                # Main Streamlit app
    ├── movie_dict.pkl        # Movie metadata file
    ├── similarity.pkl        # Precomputed similarity matrix
    ├── requirements.txt      # Python dependencies
    └── README.md             # Project documentation

## Data Pipeline Overview

| Step | Description |
|------|--------------|
| **1. Data Collection** | Gather movie metadata such as titles, genres, keywords, and overviews. |
| **2. Data Preprocessing** | Clean and merge textual columns (overview, genres, keywords, etc.) to create a single feature column. |
| **3. Feature Extraction** | Convert combined text data into numerical vectors using `CountVectorizer`. |
| **4. Similarity Calculation** | Compute cosine similarity between movie vectors to identify similar movies. |
| **5. Deployment** | Integrate the model with Streamlit UI and TMDb API for real-time movie recommendations. |

## Dashboard Preview
<p align="center"> <img width="714" height="380" src="https://github.com/user-attachments/assets/1efb744a-86d7-418e-a517-587c3fe99912" alt="App Screenshot"> </p>


## Key Outcomes

|  Outcome | Description |
|------------|-------------|
| **End-to-End Web App** | Developed a complete movie recommendation system from data preprocessing to deployment. |
| **TMDb API Integration** | Integrated the TMDb API to fetch real-time movie posters, ratings, and trailers. |
| **Cosine Similarity Model** | Implemented content-based filtering using cosine similarity for accurate recommendations. |
| **Interactive Streamlit UI** | Designed a user-friendly interface with dynamic elements for enhanced user experience. |

## How to Run This Project
<div>
<strong><em>Prerequisites⬇️</em></strong>

 1. Install Python (version 3.7 or later).
 2. Install required Python libraries:

         pip install streamlit pandas requests

<strong><em>Setup⬇️</em></strong>

 1. Prepare Data:
    Since `movie_dict.pkl` and `similarity.pkl` are not provided, you need to generate them:

       * The `movie_dict.pkl` file should contain movie metadata (e.g., movie IDs, titles, etc.).
       * The `similarity.pkl` file should be a precomputed similarity matrix.
       * Use your dataset and appropriate Python libraries to create these files.
2. Clone the Repository:
   
       git clone https://github.com/your-username/Movie-Recommender-System.git
       cd Movie-Recommender-System
   
4. Add the Required Files:
    Place the generated `movie_dict.pkl` and `similarity.pkl` files in the project directory.
   
5. Run the Application:
   
        streamlit run app.py

<strong><em>API Integration⬇️</em></strong>

The app uses the [TMDb API](https://developer.themoviedb.org/reference/intro/getting-started) for fetching movie details.
Replace your TMDb API key inside the code:
`
      
      `api_key = "YOUR_TMDB_API_KEY"


</div>

## Contributions
<p>Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests.<br>
    Together, let's make this recommendation system even more powerful and versatile.</p>

## License
This project is licensed under the [MIT License](https://github.com/Faisal-khann/Movie-Recommendation-System?tab=MIT-1-ov-file)
2025 Faisal Khan
<p>If you like this project don’t forget to 🌟(star) the repository and Clone this repository.</p>
