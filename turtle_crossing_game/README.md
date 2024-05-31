# Turtle Crossing Game

## Description

Turtle Crossing is a simple game built using Python's Turtle graphics module. The game involves a turtle trying to cross a road while avoiding moving cars. The player controls the turtle and aims to reach the other side of the screen without getting hit by the cars.

## Features

- **Screen Setup:** The game screen is set up with a khaki background and specific dimensions.
- **Center Lines:** The road has center lines to give a realistic road effect.
- **Moving Cars:** Cars move across the screen, creating obstacles for the turtle.
- **Score Board:** Keeps track of the player's score based on the number of successful crossings.

## Requirements

- Python 3.x
- Turtle module (standard with Python installation)

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Run the game:**
    ```bash
    python main.py
    ```

## Usage

- Use the arrow keys to control the turtle and navigate across the road.
- Avoid the moving cars to prevent the turtle from getting hit.
- Successfully reach the other side to increase your score.

## File Structure

```
.
├── main.py                  # Main game file
├── center_line.py           # Centerline class for drawing road lines
├── move_car.py              # MoveCar class for handling car movement
├── score_board.py           # ScoreBoard class for displaying the score
├── README.md                # This README file
```

## How to Play

1. **Launch the game:** Run the `main.py` file to start the game.
2. **Control the turtle:** Use the arrow keys to move the turtle.
3. **Avoid cars:** Navigate the turtle across the road while avoiding the moving cars.
4. **Score points:** Each successful crossing increases your score.

