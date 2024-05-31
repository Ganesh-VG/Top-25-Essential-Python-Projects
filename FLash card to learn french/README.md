# Flashy - Flashcard, French Learning App

## Description
Flashy is a flashcard learning application built using Tkinter and pandas in Python. This app helps users learn French words by displaying a French word and then revealing its English translation after a brief delay. The app tracks progress by saving words that need to be learned in a CSV file.

## Features
- Displays French words on flashcards.
- Reveals the English translation after a delay.
- Keeps track of words to be learned.
- Updates the list of words to be learned dynamically.

## Installation

### Prerequisites
- Python 3.x
- Tkinter (usually included with Python installations)
- pandas

### Installation Steps
1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install required packages**:
    ```bash
    pip install pandas
    ```

3. **Prepare data files**:
    Ensure you have the `french_words.csv` file in a `data` directory. This file should contain the French words and their English translations in the format:
    ```
    French,English
    Bonjour,Hello
    ...
    ```

4. **Prepare image files**:
    Ensure you have the following image files in an `images` directory:
    - `card_front.png`
    - `card_back.png`
    - `right.png`
    - `wrong.png`

## Usage

1. **Run the application**:
    ```bash
    python flashy.py
    ```

2. **Interacting with the application**:
    - The app will display a French word on the card.
    - After 3 seconds, the English translation will be displayed.
    - Click the "right" button if you know the word. This will remove the word from the learning list.
    - Click the "wrong" button if you don't know the word. This will keep the word in the learning list.

## Code Explanation

### Importing Libraries
```python
from tkinter import *
import pandas as p
import random
```

### Reading Data
The code tries to read `word_to_learn.csv` to get the list of words the user is still learning. If this file is empty, it reads from `french_words.csv`.

### Flashcard Functionality
- **word_call()**: Chooses a random word from the list, displays it, and removes it from the list if the user knows it.
- **display_ans()**: Displays the English translation of the current word.

### GUI Setup
- Sets up the Tkinter window with a canvas to display the flashcards.
- Adds buttons for user interaction to indicate whether they know the word or not.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
