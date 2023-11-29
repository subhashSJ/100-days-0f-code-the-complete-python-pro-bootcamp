from tkinter import *


def calculate():
    kilometer_result_label.config(text=f"{1.609 * float(input.get())}")


# Creating a new window and configurations
window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=350, height=200)
window.config(padx=80, pady=80)

input = Entry(width=15)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text=f"0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
