# Book Recommender System - Collaborative Filtering

## Overview
This project implements a book recommender system using collaborative filtering. The collaborative filtering approach leverages user-item interactions to recommend books to users based on the preferences of similar users.

## Data Sources
- `books.csv`: Contains information about books, including ISBN, title, author, publication year, publisher, and image URLs.
- `ratings.csv`: Consists of user ratings for different books identified by ISBN.
- `users.csv`: Contains user information, including user ID, location, and age.

## Data Preprocessing
1. Merged the `ratings` and `books` datasets to associate book titles with each rating.
2. Dropped unnecessary columns like image URLs.
3. Addressed missing values in the datasets.
4. Filtered out users with low ratings to improve the quality of the collaborative filtering system.

## Collaborative Filtering
1. Created a user-item matrix representing user ratings for books.
2. Applied collaborative filtering using cosine similarity.
3. Saved the model components, including the user-item matrix and user similarity, using pickle.

## Streamlit App
1. Developed a Streamlit app to interact with the recommender system.
2. Loaded the saved model components.
3. Implemented a user interface allowing users to select a book and receive recommendations.
4. Displayed recommended books with their titles and corresponding images.

## Running the Streamlit App
1. Install the required dependencies using `pip install -r requirements.txt`.
2. Run the Streamlit app using the command `streamlit run book_recommendation_app.py`.

## Files and Artifacts
- `book_recommendation.ipynb`: Jupyter Notebook containing the collaborative filtering and model saving logic.
- `book_recommendation_app.py`: Streamlit app for user interaction.
- `artifacts/model.pkl`: Pickle file containing the saved collaborative filtering model.
- `artifacts/book_names.pkl`, `artifacts/final_rating.pkl`, `artifacts/book_pivot.pkl`: Additional model-related artifacts.

## Additional Notes
- Ensure that the dataset paths in the code are correctly specified.
- Adjust the model and Streamlit app logic based on specific project requirements.
