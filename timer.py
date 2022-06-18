import tkinter as tk
main_window = tk.Tk()


def on_after():
    a = "hello"
    label_text.configure( text=a)
label_text = tk.Label(main_window, text="hello world")

label_text.grid(column=1, row=1)
label_text.after(3000, on_after) # after 3000 ms call on_after

main_window.mainloop()