# Cafe and Wifi Website

## Description
This Flask web application allows users to submit and view information about various cafes, including their location, operating hours, and ratings for coffee, wifi, and power outlets. The project uses Flask for the backend, Flask-WTF for form handling, and Flask-Bootstrap for styling.

## Features
1. **Home Page**: Displays the homepage of the application.
2. **Add Cafe**: Allows users to add new cafes by filling out a form with the cafe's name, location URL, operating hours, and ratings for coffee, wifi, and power outlets.
3. **View Cafes**: Displays a list of all cafes stored in the CSV file.
4. **Cafe URLs**: Redirects to the cafe's location URL when a cafe is selected.

## Installation

### Prerequisites
- Python 3.x
- Flask
- Flask-Bootstrap
- Flask-WTF

### Installation Steps
1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    flask run
    ```

## File Structure
- `app.py`: Main application file containing the Flask routes and form handling logic.
- `templates/`: Directory containing HTML templates for the application.
  - `index.html`: Home page template.
  - `add.html`: Template for the add cafe form.
  - `cafes.html`: Template for displaying all cafes.
- `cafe-data.csv`: CSV file used to store cafe data.

## Usage
- **Add a Cafe**: Navigate to `/add` and fill out the form to add a new cafe. The data will be appended to the `cafe-data.csv` file.
- **View Cafes**: Navigate to `/cafes` to see a list of all cafes. Clicking on a cafe will redirect to its location URL.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Acknowledgements
- The Flask framework for making web development easier.
- Flask-Bootstrap for integrating Bootstrap with Flask.
- Flask-WTF for seamless form handling.

---

Feel free to modify the content according to your specific needs and preferences.
