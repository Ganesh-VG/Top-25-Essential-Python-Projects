from tkinter import *
import playsoundsimple as pss
import math
from datetime import date
import pandas as p

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
L_GREEN = "#00FF00"
GREY = "#404040"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
count_timer = 0
pause = False
with open("Total_Work_Hours.txt") as file:
    work_hours = float(file.read())

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_tick.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global pause
    if pause is False:
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps == 8:
            count_down(long_break_sec)
            label_timer.config(text="BREAK", fg=RED)
            s = pss.Sound("Radar Notification.mp3")
            s.play(1)
            s.wait()
            daily_data_mod()
            work_log()

        elif reps == 1 or reps == 3 or reps == 5 or reps == 7:
            count_down(work_sec)
            label_timer.config(text="WORK", fg=PINK)
            s = pss.Sound("Announcement Notification ! Announcement ! Notification.mp3")
            s.play(1)
            s.wait()

        elif reps == 2 or reps == 4 or reps == 6:
            count_down(short_break_sec)
            label_timer.config(text="BREAK", fg=PINK)
            s = pss.Sound("notification.mp3")
            s.play(1)
            s.wait()
            daily_data_mod()
            work_log()

        else:
            reset_timer()
            start_timer()

    else:
        global count_timer
        pause = not pause
        count_down(count_timer)

# ---------------------------- PAUSE ------------------------------- #


def do_pause():
    global pause
    pause = True

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global count_timer
    count_timer = count
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_second = count % 60
    if count_second == 0:
        count_second = "00"
    elif count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")
    if count > 0:
        global pause
        if pause is False:
            global timer
            timer = window.after(1000, count_down, count-1)

    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "🟢 "
        label_tick.config(text=marks)

# ---------------------------- DAILY DATA ------------------------------- #


def daily_data_mod():

    due = p.read_csv("Daily_Work_Log.csv")
    today = str(date.today())
    comp = due["date"].iloc[-1]
    wri = due["time"].iloc[-1]

    if today == comp:

        due.drop(due.index[(due["date"] == today)], axis=0, inplace=True)
        due.to_csv("Daily_Work_Log.csv", mode="w", index=False)
        today = date.today()
        wri += 0.5
        data = {
            "date": [today],
            "time": [wri],
        }
        df = p.DataFrame(data)
        df.to_csv("Daily_Work_Log.csv", mode="a", index=False, header=False)

    else:
        data = {
            "date": [today],
            "time": [0.5],
        }
        df = p.DataFrame(data)
        df.to_csv("Daily_Work_Log.csv", mode="a", index=False, header=False)


# ---------------------------- UI SETUP ------------------------------- #

def work_log():
    global work_hours
    work_hours += 0.5
    with open("Total_Work_Hours.txt", mode="w") as file:
        file.write(f"{work_hours}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("WORK LOG RECORDER")
window.config(padx=30, pady=10, bg=GREY)

canvas = Canvas(width=180, height=100, bg=GREY, highlightthickness=0)
timer_text = canvas.create_text(90, 50, text="00:00", fill="white", font=("FONT_NAME", 35, "bold"))
canvas.grid(column=1, row=1)


label_timer = Label(text="Timer", font=("Courier", 40, "bold"), fg=GREEN, bg=GREY, highlightthickness=0)
label_timer.grid(column=1, row=0)

button_start = Button(text="START", fg="white", bg=GREY, highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="RESET", fg="white", bg=GREY, highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

button_pause = Button(text="PAUSE", fg="white", bg=GREY, highlightthickness=0, command=do_pause)
button_pause.grid(column=1, row=2, pady=10)

label_tick = Label(font=("Courier", 15), fg=L_GREEN, bg=GREY, highlightthickness=0)
label_tick.grid(column=1, row=3, pady=10)


window.mainloop()