import streamlit as st
import os
from dotenv import load_dotenv
import pickle
import requests

# Load API key from .env
load_dotenv()
omdb_api_key = os.getenv("OMDB_API_KEY")

def fetch_poster_from_omdb(movie_title):
    try:
        url = f"http://www.omdbapi.com/?t={movie_title}&apikey=6d2a26d0"
        response = requests.get(url)
        data = response.json()

        poster_url = data.get("Poster")
        if poster_url and poster_url != "N/A":
            return poster_url
        else:
            return "https://via.placeholder.com/300x450?text=No+Poster"
    except Exception as e:
        print(f"OMDb error: {e}")
        return "https://via.placeholder.com/300x450?text=Error"

# Load precomputed data
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# UI setup
st.set_page_config(page_title="Movie Recommendation System", layout="wide", page_icon="🎬")
st.title("🎥 Movie Recommendation system")
selected_movie = st.selectbox("Select a movie:", movies_list)

# Recommendation logic (unchanged)
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])

    recommend_movie = []
    recommend_poster = []

    for i in distance[1:6]:
        movie_title = movies.iloc[i[0]].title
        recommend_movie.append(movie_title)
        recommend_poster.append(fetch_poster_from_omdb(movie_title))
    return recommend_movie, recommend_poster

# Show recommendations
if st.button("Show Recommendations"):
    movie_name, movie_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])


