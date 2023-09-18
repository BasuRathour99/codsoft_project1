import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

app = tk.Tk()
app.title("To-Do List")

task_entry = tk.Entry(app, width=40)
add_button = tk.Button(app, text="Add Task", width=20, command=add_task)
delete_button = tk.Button(app, text="Delete Task", width=20, command=delete_task)
task_listbox = tk.Listbox(app, width=50)

task_entry.pack(pady=10)
add_button.pack()
delete_button.pack()
task_listbox.pack(pady=10)

app.mainloop()
