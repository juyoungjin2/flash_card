BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

window = Tk()
window.config(padx= 50, pady= 50, bg=BACKGROUND_COLOR)


card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")

h = card_back.height()
w = card_back.width()
canvas = Canvas(height=h, width=w, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
card_f = canvas.create_image(w/2, h/2, image = card_front)




def image_back():
   canvas.itemconfig(card_f,image=card_back)
def image_front():
   canvas.itemconfig(card_f,image=card_front)


def change_img():
    canvas.delete("all")
    PhotoImage(file="./images/card_front.png")
    canvas.create_image(w/2, h/2, image = card_front)


wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")
x_button = Button(image= wrong_image, command=image_back)
y_button = Button(image= right_image, command=image_front)
x_button.grid(row=1,column=0)
y_button.grid(row=1,column=1)

window.mainloop()