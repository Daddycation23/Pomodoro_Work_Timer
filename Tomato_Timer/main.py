from tkinter import *
import math
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 1
count_timer = None
pygame.mixer.init()

def play_alarm():
    pygame.mixer.music.load(r"") #Input ur music file path here
    pygame.mixer.music.play(loops=0)

def stop_alarm():
    pygame.mixer.music.stop()


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(count_timer)
    timer["text"] = "Timer"
    stop_alarm()
    global rep
    rep = 1
    tick["text"] = ""
    canvas.itemconfig(counter, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    stop_alarm()
    global rep
    if rep % 2 == 0 and rep < 8:
        count_down(SHORT_BREAK_MIN * 60)
        timer.config(text="Short Break", fg=PINK)
    elif rep == 1 or rep % 2 != 0:
        count_down(WORK_MIN * 60)
        timer.config(text="Work", fg=GREEN)
    elif rep == 8:
        count_down(LONG_BREAK_MIN * 60)
        timer.config(text="Loooooooong Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global rep
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(counter, text=f"{count_min}:{count_sec}")
    if count > 0:
        global count_timer
        count_timer = window.after(1000, count_down, count - 1)
    else:
        check = ""
        work_sessions = math.floor(rep/2)
        for _ in range(work_sessions):
            check += "✔️"
        tick.config(text=check)
    if count == 0 or count < 0:
        play_alarm()
        rep += 1
        if rep > 8:
            reset_timer()
            rep = 1


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato Work Timer")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=300, height=250, bg=YELLOW, highlightthickness=0)
tomahtoe_photo = PhotoImage(file="tomato.png")
canvas.create_image(150, 125, image=tomahtoe_photo)
counter = canvas.create_text(150, 150, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer = Label(text="Timer")
timer.grid(column=1, row=0)
timer.config(bg=YELLOW, font=(FONT_NAME, 40, "bold"), foreground=GREEN)

start_button = Button(command=start_timer, width=6, height=2)
start_button["text"] = "Start"
start_button.grid(column=0, row=2)

reset_button = Button(command=reset_timer, width=6, height=2)
reset_button["text"] = "Reset"
reset_button.grid(column=2, row=2)

tick = Label()
tick.grid(column=1, row=2)
tick.config(bg=YELLOW, font=(FONT_NAME, 12), foreground=GREEN)



window.mainloop()
