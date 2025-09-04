# database_frontend.py
import tkinter as tk
from tkinter import messagebox

from PersonDAO import PersonDAO

main_window = tk.Tk()
main_window.title("Database Frontend GUI")
main_window.geometry("600x400")

dao = PersonDAO()
users = dao.get_all()

def on_click():
    messagebox.showinfo("Information", "You clicked the button")

button = tk.Button(main_window, text="Press Me", command=on_click)
button.place(x=10, y=20)

list_box = tk.Listbox(main_window, height=10)
list_box.place(x=10, y=50)

def on_select(evt):
    selection = list_box.curselection()
    if selection:
        index = selection[0]
        name = list_box.get(index)
        print (name)


list_box.bind("<<ListboxSelect>>", on_select)

for user in users:
    list_box.insert(tk.END, user.name)

main_window.mainloop()


