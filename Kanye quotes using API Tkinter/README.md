# Kanye Says - Tkinter App

## Description
"Kanye Says" is a fun, simple Tkinter application that fetches random quotes from Kanye West using the "Kanye Rest" API. Each time the user clicks on the Kanye image, a new quote is displayed on the screen.

## Features
- Fetches random Kanye West quotes from an online API.
- Displays the quote in a nicely formatted window.
- Uses Tkinter for the graphical interface.

## Installation

### Prerequisites
- Python 3.x
- Tkinter (usually included with Python installations)
- requests library

### Installation Steps
1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install required packages**:
    ```bash
    pip install requests
    ```

3. **Prepare image files**:
    Ensure you have the following image files in the project directory:
    - `background.png`
    - `kanye.png`

## Usage

1. **Run the application**:
    ```bash
    python kanye_says.py
    ```

2. **Interacting with the application**:
    - The app will display a window with a background image and a quote.
    - Click the Kanye image button to fetch and display a new quote from the API.

## Code Explanation

### Importing Libraries
```python
from tkinter import *
import requests
```

### Fetching Quotes
- **get_quote()**: Makes a request to the "Kanye Rest" API to fetch a random quote and updates the displayed quote on the canvas.

### GUI Setup
- Sets up the Tkinter window with a canvas to display the quote and background image.
- Adds a button with Kanye's image which, when clicked, fetches a new quote.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

