# Movie-Recommendation-System

## Project Description ⬇️
<p>
  The Movie Recommender System is a Streamlit-based application designed to help users discover movies they might enjoy.<br>
  By selecting a movie, the system provides personalized recommendations based on similarity, along with the following features:<br>
  
   * <strong>Recommendations:</strong> Displays a list of suggested movies.
   * <strong>Movie Posters:</strong> Shows the posters for a visual preview.
   * <strong>Ratings and Overviews:</strong> Includes average ratings and a short description of each movie.
   * <strong>Trailers:</strong> Provides links to YouTube trailers for easy access.
   * <strong>User Interface:</strong> Features a clean and interactive design, enhancing the user experience.
    
</p>

## How it Works

  1. Select a movie from the dropdown.
  2. Click the "Recommend" button.
  3. View a list of similar movies, along with their:

        * Posters
        * Ratings
        * Overviews
        * Links to YouTube trailers

## Technologies Used⬇️

  1. **Python:** Core programming language.
  2. **Streamlit:** Framework for building the web app.
  3. **TMDb API:** Fetches movie details like posters, ratings, and trailers.
  4. **Machine Learning:** Recommendation logic based on movie similarity.
  5. **Pandas:** For handling movie data.
  6. **Pickle:** For saving preprocessed data (not included in this repository).

## Prerequisites⬇️

 1. Install Python (version 3.7 or later).
 2. Install required Python libraries:

         pip install streamlit pandas requests

## Setup⬇️

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

## API Integration⬇️

   The app uses the [TMDb API](https://developer.themoviedb.org/reference/intro/getting-started) to fetch movie details. Replace the API key in the code (`api_key`) with your own TMDb API key.

## Project Structure⬇️

    Movie-Recommender-System/
    │
    ├── app.py                # Main Streamlit application
    ├── README.md             # Project documentation
    └── requirements.txt      # Dependencies


## Screenshot

<img width="714" height="380" alt="Image" src="https://github.com/user-attachments/assets/1efb744a-86d7-418e-a517-587c3fe99912" />


## Contributions ⬇️
<p>Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests.<br>
    Together, let's make this recommendation system even more powerful and versatile.</p>

## License ⬇️
This project is licensed under the [MIT License](https://github.com/Faisal-khann/Movie-Recommendation-System?tab=MIT-1-ov-file)
2025 Faisal Khan
<p>If you like this project don’t forget to 🌟(star) the repository and Clone this repository.</p>
