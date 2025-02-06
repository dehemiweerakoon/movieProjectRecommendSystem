import pickle
import  streamlit as st
import  requests
 # added
from Key import getKey

movies = pickle.load(open('artifacts/movie_list.pickle','rb'))
simulation = pickle.load(open('artifacts/similarity.pickle','rb'))


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={getKey()}"

    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    fullpath = "http://image.tmdb.org/t/p/w500"+poster_path
    return  fullpath

def recommond(movie):
    index = movies[movies['title']==movie].index[0]
    distances = sorted(list(enumerate(simulation[index])),reverse=True,key=lambda x:x[1])
    recommended_movies_names=[]
    recommended_movies_poster=[]
    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies_names.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies_poster,recommended_movies_names

st.header("Movie Recommend System")
# hello
movie_list = movies['title'].values
selected_movies = st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)

if st.button('Recommendation'):
    recommend_movies_poster,recommended_movies_name = recommond(selected_movies)
    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommend_movies_poster[0])

    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommend_movies_poster[1])

    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommend_movies_poster[2])

    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommend_movies_poster[3])

    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommend_movies_poster[4])

    col6, col7, col8, col9, col10 = st.columns(5)

    with col6:
        st.text(recommended_movies_name[5])
        st.image(recommend_movies_poster[5])

    with col7:
        st.text(recommended_movies_name[6])
        st.image(recommend_movies_poster[6])
    with col8:
        st.text(recommended_movies_name[7])
        st.image(recommend_movies_poster[7])
    with col9:
        st.text(recommended_movies_name[8])
        st.image(recommend_movies_poster[8])
    with col10:
        st.text(recommended_movies_name[9])
        st.image(recommend_movies_poster[9])



