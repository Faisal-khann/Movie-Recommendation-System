import pandas as pd
import streamlit as st
import pickle
import requests
from PIL import Image

# Function to fetch the poster, rating, and overview of a movie
def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=21931a6a1dd7579e0f292e7b6c07bd56&language=en-US"
    response = requests.get(url)
    data = response.json()
    poster_path = f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    rating = data['vote_average']
    overview = data['overview']
    return poster_path, rating, overview

# Function to fetch the YouTube trailer URL of a movie
def fetch_trailer(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key=21931a6a1dd7579e0f292e7b6c07bd56&language=en-US"
    response = requests.get(url)
    data = response.json()
    for video in data.get('results', []):
        if video['site'] == 'YouTube' and video['type'] == 'Trailer':
            return f"https://www.youtube.com/watch?v={video['key']}"
    return None

# Function to recommend movies based on similarity
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_ratings = []
    recommended_movies_trailers = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        poster_path, rating, _ = fetch_movie_details(movie_id)  # Add `_` to discard the `overview`
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(poster_path)
        recommended_movies_ratings.append(f"{rating:.2f}")  # Format rating to 2 decimal places
        recommended_movies_trailers.append(fetch_trailer(movie_id))
    
    return (recommended_movies, 
            recommended_movies_posters, 
            recommended_movies_ratings, 
            recommended_movies_trailers)


# Load the movies data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Initialize Streamlit session state for watchlist
if "watchlist" not in st.session_state:
    st.session_state.watchlist = []


# Streamlit app setup
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" integrity="sha512-Fo3rlrj/k7ujTTXJNf1MqL0Y0HL8d49O5+U1fnXCCr8sUovDzmUwJaT/nkTyUM2Fu4Ikm9T9n2zpO5ozhDgUQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
    body {
        background-color: #2c2c2c;
        color: #f5f5f5;
        font-family: 'Roboto', sans-serif;
    }
    .stButton>button {
    background: linear-gradient(to right, #2196f3, #21cbf3);
    color: #f5f5f5;
    font-weight: 600;
    font-family: 'Roboto', sans-serif;
    border-radius: 12px;
    padding: 10px 20px;
    border: none;
    transition: all 0.3s ease;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
}
.stButton>button:hover {
    background: linear-gradient(to right, #1976d2, #1e88e5);
    color: #ffffff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

    .movie-container {
        background-color: #333;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        text-align: center;
        max-width: 200px;
        margin: 20px;
    }
    .movie-title {
        font-size: 16px;
        font-weight: bold;
        color: #e0e0e0;
        margin-top: 10px;
    }
    .movie-rating {
        font-size: 14px;
        color: #b0b0b0;
        margin-top: 5px;
    }
    img {
        border-radius: 10px;
    }
    .trailer-button{
        background-color: #ffffff;
        color: #000000;
        border: 2px solid #000000;
        border-radius: 25px;
        font-weight: bold;
        padding: 5px 10px;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    .trailer-button:hover{
        background-color: #1976d2;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="font-size: 36px; color: #f5f5f5;">Movie Recommender System</h1>
        <h2 style="font-size: 24px; color: #f5f5f5;">Discover Your Next Favorite Movie!</h2>
        <p style="color: #b0b0b0;">Select a movie and we’ll show you some fantastic recommendations along with posters, ratings, and trailers. Get ready for your next movie marathon!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("Movie Recommender System")
img = Image.open('cinema.png')
st.sidebar.image(img)

# Sidebar: About the App
# -------------- Sidebar Start --------------
with st.sidebar:

    with st.expander("About"):
        st.markdown("""
        This Movie Recommender System suggests movies based on your selected favorite.
        
        - Built using Python, Streamlit, and ML
        - Fetches posters, overviews, ratings, and trailers
        """)

    with st.expander("How to Use"):
        st.markdown("""
        1. Select a movie from the dropdown  
        2. Click 'Recommend'  
        3. Get top similar movie suggestions with posters, ratings and trailers
        """)

    with st.expander("Contact"):
        st.markdown("""
        👨‍💻 **Faisal Khan**  
        📧 [Email Me](mailto:faisalkhan.datasci@gmail.com)  
        💼 [LinkedIn](https://www.linkedin.com/in/faisal-khan-332b882bb)  
        🐙 [GitHub](https://github.com/Faisal-khann)
        """)

    st.markdown("---")


# Select box for user input
selected_movie_name = st.selectbox("What are you looking for today?", movies['title'].values)

# Recommend movies when the button is clicked
if st.button('Recommend'):
    (names, posters, ratings, trailers) = recommend(selected_movie_name)
    st.subheader("Recommended Movies for You:")

    # Display movies in rows of 3 columns
    for i in range(0, len(names), 3):
        cols = st.columns(3)
        for col, name, poster, rating, trailer in zip(cols, names[i:i+3], posters[i:i+3], ratings[i:i+3], trailers[i:i+3]):
            with col:
                st.markdown(
                    f"""
                    <div class="movie-container">
                        <img src="{poster}" alt="{name}" style="width:100%; height:auto;">
                        <div class="movie-title">{name}</div>
                        <div class="movie-rating">Rating: {rating}/10</div>
                        <div style="margin-top: 10px;">
                            <a href="{trailer}" target="_blank" style="text-decoration: none;">
                                <button class="trailer-button">
                                    🎥 Watch Trailer
                                </button>
                            </a>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

# Footer
st.markdown("""<hr style="margin-top: 50px;"/>""", unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align: center; padding: 10px; font-size: 14px;">
        Made with <span style="color: #e25555;">❤️</span> by <strong>Faisal Khan</strong>
    </div>
    """,
    unsafe_allow_html=True
)


