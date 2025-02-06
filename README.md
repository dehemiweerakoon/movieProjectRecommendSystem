# Movie Recommendation System

This project implements a movie recommendation system using collaborative filtering.  It's built using Python, Streamlit for the user interface, and leverages the TMDB (The Movie Database) API for movie poster retrieval.

## Overview

The application allows users to select a movie from a dropdown list, and upon clicking the "Recommendation" button, it displays the top 10 movies that are similar to the selected movie. Similarity is calculated based on a pre-computed similarity matrix.  Movie posters are fetched dynamically from the TMDB API.

## Technologies Used

* **Python:** Core programming language.
* **Streamlit:**  For creating the interactive web application.
* **Pickle:** For serializing and deserializing Python objects (movie list and similarity matrix).
* **Requests:** For making HTTP requests to the TMDB API.

## Obtain a TMDB API key:

Create an account at https://www.themoviedb.org/.
Go to your account settings and request an API key.
Create Key.py:

In the project root directory, create a file named Key.py.
Inside Key.py, add the following line, replacing YOUR_API_KEY with your actual TMDB API key:
<!-- end list -->

## Python

def getKey():
    return "YOUR_API_KEY"
used for getting the API key that can we get using website

## Run the Streamlit app

**streamlit run app.py**

![image](https://github.com/user-attachments/assets/75cbfaa4-d2e9-4519-85bc-c58c91e30586)
