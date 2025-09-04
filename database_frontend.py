# database_frontend.py
import tkinter as tk
from tkinter import messagebox

from PersonDAO import PersonDAO

id_map = {}

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

selected_user = None


def on_select(evt):
    global selected_user
    selection = list_box.curselection()
    if selection:
        index = selection[0]
        selected_user = id_map[index]
        print (selected_user)

def on_delete():
    global selected_user
    if selected_user != None:
        answer = messagebox.askyesno("Confirmation", "Are you suer?")

        if answer:
            dao.delete(selected_user.id)

            index = list_box.curselection()[0]
            list_box.delete(index)

delete_button = tk.Button(main_window, text="Delete", command=on_delete)
delete_button.place(x=160, y=60)


list_box.bind("<<ListboxSelect>>", on_select)

for index, user in enumerate(users):
    id_map[index] = user
    list_box.insert(tk.END, user.name)

main_window.mainloop()


