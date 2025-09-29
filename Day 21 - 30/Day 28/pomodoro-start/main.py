import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔"
CANVAS_WIDTH = 206
CANVAS_HEIGHT = 224
PADDING_X = 100
PADDING_Y = 50
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #

def timer_start():
    count_down(10)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = "0" + str(count_min)

    if count_sec == 0:
        count_sec = "00"

    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=PADDING_X, pady=PADDING_Y)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=tomato_img)
timer_count = canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(window, text="Timer", font=(FONT_NAME, 46))
timer_label.grid(column=1, row=0)


start_button = Button(window, text="Start", command=timer_start)
start_button.grid(column=0, row=2)


reset_button = Button(window, text="Reset")
reset_button.grid(column=2, row=2)


check_mark_label = Label(window, text=CHECK_MARK, font=(FONT_NAME, 25), fg=GREEN)
check_mark_label.grid(column=1, row=3)


window.mainloop()