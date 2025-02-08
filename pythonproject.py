import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Create widgets
task_entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
clear_button = tk.Button(root, text="Clear All", command=clear_tasks)
tasks_listbox = tk.Listbox(root, width=50, height=15)

# Place widgets on window
task_entry.pack(pady=10)
add_button.pack(pady=5)
tasks_listbox.pack(pady=10)
remove_button.pack(pady=5)
clear_button.pack(pady=5)

# Run the main loop
root.mainloop()
