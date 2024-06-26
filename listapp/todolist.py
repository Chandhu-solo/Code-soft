import tkinter as tk
from tkinter import messagebox
from tkinter import font
from tkinter import PhotoImage

# File to store tasks
TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from the file."""
    tasks = []
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task():
    """Add a task to the list."""
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_task():
    """Remove the selected task from the list."""
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
        del tasks[selected_index]
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

def update_task_listbox():
    """Update the task listbox with current tasks."""
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def on_closing():
    """Save tasks and close the application."""
    save_tasks(tasks)
    root.destroy()

# Load tasks from file
tasks = load_tasks()

# Create the main window
root = tk.Tk()
root.title("To-Do List App")
root.state('zoomed')  # Maximize the window

# Define custom fonts and colors
header_font = font.Font(family='Helvetica', size=16, weight='bold')
task_font = font.Font(family='Helvetica', size=12)
bg_color = "#1E3D58"
button_color = "#4CAF50"
button_text_color = "#FFFFFF"
entry_bg_color = "#FFFFFF"
entry_fg_color = "#000000"
listbox_bg_color = "#F0F0F0"
listbox_fg_color = "#000000"
listbox_select_bg = "#000000"
listbox_select_fg = "#FFFFFF"

# Set window background color
root.configure(bg=bg_color)

# Load logo
logo = PhotoImage(file="logo.png")  # Ensure this is a transparent PNG
small_logo = logo.subsample(2, 2)  # Create a smaller version of the logo

# Create and place logo on the left side
logo_label = tk.Label(root, image=logo, bg=bg_color)
logo_label.grid(row=0, column=0, rowspan=3, padx=20, pady=20)

# Create and place a small logo on the right side
small_logo_label = tk.Label(root, image=small_logo, bg=bg_color)
small_logo_label.grid(row=0, column=2, padx=20, pady=20)

# Create and place widgets
header = tk.Label(root, text="To-Do List App", font=header_font, bg=bg_color, fg=button_text_color)
header.grid(row=0, column=1, pady=10)

frame = tk.Frame(root, bg=bg_color)
frame.grid(row=1, column=1, padx=20, pady=10, sticky='w')

task_entry = tk.Entry(frame, width=30, font=task_font, bg=entry_bg_color, fg=entry_fg_color, insertbackground=entry_fg_color)
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(frame, text="Add Task", command=add_task, bg=button_color, fg=button_text_color, font=task_font)
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_button = tk.Button(frame, text="Remove Task", command=remove_task, bg=button_color, fg=button_text_color, font=task_font)
remove_button.grid(row=1, column=1, padx=10, pady=10)

list_frame = tk.Frame(root, bg=bg_color)
list_frame.grid(row=2, column=1, padx=20, pady=10)

task_listbox = tk.Listbox(list_frame, width=50, height=20, font=task_font, bg=listbox_bg_color, fg=listbox_fg_color, selectbackground=listbox_select_bg, selectforeground=listbox_select_fg, highlightbackground=bg_color, bd=0)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Populate the listbox with tasks
update_task_listbox()

# Handle window closing event
root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the application
root.mainloop()
