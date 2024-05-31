# Movie Collection Web App

## Description

This project is a web application for managing a movie collection. Users can add, edit, view, and delete movies from their collection. The app uses The Movie Database (TMDb) API to fetch movie details.

## Features

- View a list of movies sorted by rating.
- Add new movies by searching for titles using the TMDb API.
- Edit movie ratings and reviews.
- Delete movies from the collection.

## Technologies Used

- Python
- Flask
- Flask-Bootstrap
- Flask-WTF
- Flask-SQLAlchemy
- SQLite
- TMDb API
- HTML/CSS

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install the required packages:**
    ```bash
    python -m pip install -r requirements.txt
    ```

3. **Set up the database:**
    ```bash
    python
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```

4. **Get your TMDb API token:**
    - Sign up on [The Movie Database](https://www.themoviedb.org/).
    - Go to your account settings and generate an API token.
    - Replace `<GET YOUR API TOKEN BY SIGNING IN TO TMDB>` in the code with your actual API token.

5. **Run the application:**
    ```bash
    python app.py
    ```

## Usage

- **Home Page:** Displays all movies in the collection sorted by rating.
- **Add Movie:** Navigate to `/add` to search for and add a new movie.
- **Edit Movie:** Navigate to `/edit?id=<movie_id>` to edit a movie's rating and review.
- **Delete Movie:** Navigate to `/delete?id=<movie_id>` to delete a movie from the collection.

## File Structure

```
.
├── app.py                  # Main application file
├── templates/              # HTML templates
│   ├── index.html          # Home page template
│   ├── add.html            # Add movie page template
│   ├── edit.html           # Edit movie page template
├── Movie-collection.db     # SQLite database file
├── requirements.txt        # List of required packages
├── static/                 # Static files (images, CSS, etc.)
└── README.md               # This README file
```

