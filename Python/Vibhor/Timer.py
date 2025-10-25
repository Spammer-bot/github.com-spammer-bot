import tkinter as tk
from tkinter import messagebox
import time

class SpaceTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Timer")
        self.root.geometry("400x500")   
        self.root.configure(bg='black')
        
        self.timer_running = False
        self.work_min = 25
        self.break_min = 5
        self.remaining = 0
        
        self.create_widgets()
    
    def create_widgets(self):
        self.title = tk.Label(self.root, text="Mission Control", font=("Orbitron",20),bg='black',fg='white')
        self.title.pack(pady=20)
        
        self.timer_label = tk.Label(self.root, text="25:00", font=("DS-Digital", 48), bg="black", fg="lime")
        self.timer_label.pack(pady=10)
        
        self.start_butn = tk.Button(self.root, text="Start",font=('Arial',14),command=self.start_timer)
        self.start_butn.pack(pady=10)
        
        self.reset_btn = tk.Button(self.root, text="Reset", font=("Arial", 14), command=self.reset_timer)
        self.reset_btn.pack(pady=5)
    def start_timer(self):
        if not self.timer_running:
            self.remaining = self.work_min * 60
            self.timer_running = True
            self.count_down()

    def reset_timer(self):
        self.timer_running = False
        self.remaining = 0
        self.timer_label.config(text="25:00")

    def count_down(self):
        if self.remaining > 0 and self.timer_running:
            mins, secs = divmod(self.remaining, 60)
            self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
            self.remaining -= 1
            self.root.after(1000, self.count_down)
        elif self.remaining == 0 and self.timer_running:
            self.timer_running = False
            messagebox.showinfo("Pomodoro Complete!", "Time for a break! 🌖")
            self.timer_label.config(text="05:00")
            self.session_label.config(text="Sessions Completed: 1")

root = tk.Tk()
app = SpaceTimer(root)
root.mainloop()