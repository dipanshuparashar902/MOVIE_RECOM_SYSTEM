
import streamlit as st
import pickle
import requests

# Set page to wide mode for a better layout
st.set_page_config(page_title="Movie Recommender", layout="wide")

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stHeading h1 {
        color: #E50914; /* Netflix Red */
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }
    .movie-card {
        transition: transform .2s;
        border-radius: 10px;
    }
    .movie-card:hover {
        transform: scale(1.05);
        cursor: pointer;
    }
    div[data-testid="stText"] {
        font-weight: 600;
        font-size: 14px;
        text-align: center;
        height: 50px;
        color: #ffffff;
    }
    hr {
        margin-top: 2rem;
        margin-bottom: 2rem;
        border: 0;
        border-top: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CACHED FUNCTIONS FOR PERFORMANCE ---
@st.cache_data
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=19ad151da23e3c6246eddfe342f20be1&language=en-US"
        data = requests.get(url).json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=Error"

# Load data
movies = pickle.load(open("movies_list.pkl", "rb"))
#similarity = pickle.load(open("similarity.pkl", "rb")) #for all similarity data
similarity = pickle.load(open("similarity_compact.pkl", "rb"))
movies_list = movies['title'].values

st.title('🎬 Movie Recommendation System')

# --- SECTION 1: TRENDING NOW (HORIZONTAL SCROLL STYLE) ---
if 'random_trending' not in st.session_state:
    st.session_state.random_trending = movies.sample(10) # Showing 10 movies

st.subheader("🔥 Trending Now")
# Creating a container with columns to mimic a gallery
t_cols = st.columns(10)
for i, (index, row) in enumerate(st.session_state.random_trending.iterrows()):
    with t_cols[i]:
        poster = fetch_poster(row['id'])
        st.image(poster, use_container_width=True)

st.markdown("---")

# --- SECTION 2: SEARCH & RECOMMEND ---
st.subheader("🔍 Find Your Next Favorite")
col_search, _ = st.columns([2, 2]) # Keep search bar on the left
with col_search:
    selectvalue = st.selectbox("Type or select a movie you liked:", movies_list)

# def recommend(movie): all movies similarity function
#     movie_index = movies[movies['title'] == movie].index[0]
#     distance = sorted(list(enumerate(similarity[movie_index])), key=lambda vector: vector[1], reverse=True)
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in distance[1:7]: # Recommending 6 movies for a cleaner layout
#         movies_id = movies.iloc[i[0]].id
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movies_posters.append(fetch_poster(movies_id))
#     return recommended_movies, recommended_movies_posters

# Load the compact model instead of the large one
similarity = pickle.load(open("similarity_compact.pkl", "rb"))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    
    # Grab the pre-calculated top matches from the dictionary
    distance = similarity[movie_index] 
    
    recommended_movies = []
    recommended_movies_posters = []
    
    # Iterate through the pre-calculated distances
    for i in distance[0:6]: 
        movies_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies_id))
        
    return recommended_movies, recommended_movies_posters

if st.button("Get Recommendations"):
    names, posters = recommend(selectvalue)
    
    st.write("### Recommended for You")
    # Using 6 columns (two rows of 3 or one row of 6)
    cols = st.columns(6)
    for i in range(6):
        with cols[i]:
            st.image(posters[i], use_container_width=True)
            st.text(names[i])