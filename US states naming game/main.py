import turtle
import pandas
from state_tracker import StateTracker

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

us_data = pandas.read_csv("50_states.csv")
col_list = us_data.state.values.tolist()

missed_states = []
guessed_states = []
guess = 0

while guess != 50:
    answer_state = screen.textinput(title=f"{guess}/50 States Correct", prompt="What's another state's name?")
    ans = answer_state.title()
    if ans == "Exit":
        missed_states = [guessed for guessed in col_list if guessed not in guessed_states]
        data = pandas.DataFrame(missed_states)
        data.to_csv("missed_states.csv")
        break
    if ans not in guessed_states:
        if ans in col_list:
            guessed_states.append(ans)
            guess += 1
            comp_list = us_data[us_data.state == ans]
            x = int(comp_list.x)
            y = int(comp_list.y)
            state_tracker = StateTracker(ans, x, y)
    else:
        pass





