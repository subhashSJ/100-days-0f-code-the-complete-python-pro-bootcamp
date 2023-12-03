from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
    to_learn = df.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title_text, text=f"English", fill="white")
    canvas.itemconfig(
        word_text, text=f"{current_word['English']}", fill="white")


def next_card():
    global timer, current_word
    window.after_cancel(timer)

    current_word = choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title_text, text=f"French", fill="black")
    canvas.itemconfig(
        word_text, text=f"{current_word['French']}", fill="black")
    timer = window.after(3000, flip_card)


def known_words():
    to_learn.remove(current_word)
    to_learn_df = pd.DataFrame(to_learn)
    to_learn_df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def unknown_words():
    next_card()


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

canvas_image = canvas.create_image(400, 263)
title_text = canvas.create_text(400, 150, text="",
                                font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="",
                               font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=unknown_words)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(
    image=right_image, highlightthickness=0, command=known_words)
right_button.grid(row=1, column=1)

timer = window.after(3000, flip_card)
next_card()

window.mainloop()
