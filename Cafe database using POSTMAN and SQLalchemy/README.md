# Cafe database using POSTMAN and SQLalchemy



This project is a Flask web application that provides an API for managing a database of cafes. The application supports CRUD operations (Create, Read, Update, Delete) and allows users to interact with the cafe data via HTTP requests. The app uses SQLAlchemy for database operations and SQLite as the database backend.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Flask
- Flask-SQLAlchemy

To install the required packages, use the following command:

```bash
pip install -r requirements.txt
```

## Project Structure

- `app.py`: The main application file containing the Flask routes and database models.
- `templates/`: Directory containing the HTML templates for the web interface.
  - `index.html`: The home page template.

## Database

The application uses SQLite for storing cafe data. The database schema is defined using SQLAlchemy ORM.

## Models

- **Cafe**: Represents a cafe with the following fields:
  - `id`: Integer, primary key.
  - `name`: String, unique, non-nullable.
  - `map_url`: String, non-nullable.
  - `img_url`: String, non-nullable.
  - `location`: String, non-nullable.
  - `seats`: String, non-nullable.
  - `has_toilet`: Boolean, non-nullable.
  - `has_wifi`: Boolean, non-nullable.
  - `has_sockets`: Boolean, non-nullable.
  - `can_take_calls`: Boolean, non-nullable.
  - `coffee_price`: String, nullable.

## Routes

- **Home Route (`/`)**: Renders the home page.
- **Random Cafe Route (`/random`)**: Returns a random cafe in JSON format.
- **All Cafes Route (`/all`)**: Returns a list of all cafes in JSON format.
- **Search Cafe Route (`/search/<loc>`)**: Searches for cafes by location and returns them in JSON format.
- **Add Cafe Route (`/add`)**: Adds a new cafe to the database.
- **Update Price Route (`/update_price/<cafe_id>`)**: Updates the coffee price of a cafe.
- **Report Closed Route (`/report_closed/<cafe_id>`)**: Deletes a cafe from the database.

## Running the Application

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/cafe-api-flask.git
   cd cafe-api-flask
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

## Example Usage

- **Get a Random Cafe:**

  ```bash
  GET /random
  ```

- **Get All Cafes:**

  ```bash
  GET /all
  ```

- **Search Cafes by Location:**

  ```bash
  GET /search/<loc>
  ```

- **Add a New Cafe:**

  ```bash
  POST /add
  ```

- **Update Cafe Price:**

  ```bash
  PATCH /update_price/<cafe_id>?new_price=<new_price>
  ```

- **Report a Cafe Closed:**

  ```bash
  DELETE /report_closed/<cafe_id>?api-key=TopSecretAPIKey
  ```

## Conclusion

This Flask application provides a simple and effective API for managing a cafe database, demonstrating basic CRUD operations with Flask and SQLAlchemy. It can be expanded with additional features such as user authentication, advanced search capabilities, and more.
