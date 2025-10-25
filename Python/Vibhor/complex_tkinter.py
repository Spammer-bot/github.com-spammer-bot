import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser
import sqlite3
import threading
import time
from datetime import datetime

def init_db():
    conn = sqlite3.connect("app_data.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT,
        deadline TEXT,
        status TEXT
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY,
        content TEXT
    )""")
    conn.commit()
    conn.close()
    
class TaskNotesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Personal Task & Notes Manager")
        self.geometry("900x600")
        self.configure(bg="#1e1e2e")

        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="#2e2e3e", foreground="white", fieldbackground="#2e2e3e")
        self.style.map("Treeview", background=[("selected", "#444466")])

        self.create_menu()
        self.create_layout()
        self.create_statusbar()

        self.load_tasks()
        self.load_notes()

        threading.Thread(target=self.update_clock, daemon=True).start()

    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Export Tasks", command=self.export_tasks)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        toolsmenu = tk.Menu(menubar, tearoff=0)
        toolsmenu.add_command(label="Change Theme Color", command=self.change_color)
        menubar.add_cascade(label="Tools", menu=toolsmenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Tkinter Task & Notes Manager\nBy You"))
        menubar.add_cascade(label="Help", menu=helpmenu)

    def create_layout(self):
        paned = ttk.PanedWindow(self, orient="horizontal")
        paned.pack(fill="both", expand=True, pady=5, padx=5)

        task_frame = ttk.Labelframe(paned, text="Tasks")
        paned.add(task_frame, weight=2)

        self.tree = ttk.Treeview(task_frame, columns=("Title", "Deadline", "Status"), show="headings")
        for col in ("Title", "Deadline", "Status"):
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)

        ttk.Button(task_frame, text="Add Task", command=self.add_task_window).pack(side="left", padx=5, pady=5)
        ttk.Button(task_frame, text="Delete Task", command=self.delete_task).pack(side="left", padx=5, pady=5)

        notes_frame = ttk.Labelframe(paned, text="Notes")
        paned.add(notes_frame, weight=1)

        self.text_area = tk.Text(notes_frame, wrap="word", bg="#2e2e3e", fg="white")
        self.text_area.pack(fill="both", expand=True, padx=5, pady=5)
        ttk.Button(notes_frame, text="Save Note", command=self.save_note).pack(pady=5)

    def create_statusbar(self):
        self.status = tk.StringVar()
        self.status.set("Welcome!")
        bar = tk.Label(self, textvariable=self.status, bg="#11111a", fg="white", anchor="w")
        bar.pack(side="bottom", fill="x")

    def load_tasks(self):
        conn = sqlite3.connect("app_data.db")
        c = conn.cursor()
        c.execute("SELECT * FROM tasks")
        rows = c.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=(row[1], row[2], row[3]))
        conn.close()

    def add_task_window(self):
        win = tk.Toplevel(self)
        win.title("Add Task")
        win.geometry("300x200")

        tk.Label(win, text="Task Title:").pack(pady=5)
        title_entry = tk.Entry(win)
        title_entry.pack(pady=5)

        tk.Label(win, text="Deadline (YYYY-MM-DD):").pack(pady=5)
        deadline_entry = tk.Entry(win)
        deadline_entry.pack(pady=5)

        def save():
            title = title_entry.get()
            deadline = deadline_entry.get()
            if not title:
                messagebox.showerror("Error", "Task Title required")
                return
            conn = sqlite3.connect("app_data.db")
            c = conn.cursor()
            c.execute("INSERT INTO tasks (title, deadline, status) VALUES (?, ?, ?)", (title, deadline, "Pending"))
            conn.commit()
            conn.close()
            self.tree.insert("", "end", values=(title, deadline, "Pending"))
            win.destroy()
            self.status.set("Task Added!")

        ttk.Button(win, text="Save", command=save).pack(pady=10)

    def delete_task(self):
        selected = self.tree.selection()
        if not selected:
            return
        item = self.tree.item(selected[0])
        title = item["values"][0]
        conn = sqlite3.connect("app_data.db")
        c = conn.cursor()
        c.execute("DELETE FROM tasks WHERE title=?", (title,))
        conn.commit()
        conn.close()
        self.tree.delete(selected[0])
        self.status.set("Task Deleted!")

    def export_tasks(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files","*.txt")])
        if not file:
            return
        with open(file, "w") as f:
            for child in self.tree.get_children():
                f.write(str(self.tree.item(child)["values"]) + "\n")
        self.status.set("Tasks Exported!")

    def load_notes(self):
        conn = sqlite3.connect("app_data.db")
        c = conn.cursor()
        c.execute("SELECT * FROM notes")
        rows = c.fetchall()
        if rows:
            self.text_area.insert("1.0", rows[-1][1])
        conn.close()

    def save_note(self):
        content = self.text_area.get("1.0", "end-1c")
        conn = sqlite3.connect("app_data.db")
        c = conn.cursor()
        c.execute("INSERT INTO notes (content) VALUES (?)", (content,))
        conn.commit()
        conn.close()
        self.status.set("Note Saved!")

    def change_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.configure(bg=color)

    def update_clock(self):
        while True:
            now = datetime.now().strftime("%H:%M:%S")
            self.status.set(f"Time: {now}")
            time.sleep(1)

if __name__ == "__main__":
    init_db()
    app = TaskNotesApp()
    app.mainloop()