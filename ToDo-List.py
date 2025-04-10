import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

# Task Functions
tasks = []

def load_tasks():
    global tasks
    if os.path.exists("tasks.json"):
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = []
            messagebox.showerror("Error", "tasks.json is corrupted. Starting with an empty list.")
    update_listbox()

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["done"] else "❌"
        listbox.insert(tk.END, f"{status} {task['task']}")

def add_task():
    task_text = simpledialog.askstring("Add Task", "Enter your task:")
    if task_text:
        tasks.append({"task": task_text, "done": False})
        update_listbox()
        save_tasks()

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        removed = tasks.pop(index)
        update_listbox()
        save_tasks()
        messagebox.showinfo("Deleted", f"Task '{removed['task']}' deleted.")
    else:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = True
        update_listbox()
        save_tasks()
        messagebox.showinfo("Done", f"Task '{tasks[index]['task']}' marked as done.")
    else:
        messagebox.showwarning("No Selection", "Please select a task to mark as done.")

# GUI Setup
root = tk.Tk()
root.geometry("700x780")
root.title("📝 ToDo List App") 
root.configure(bg="#FAFAD2") 

# Header Label
label = tk.Label(
    root,
    text="📝 My ToDo List",
    font=("Arial", 18, "bold"),
    fg="black",
    bg="#FAFAD2",
    pady=10
)
label.pack()

# Task Listbox
listbox = tk.Listbox(
    root,
    width=40,
    height=10,
    font=("Arial", 12),
    selectbackground="#FFFFFF",
    selectforeground="#FAFAD2", 
    bg="black",
    fg="#FFFFFF"
)
listbox.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="")
btn_frame.pack(pady=10)

add_btn = tk.Button(
    btn_frame,
    text="➕ Add Task",
    width=12,
    command=add_task,
    bg="#27ae60",
    fg="black",
    activebackground="#27ae60",
    font=("Arial", 10, "bold")
)
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(
    btn_frame,
    text="🗑 Delete Task",
    width=12,
    command=delete_task,
    bg="#e74c3c",
    fg="black"
)
delete_btn.grid(row=0, column=1, padx=5)

done_btn = tk.Button(
    btn_frame,
    text="✅ Mark as Done",
    width=12,
    command=mark_done,
    bg="#0000FF",
    fg="black"
)
done_btn.grid(row=0, column=2, padx=5)

# Load tasks from file at start
load_tasks()

# Run the app
root.mainloop()
