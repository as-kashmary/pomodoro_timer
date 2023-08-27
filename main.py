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
reps=0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps

    if reps%2 and reps!=7:
        title_label.config(text="Short Break",fg=PINK,bg=YELLOW,font=(FONT_NAME,24,"bold"))
        count_down(SHORT_BREAK_MIN * 60);
    elif reps!=7:
        count_down(WORK_MIN * 60);
    else:
        title_label.config(text="Long Break",fg=RED,bg=YELLOW,font=(FONT_NAME,24,"bold"))
        count_down(LONG_BREAK_MIN*60)
    reps +=1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_sec=count
    sec=count_sec%60;
    if len(str(sec))==1:
        count_show = str(int(count_sec / 60)) + ":0" + str(count_sec % 60)
    else:
        count_show = str(int(count_sec / 60)) + ":" + str(count_sec % 60)

    canvas.itemconfig(canvas_t, text=count_show)
    if count_sec >0:
        window.after(1000, count_down, count_sec - 1)
    else:
        start_timer();

# ---------------------------- UI SETUP ------------------------------- #

window=Tk();
title_label=Label(text="Work time",fg=GREEN,bg=YELLOW,font=(FONT_NAME,24,"bold"))
title_label.grid(row=0,column=1);



window.minsize(height=100, width=50);
window.config(padx=100,pady=100,bg=YELLOW)
pic=PhotoImage(file="tomato.png")
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=pic)
canvas_t=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,24,"bold"))
canvas.grid(row=1,column=1);

button1=Button(command=start_timer,text="Start", font=(FONT_NAME,10,"bold"))
button1.config(padx=1,pady=1)
button1.grid(row=2,column=0);

tick=Label(text="✔",fg=GREEN,bg=YELLOW)
tick.config(padx=5,pady=5)
tick.grid(row=3,column=1)

button2=Button(text="Reset",font=(FONT_NAME,10,"bold"))
button1.config(padx=1,pady=1)
button2.grid(row=2,column=2);



window.mainloop()
