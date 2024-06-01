# Hirst_painting using Colorgram and Turtle

## Overview

This project creates a Hirst painting using Colorgram and Turtle graphics. The turtle navigates through a series of colorful dots arranged in a grid pattern.

## Prerequisites

- Python 3.x
- `turtle` library (included with Python standard library)
- `colorgram.py` module for color extraction (optional, included code provides a predefined color list)

## Setup Instructions

1. **Install Python**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install Required Modules**: Install the `colorgram.py` module if you need to extract colors from an image:
   ```bash
   pip install colorgram.py
   ```

3. **Download or Create Image**: Place an image named `Untitled.jpg` in the same directory as your script if you plan to extract colors from it.

## Code Explanation

### Color Extraction (Optional)
The following code extracts colors from an image and stores them in a list:
```python
import colorgram

rgb_colors = []
colors = colorgram.extract('Untitled.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
```

### Main Code
The main code uses the `turtle` library to draw a grid of dots with random colors from a predefined list:
```python
import random
from turtle import Screen
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.penup()
tim.speed("fastest")
tim.goto(-500, -225)
t.colormode(255)

color_list = [(202, 163, 98), (45, 97, 147), (168, 49, 80), (222, 210, 108), (141, 92, 64), (118, 172, 203), (173, 163, 40), (210, 133, 171), (208, 67, 105), (223, 78, 56), (91, 106, 193), (143, 33, 60), (31, 139, 94), (57, 172, 105), (124, 218, 205), (228, 170, 186), (47, 186, 197), (126, 191, 168), (100, 50, 42), (34, 61, 117), (223, 208, 22), (148, 207, 225), (169, 187, 225), (233, 173, 163), (49, 57, 66), (41, 75, 78)]
color_list_1 = [(45, 97, 147), (168, 49, 80), (141, 92, 64), (118, 172, 203), (173, 163, 40), (210, 133, 171), (208, 67, 105), (223, 78, 56), (91, 106, 193), (143, 33, 60), (31, 139, 94), (57, 172, 105), (124, 218, 205), (228, 170, 186), (47, 186, 197), (126, 191, 168), (100, 50, 42), (34, 61, 117), (148, 207, 225), (169, 187, 225), (233, 173, 163), (49, 57, 66), (41, 75, 78)]

for b in range(10):
    for a in range(10):
        tim.forward(50)
        tim.dot(20, random.choice(color_list_1))
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(1000)
    tim.right(180)
tim.hideturtle()

screen = Screen()
screen.exitonclick()
```

## How to Run

1. **Run the Script**: Execute the Python script in your terminal or IDE.
2. **View the Drawing**: A window will open displaying the turtle creating a grid of dots with random colors.

## Notes

- The `colorgram` module is optional and used only if you want to extract colors from an image.
- Adjust the `goto` method's coordinates and the grid size as per your screen dimensions.
