from tkinter import *


def convert_miles_to_km():
    try:
        miles = float(input_entry.get())
        km = miles * 1.60934
        result_label.config(text=f"{km:.2f} Km")
    except ValueError:
        result_label.config(text="Please enter a valid number")


def reset():
    input_entry.delete(0, END)
    result_label.config(text="0 Km")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

input_label = Label(text="Miles", font=("Arial", 14))
input_label.grid(column=0, row=0)

result_label = Label(text="0 Km", font=("Arial", 14, "bold"))
result_label.grid(column=1, row=1)

input_entry = Entry(width=10)
input_entry.grid(column=1, row=0)

convert_button = Button(text="Convert", command=convert_miles_to_km)
convert_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=1, row=2)

window.mainloop()
