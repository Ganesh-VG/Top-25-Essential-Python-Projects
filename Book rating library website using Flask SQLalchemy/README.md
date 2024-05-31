# Book rating library website using Flask SQLalchemy

This project is a simple web application built using Flask and SQLAlchemy to manage a collection of books. Users can add, edit, and delete books from the collection. The application uses an SQLite database to store book data, including title, author, and rating.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- Flask-SQLAlchemy

You can install the required packages by running:

```bash
pip install -r requirements.txt
```

## Project Structure

- `app.py`: The main application file containing routes and database models.
- `templates/`: Directory containing HTML templates for the application.
  - `index.html`: Displays the list of books.
  - `add.html`: Form to add a new book.
  - `edit.html`: Form to edit an existing book.
- `new-books-collection.db`: SQLite database file storing book information.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/book-collection-flask.git
   cd book-collection-flask
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**

   ```bash
   python app.py
   ```

   The application will be accessible at `http://127.0.0.1:5000`.

## Routes

- `/`: Displays the list of books sorted by title.
- `/add`: Shows the form to add a new book.
- `/form-entry`: Handles the form submission to add a new book.
- `/edit/<index>`: Shows the form to edit the rating of a book with the given index.
- `/delete/<index>`: Deletes the book with the given index.

## Code Overview

### Models

- **Books**: Represents the books table in the database with columns for `id`, `title`, `author`, and `rating`.

### Routes

- **Home Route (`/`)**: Fetches and displays all books ordered by title.
- **Add Route (`/add`)**: Renders the form to add a new book.
- **Form Entry Route (`/form-entry`)**: Handles the POST request to add a new book to the database.
- **Edit Route (`/edit/<index>`)**: Renders the form to edit a book's rating and handles the POST request to update the rating.
- **Delete Route (`/delete/<index>`)**: Deletes a book from the database.

## Templates

- **index.html**: Displays all books in a table with options to edit and delete each book.
- **add.html**: Contains a form to add a new book.
- **edit.html**: Contains a form to edit the rating of an existing book.

## Example Usage

To add a book, navigate to `/add`, fill out the form, and submit. To edit a book's rating, click the "Edit" button next to the book on the home page, update the rating, and submit. To delete a book, click the "Delete" button next to the book on the home page.

## Conclusion

This Flask application provides a simple interface for managing a collection of books, demonstrating basic CRUD operations using Flask and SQLAlchemy. The project can be expanded with additional features such as user authentication, advanced search, and more.
