import random

BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
from tkinter import messagebox
from random import randint
import pandas


window = Tk()
window.config(padx= 50, pady= 50, bg=BACKGROUND_COLOR)


data = pandas.read_csv("./data/french_words.csv")


right_list = []
right_list_idx = []


def new_word():
    loop_on = True
    while loop_on:
        if len(right_list) <3:
            canvas_card()
            print(right_list_idx)
            loop_on = False
        else:
            messagebox.showinfo("에러", "끝났어")
            loop_on = False



# -------------------------UI SETUP -------------  #
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
canvas = Canvas(height=562, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
canvas.create_image(400, 263, image = card_front)



# 버튼
wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")
x_button = Button(image= wrong_image, command=new_word)
y_button = Button(image= right_image, command=new_word)
x_button.grid(row=1,column=0)
y_button.grid(row=1,column=1)

def canvas_card():
    all_data = data.to_dict(orient='records')
    chosen_word = random.choice(all_data)

    if chosen_word not in right_list:
        canvas.delete("all")
        canvas.create_image(400, 263, image=card_front)
        print(chosen_word)
        print(all_data.index(chosen_word))
        canvas.create_text((400,150), text="Franch", font=("Arial", 35, "italic"), fill="black")
        canvas.create_text((400,263), text=chosen_word['French'], font=("Arial", 35, "bold"), fill="black")
        window.after(3000, lambda: canvas.delete("all"))
        window.after(3000, lambda :canvas.create_image(400, 263, image = card_back))
        window.after(3000,
                     lambda: canvas.create_text((400, 150), text="English", font=("Arial", 35, "italic"),
                                                fill="white"))
        window.after(3000,
                     lambda: canvas.create_text((400, 263), text=chosen_word['English'], font=("Arial", 35, "bold"),
                                                fill="white"))
        right_list.append(chosen_word)
        right_list_idx.append(all_data.index(chosen_word))

canvas_card()

window.mainloop()