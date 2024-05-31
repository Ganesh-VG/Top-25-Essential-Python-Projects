from tkinter import *
import pandas as p
import random

try:
    data_imp = p.read_csv("word_to_learn.csv")
    data = data_imp.to_dict(orient="records")

except p.errors.EmptyDataError:
    data_imp = p.read_csv("./data/french_words.csv")
    data = data_imp.to_dict(orient="records")

ran_word = {}


def word_call():
    global ran_word, delay
    window.after_cancel(delay)
    if len(data) == 0:
        print("Game Over!")
        canvas.itemconfig(title, text="Thankyou", fill="black")
        canvas.itemconfig(word, text="Game Over!", fill="black")
    else:
        ran_word = random.choice(data)
        data.remove(ran_word)
        df = p.DataFrame(data)
        df.to_csv("word_to_learn.csv", mode="w", index=False)
        canvas.itemconfig(image, image=image_front)
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(word, text=ran_word["French"], fill="black")
        delay = window.after(3000, func = display_ans)


def display_ans():
    image_back = PhotoImage(file="./images/card_back.png")
    canvas.itemconfig(image, image=image_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=ran_word["English"], fill="white")


BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("FLASHY")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR,highlightthickness=0)

delay = window.after(3000, func=display_ans)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_front = PhotoImage(file="./images/card_front.png")
image = canvas.create_image(400, 263, image=image_front)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

image_r = PhotoImage(file="./images/right.png")
button_r = Button(image=image_r, highlightthickness=0, command=word_call)
button_r.grid(column=0, row=1)

image_w = PhotoImage(file="./images/wrong.png")
button_w = Button(image=image_w, highlightthickness=0, command=display_ans)
button_w.grid(column=1, row=1)

window.mainloop()