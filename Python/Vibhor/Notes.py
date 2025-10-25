import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = "notes.json"

def load_notes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(DATA_FILE, "w") as f:
        json.dump(notes, f, indent=4)

class NotesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Notes App")
        self.geometry("400x400")
        
        self.notes = load_notes()

        # Search Bar
        search_frame = tk.Frame(self)
        search_frame.pack(fill=tk.X, pady=5)
        tk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        search_entry.bind("<KeyRelease>", lambda e: self.show_notes())

        # Listbox for notes
        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Buttons
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Add", command=self.add_note).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Edit", command=self.edit_note).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete_note).pack(side=tk.LEFT, padx=5)

        self.show_notes()

    def show_notes(self):
        self.listbox.delete(0, tk.END)
        search_term = self.search_var.get().lower()
        for note in self.notes:
            if search_term in note.lower():
                self.listbox.insert(tk.END, note)

    def add_note(self):
        text = simpledialog.askstring("Add Note", "Enter your note:")
        if text:
            self.notes.append(text)
            save_notes(self.notes)
            self.show_notes()

    def edit_note(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Select a note to edit")
            return
        index = selected[0]
        old_text = self.listbox.get(index)
        new_text = simpledialog.askstring("Edit Note", "Edit your note:", initialvalue=old_text)
        if new_text:
            self.notes[self.notes.index(old_text)] = new_text
            save_notes(self.notes)
            self.show_notes()

    def delete_note(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Select a note to delete")
            return
        note = self.listbox.get(selected[0])
        self.notes.remove(note)
        save_notes(self.notes)
        self.show_notes()

if __name__ == "__main__":
    app = NotesApp()
    app.mainloop()