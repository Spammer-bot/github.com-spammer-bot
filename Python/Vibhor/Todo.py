import tkinter as tk
from tkinter import messagebox
import json

DATA_FILE = "notes.json"

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        return json.load(f)
    return []

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.config(bg="#1e1e1e")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):

        heading = tk.Label(self.root, text="📝 To-Do List", font=("Helvetica", 20, "bold"), bg="#1e1e1e", fg="white")       
        heading.pack(pady=10)

        self.task_entry = tk.Entry(self.root, font=("Arial", 14))
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)

        add_btn = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Arial", 12))
        add_btn.pack(pady=5)

        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=10, padx=20, fill=tk.X, expand=True)

        self.canvas = tk.Canvas(self.task_frame, bg="#2e2e2e")
        self.scrollbar = tk.Scrollbar(self.task_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#2e2e2e")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def add_task(self):
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Input Error", "Please enter a task.")
            return

        var = tk.IntVar()
        check = tk.Checkbutton(self.scrollable_frame, text=task, variable=var, onvalue=1, offvalue=0,
                               bg="#2e2e2e", fg="white", selectcolor="#2e2e2e", font=("Arial", 12), anchor="w", padx=10, pady=5)
        check.pack(fill=tk.X, anchor="w")

        delete_btn = tk.Button(self.scrollable_frame, text="Delete", command=lambda c=check, b=None: self.delete_task(c), bg="red", fg="white", font=("Arial", 10))
        delete_btn.pack(pady=2)

        self.tasks.append((check, var))
        self.task_entry.delete(0, tk.END)

    def delete_task(self, checkbox):
        checkbox.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    app.run()