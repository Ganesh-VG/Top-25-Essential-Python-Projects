# Flask Web Application for Blog

This project is a Flask web application that displays blog posts fetched from an external API and allows users to submit contact information through a Google Form. The project utilizes Selenium for form submission automation and sends an email notification upon successful form submission.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Flask
- Requests
- Selenium
- smtplib (part of the Python standard library)

Install the required packages by running:
```bash
pip install flask requests selenium
```

## Project Structure
- `app.py`: Main application file containing Flask routes and logic.
- `templates/`: Directory containing HTML templates for the web interface.
  - `index.html`: Home page displaying all blog posts.
  - `about.html`: About page.
  - `contact.html`: Contact form page.
  - `post.html`: Individual blog post page.
  - `display.html`: Page displayed after form submission.

## Setting Up
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/flask-blog-app.git
   cd flask-blog-app
   ```

2. **Configure Environment Variables**:
   Update the following placeholders in `app.py` with your actual values:
   - `YOUR EMAIL`
   - `YOUR PASSWORD`
   - `YOUR CHROMEDRIVER PATH`
   - `YOUR GOOGLE FORM LINK`
   - `YOUR TO ADDRESS`

3. **Install ChromeDriver**:
   Download and install ChromeDriver from [here](https://sites.google.com/chromium.org/driver/) and provide the path to the executable in `app.py`.

4. **Run the Application**:
   ```bash
   python app.py
   ```

## Flask Routes
- **Home Route (`/`)**: Displays all blog posts.
- **About Route (`/about`)**: Displays the about page.
- **Contact Route (`/contact`)**: Displays the contact form.
- **Form Entry Route (`/form-entry`)**: Handles contact form submissions, automates form filling using Selenium, and sends an email notification.
- **Post Route (`/post/<int:index>`)**: Displays a specific blog post by index.

## Example Usage
- **Access Home Page**:
  Open `http://127.0.0.1:5001/` in your web browser to view all blog posts.

- **Submit Contact Form**:
  Navigate to `http://127.0.0.1:5001/contact` to fill and submit the contact form.

## Notes
- Ensure that ChromeDriver matches your installed version of Google Chrome.
- Update email credentials and recipient address as necessary.
- Selenium's automated form submission may require updates if the structure of the Google Form changes.

## Conclusion
This project demonstrates how to build a Flask web application that integrates with external APIs, automates form submissions using Selenium, and sends email notifications. It can be expanded with additional features such as user authentication, advanced search capabilities, and more.

For any questions or issues, please contact [your email] for support.
