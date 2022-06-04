from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
tick = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    main_label.config(text="Timer", fg=GREEN)
    reps = 0
    tick_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, tick
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    tick_label.config(text=(tick * int(reps / 2)))
    if reps % 8 == 0:
        main_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        main_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        main_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps, timer
    count_min = int(count / 60)
    if count_min < 10:
        count_min = "0"+ str(count_min)
    count_sec = int(count % 60)
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(5, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)

main_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45, "bold"))
main_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

tick_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45, "bold"))
tick_label.grid(row=3, column=1)



window.mainloop()
