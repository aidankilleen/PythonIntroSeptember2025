# gui_introduction.py
import tkinter as tk
from tkinter import messagebox

main_window = tk.Tk()
main_window.title("Python GUI")
main_window.geometry("600x400")

def on_click():
    messagebox.showinfo("Information", "You clicked the button")

button = tk.Button(main_window, text="Press Me", command=on_click)
button.place(x=10, y=20)

list_box = tk.Listbox(main_window, height=10)
list_box.place(x=10, y=50)

names = ["Alice", "Bob", "Carol", "Dan"]
for name in names:
    list_box.insert(tk.END, name)

main_window.mainloop()


