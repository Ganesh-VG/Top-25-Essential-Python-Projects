# Work Log Recorder

## Overview

The Work Log Recorder is a productivity tool that helps users manage their work sessions using the Pomodoro Technique. It features a timer to track work and break intervals, logs daily work sessions, and keeps a record of total work hours.

## Features

- **Pomodoro Timer:** Alternate between work and break sessions with customizable durations.
- **Daily Work Log:** Automatically logs the duration of work sessions.
- **Total Work Hours:** Maintains a cumulative record of total work hours.
- **Pause Function:** Pause and resume the timer as needed.
- **Notifications:** Play sound notifications at the end of each session.

## Requirements

- Python 3.x
- Tkinter library (standard with Python installation)
- playsoundsimple library
- pandas library

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install required libraries:**
    ```bash
    pip install pandas playsoundsimple
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **Start Timer:** Click the "START" button to begin the Pomodoro timer.
3. **Pause Timer:** Click the "PAUSE" button to pause the timer.
4. **Reset Timer:** Click the "RESET" button to reset the timer.

## File Structure

```
.
├── main.py                  # Main application file
├── center_line.py           # Centerline class for drawing road lines
├── move_car.py              # MoveCar class for handling car movement
├── score_board.py           # ScoreBoard class for displaying the score
├── Total_Work_Hours.txt     # Text file to store total work hours
├── Daily_Work_Log.csv       # CSV file to store daily work logs
├── README.md                # This README file
```

## Customization

You can customize the timer durations by modifying the constants in the `main.py` file:
- `WORK_MIN`: Duration of work sessions in minutes (default is 25 minutes)
- `SHORT_BREAK_MIN`: Duration of short breaks in minutes (default is 5 minutes)
- `LONG_BREAK_MIN`: Duration of long breaks in minutes (default is 20 minutes)

