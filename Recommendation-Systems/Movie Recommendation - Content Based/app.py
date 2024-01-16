import pickle
import streamlit as st
import requests
import pandas as pd

# for the catch posters from themoviedb.org
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=3234f17f00c026424d5b6ed71134102c&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarty[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

st.header('Movie Recommendation System - Content Based')
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarty = pickle.load(open('artifacts/similarty.pkl', 'rb'))

movie_list = movies['title'].values
movie_select = st.selectbox(
                            'Select Movie',
                            movie_list
)

if st.button('Show Recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(movie_select)
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])
    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])
    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])
    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])
    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])
    with col6:
        st.text(recommended_movies_name[5])
        st.image(recommended_movies_poster[5])
    with col7:
        st.text(recommended_movies_name[6])
        st.image(recommended_movies_poster[6])
    with col8:
        st.text(recommended_movies_name[7])
        st.image(recommended_movies_poster[7])
    with col9:
        st.text(recommended_movies_name[8])
        st.image(recommended_movies_poster[8])
    with col10:
        st.text(recommended_movies_name[9])
        st.image(recommended_movies_poster[9])