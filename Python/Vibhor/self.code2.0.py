import tkinter as tk
from tkinter import messagebox

class Vibhor:
        def __init__(self, root):
            self.root = root
            self.root.title("Info_Stealer")
            self.root.geometry("1920x1080")
            self.root.config(bg="#000000")

            self.info = []

            self.create_widgets()

        def create_widgets(self):

            heading = tk.Label(self.root, text="Welcome To Info Stealer", font=("Arial", 20, "bold"), bg="#000000", fg="white")
            heading.pack(pady=10)

            sub_heading = tk.Label(self.root, text="This app steal your info and copy pastes your info to other platforms", font=("Arial", 18), bg="#000000", fg="white")
            sub_heading.pack(pady=10)

            self.name_entry = tk.Entry(self.root, font=("Arial", 14))
            self.name_entry.pack(padx=20, pady=10, fill=tk.X)

            self.age_entry = tk.Entry(self.root, font=("Arial", 14))
            self.age_entry.pack(padx=20, pady=10, fill=tk.X)

            self.address_entry = tk.Entry(self.root, font=("Arial", 14))
            self.address_entry.pack(padx=20, pady=10, fill=tk.X)

            submit_butn = tk.Button(self.root, text="Submit", font=("Arial", 14), command=self.error)
            submit_butn.pack(pady=20)

            self.result_frame = tk.Frame(self.root, bg="#000000")
            self.result_frame.pack(pady=20)

        def error(self):
            name = self.name_entry.get().strip()
            if not name:
                messagebox.showwarning("Input Error", "Please Enter a Name")
                return
            
            age = self.age_entry.get().strip()
            if not age:
                messagebox.showwarning("Input Error", "Please Enter an Age")
                return
            
            address = self.address_entry.get().strip()
            if not age:
                messagebox.showwarning("Input Error", "Please Enter an Address")
                return
            
            for widget in self.result_frame.winfo_children():
                widget.destroy()

            tk.Label(self.result_frame, text=f"This is your Name: {name}", font=("Arial", 14), bg="#000000", fg="white").pack(pady=5)
            
            tk.Label(self.result_frame, text=f"This is your Age: {age}", font=("Arial", 14), bg="#000000", fg="white").pack(pady=5)
            
            tk.Label(self.result_frame, text=f"This is your Address: {address}", font=("Arial", 14), bg="#000000", fg="white").pack(pady=5)

root = tk.Tk()
app = Vibhor(root)
root.mainloop()