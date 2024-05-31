# Quiz Game Application

## Description
This is a simple Quiz Game application implemented in Python. The game uses a series of questions stored in a separate data file and tests the user's knowledge by presenting these questions one by one. The user can answer and get immediate feedback on their correctness.

## Features
- Presents questions one by one.
- Tracks the user's score.
- Provides immediate feedback for each question.

## Installation

### Prerequisites
- Python 3.x

### Installation Steps
1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Ensure you have the necessary files**:
    - `question_model.py`
    - `data.py`
    - `quiz_brain.py`
    - The main script to run the quiz (e.g., `main.py`).

## Files and Structure

### question_model.py
Defines the `Question` class which holds the question text and the correct answer.

### data.py
Contains the question data in a list of dictionaries, each with a "text" and "answer" key.

### quiz_brain.py
Contains the `Quiz_Brain` class which manages the flow of the quiz, including presenting questions and keeping track of the score.

## Usage

1. **Run the application**:
    ```bash
    python main.py
    ```

2. **Gameplay**:
    - The quiz presents one question at a time.
    - The user inputs their answer.
    - Immediate feedback is provided.
    - The game continues until all questions are answered.
    - The final score is displayed at the end.

## Code Example

### Main Script (main.py)
```python
from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

question_bank = []

for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))

quiz = Quiz_Brain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
```

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
