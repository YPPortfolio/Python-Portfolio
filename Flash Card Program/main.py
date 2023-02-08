from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "white"
FONT = "Arial"
TO_LEARN = {}

try:
    with open("./data/words_to_learn.csv", "r") as data_file:
        data = pandas.read_csv(data_file)
except FileNotFoundError:
    with open("./data/french_words.csv", "r") as data_file:
        data = pandas.read_csv(data_file)
        TO_LEARN = data.to_dict(orient="records")
else:
    TO_LEARN = data.to_dict(orient="records")

CURRENT_WORD = {}

#--- NEW WORD GENERATION ---#
def next_card():
    global CURRENT_WORD, flip_timer
    canvas.after_cancel(flip_timer)
    CURRENT_WORD = random.choice(TO_LEARN)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=CURRENT_WORD["French"], fill="black")
    flip_timer = window.after(3000, func=answer_card)

def is_known():
    global TO_LEARN
    TO_LEARN.remove(CURRENT_WORD)
    data = pandas.DataFrame(TO_LEARN)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

#--- ANSWER CARD FLIP ---#
def answer_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill=WHITE)
    canvas.itemconfig(card_word, text=CURRENT_WORD["English"], fill=WHITE)


#--- UI SET UP ---#

# WINDOW
window = Tk()
window.title("Flash Card Practice")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=answer_card)

# CANVAS
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, (526/2), image=card_front_img)
card_title = canvas.create_text(400, 150, text="Language", font=(FONT, 40, "italic"))
card_word = canvas.create_text(400, 254, text="Word", font=(FONT, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()



#--- MAINLOOP ---#
window.mainloop()


