'''
Author: Najma Bibi
Email: najmabibi@gmail.com
Date: 2024-July-10
'''

import pickle
import streamlit as st
import requests

# Function to fetch the movie poster from the TMDB API
def get_movie_poster(movie_id):
    api_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(api_url)
    movie_data = response.json()
    poster_path = movie_data['poster_path']
    full_poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_poster_url

# Function to get movie recommendations based on the selected movie
def get_recommendations(selected_movie):
    # Find the index of the selected movie
    movie_index = movies_df[movies_df['title'] == selected_movie].index[0]
    # Calculate similarity scores
    similarity_scores = sorted(list(enumerate(similarity_matrix[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movie_titles = []
    recommended_movie_posters = []
    # Get the top 5 similar movies
    for score in similarity_scores[1:6]:
        similar_movie_id = movies_df.iloc[score[0]].movie_id
        recommended_movie_posters.append(get_movie_poster(similar_movie_id))
        recommended_movie_titles.append(movies_df.iloc[score[0]].title)
    return recommended_movie_titles, recommended_movie_posters

# Load the movies data and similarity matrix
movies_df = pickle.load(open('savedModel/movie_list.pkl', 'rb'))
similarity_matrix = pickle.load(open('savedModel/similarity.pkl', 'rb'))

# CSS for styled header
st.markdown(
    """
    <style>
    .header-box {
        border: 2px solid #4CAF50;
        padding: 10px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Styled header
st.markdown('<div class="header-box"><h1>RECOMMENDATION SYSTEM</h1></div>', unsafe_allow_html=True)

# Dropdown to select a movie
movie_list = movies_df['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Button to show recommendations
if st.button('Show Recommendation'):
    # Get recommendations
    recommended_movie_titles, recommended_movie_posters = get_recommendations(selected_movie)
    # Display the recommendations in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_titles[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_titles[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_titles[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_titles[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_titles[4])
        st.image(recommended_movie_posters[4])
