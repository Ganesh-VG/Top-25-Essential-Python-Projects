# U.S. States Game

## Overview

This project is a simple educational game to test and improve your knowledge of the U.S. states. The game prompts the user to name as many U.S. states as they can. The correctly guessed states are displayed on a blank map of the United States.

## Prerequisites

- Python 3.x
- `turtle` module (included with Python standard library)
- `pandas` module

## Files

1. `main.py` (the main script)
2. `state_tracker.py` (handles state name display)
3. `blank_states_img.gif` (image of the blank U.S. map)
4. `50_states.csv` (data file containing state names and coordinates)
5. `missed_states.csv` (will be generated, contains states that were not guessed)

### `50_states.csv`

Ensure your `50_states.csv` file contains the following columns:
- `state`: Name of the state
- `x`: X-coordinate for state label placement
- `y`: Y-coordinate for state label placement

### `state_tracker.py`

This file contains the `StateTracker` class which is responsible for displaying the guessed state names on the map.

## How to Run

1. **Ensure all files are in the same directory**: Place `main.py`, `state_tracker.py`, `blank_states_img.gif`, and `50_states.csv` in the same folder.
2. **Run the main script**: Execute `main.py` in your Python environment.
3. **Start guessing**: Enter the names of U.S. states in the prompt. Correct guesses will be displayed on the map.
4. **Exit**: Type "Exit" to end the game and generate `missed_states.csv` with the names of states you missed.

Enjoy the game and improve your knowledge of U.S. states!
