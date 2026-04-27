

**Movie Recommender System** 


**Project Overview**


This project is a comprehensive Content-Based Movie Recommendation System designed to provide users with personalized movie suggestions based on their viewing preferences. By analyzing movie metadata such as genres and plot overviews, the system identifies and recommends films with high thematic and structural similarity.

**Technical Implementation**
The project is divided into two primary phases:

1. Data Engineering & Model Training (main.ipynb)
Data Acquisition: Processed a dataset containing 10,000 movies, extracting key features like id, title, genre, and overview.

2.  Feature Engineering: Created a unified "tags" column by combining genres and plot summaries to capture the essence of each film.

3.  Vectorization: Utilized CountVectorizer to transform text data into numerical vectors.

4.  Similarity Computation: Implemented Cosine Similarity to calculate a multi-dimensional similarity matrix across the entire dataset, which was then serialized into a similarity.pkl file for production use.

**2. Web Application Deployment (app.py)**

1.  User Interface: Built a high-performance web dashboard using Streamlit, featuring a custom "Netflix-style" dark theme.

2.  Recommendation Engine: Developed logic to retrieve the top 6 most similar movies in real-time by querying the pre-computed similarity matrix.

3.  External API Integration: Integrated the TMDB (The Movie Database) API to dynamically fetch and display movie posters based on unique movie IDs.

4.  Discovery Features: Included a "Trending Now" gallery that showcases a randomized selection of movies to encourage broader user exploration.

**Working Screenshots and Videos**
1.  **Screenshots**

    <img width="1512" height="982" alt="MR-1" src="https://github.com/user-attachments/assets/ac82651b-615d-4dae-a321-b1579c256df6" />

    <img width="1512" height="982" alt="MR-2" src="https://github.com/user-attachments/assets/6c68cf74-13e3-411c-82aa-552d59e8254c" />

    <img width="1512" height="908" alt="MR-3" src="https://github.com/user-attachments/assets/2d7e100b-137d-44c2-9c21-25e2c6ad7b34" />

    <img width="1512" height="908" alt="MR-4" src="https://github.com/user-attachments/assets/fbde03b5-8cde-4b6c-ab83-fe98ddadfd8f" />

    <img width="1512" height="908" alt="MR-5" src="https://github.com/user-attachments/assets/ac3d7637-e77e-4a80-9a28-5b74fac73e67" />

    <img width="1512" height="908" alt="MR-6" src="https://github.com/user-attachments/assets/7c56116b-2ffe-4608-8447-b4bd412382c0" />

2. **Videos**

  https://github.com/user-attachments/assets/b80ad1a0-678f-4d1d-a49b-ee9f4f3606f2












**Business Value**

1.  Enhanced User Engagement: By providing relevant content recommendations, the system increases the time users spend on the platform.

2.  Automated Personalization: Eliminates the need for manual curation by using machine learning to understand content relationships.

3.  Scalable Architecture: The use of pre-computed similarity matrices ensures the application remains responsive even as the dataset grows.

**How to Run**

1.  Ensure you have the required libraries installed: pip install streamlit pandas requests scikit-learn.

2.  Run the Streamlit application: streamlit run app.py.
