# Compulsory Task
# Creating a temperature covert app
import tkinter as tk
from tkinter import LabelFrame, Button, Entry, END, messagebox

# adding TK and giving size of body and title

gui = tk.Tk()

gui.title("Temperature Convertor")
gui.geometry("720x450")
gui.config(bg="brown")

# adding text labels
celsius_label_frame = LabelFrame(gui, text="Celsius to Fahrenheit")
fahrenheit_label_frame = LabelFrame(gui, text="Fahrenheit to Celsius")
# adding positioning and size
celsius_entry = Entry(celsius_label_frame, width=10, state="readonly")
celsius_entry.place(x=50, y=30)
# adding text labels
fahrenheit_entry = Entry(fahrenheit_label_frame, width=10, state="readonly")
fahrenheit_entry.place(x=50, y=30)
# adding positioning and size
celsius_label_frame.place(x=60, y=70, height=110, width=190)
fahrenheit_label_frame.place(x=470, y=70, height=110, width=190)

# defining the temperature conversion


def temp_con():
    try:
        if celsius_entry['state'] == "normal" and celsius_entry.get() != "":
            to_fahrenheit = float(celsius_entry.get()) * 9 / 5 + 32
            results_entry.delete(0, END)
            results_entry.insert(0, to_fahrenheit)

    except:
              messagebox.showinfo("ERROR", "Must be numbers")
    try:
        if fahrenheit_entry['state'] == "normal" and fahrenheit_entry.get() != "":
             to_celsius = (float(fahrenheit_entry.get()) - 32) * 5 / 9
             results_entry.delete(0, END)
             results_entry.insert (0, to_celsius)

    except:
        messagebox.showinfo("ERROR", "Must be numbers")


# defining the clear button

def clear():
    celsius_entry.delete(0, END)
    fahrenheit_entry.delete(0, END)
    results_entry.delete(0, END)

# defining entry values of temperature


def celc_ent():

        if celsius_entry['state'] == "normal":
            celsius_entry.config(state="disabled")

        else:
            celsius_entry.config(state="normal")
            fahrenheit_entry.config(state="disabled")


def farh_ent():
    if fahrenheit_entry['state'] == "normal":
        fahrenheit_entry.config(state="disabled")
    else:
        fahrenheit_entry.config(state="normal")
        celsius_entry.config(state="disabled")

# defining exit button

def exit():
    msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit")
    if msg_box == "yes":
        gui.destroy()
    else:
        messagebox.showinfo("Returning", "You will now return ")

# activating buttons


activate_celsius_btn = Button(gui, text="Activate C to F", borderwidth=6, fg="red", font=("Consolas 15 bold"), command=celc_ent, bg="yellow")
activate_celsius_btn.place(x=50, y=190)


activate_fahrenheit_btn = Button(gui, text="Activate F to C", command=farh_ent, borderwidth=6, fg="red", font=("Consolas 15 bold"),  bg="yellow")
activate_fahrenheit_btn.place(x=460, y=190)
# convert buttons

convert_button = Button(gui, text="Convert", command=temp_con, borderwidth=6, fg="red", font=("Consolas 15 bold"),  bg="yellow")
convert_button.place(x=80, y=280)

# results

results_entry = Entry(gui, bg="yellow", width=10)
results_entry.place(x=220, y=290, height=29.5)

# giving clear button a command

clear_button = Button(gui, text="Clear", command=clear, borderwidth=6, fg="red", font=("Consolas 15 bold"),  bg="yellow")
clear_button.place(x=350, y=220)

# giving exit button a command

exit_button = Button(gui, text="Exit", command=exit, borderwidth=6, fg="red", font=("Consolas 15 bold"),  bg="yellow")
exit_button.place(x=350, y=280)

# adding a mainloop for it to run
gui.mainloop()