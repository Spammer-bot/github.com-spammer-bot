import tkinter as tk
from tkinter import messagebox

class Vibhor:
    def __init__(self, root):
        self.root = root
        self.root.title("Vibhor")
        self.root.geometry("1920x1080")
        self.root.config(bg="#1d0c0c")

        self.friends = []

        self.add_friends()

    def add_friends(self):

        heading = tk.Label(self.root, text="My name is Vibhor.", font=("Ariel", 20, "bold"), bg="#3e3e3e", fg="white" )
        heading.pack(pady=10)

        heading = tk.Label(self.root, text="I am 13 years old.", font=("Ariel", 14, "bold"), bg="#3e3e3e", fg="white" )
        heading.pack(pady=10)

        heading = tk.Label(self.root, text="I like to play football.", font=("Ariel", 14, "bold"), bg="#3e3e3e", fg="white" )
        heading.pack(pady=10)

        heading = tk.Label(self.root, text="My hobby is to play and do gaming.", font=("Ariel", 14, "bold"), bg="#3e3e3e", fg="white" )
        heading.pack(pady=10)

        self.friends_entry = tk.Entry(self.root, font=("Arial", 14))
        self.friends_entry.pack(pady=10, padx=20, fill=tk.X)

        add_butn = tk.Button(self.root, text="Add Friends", command=self.add_friends, bg="#4e4e4e", fg="white", font=("Arial", 20))
        add_butn.pack(pady=5)

        self.friend_frame = tk.Frame(self.root)
        self.friend_frame.pack(pady=10, padx=20, fill=tk.X, expand=True)

        self.canvas = tk.Canvas(self.friend_frame, bg="#5e5e5e")
        self.scrollbar = tk.Scrollbar(self.friend_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#6e6e6e")
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

    def add_friends2(self):
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Input Error", "Please enter a friend")
        
        var = tk.IntVar()
        check = tk.Checkbutton(self.scrollable_frame, text="friend", variable=var, onvalue=1, offvalue=0, bg="#2e2e2e", fg="white", selectcolor="#9e9e9e", font=("Arial", 12), anchor="w", padx=10, pady=5)
        check.pack(fill=tk.X, anchor="w")

        delete_friend_butn = tk.Button(self.scrollable_frame, text="Delete Friend", command=lambda c=check, b=None: self.delete_task(c), bg="red", fg="white", font=("Arial", 10))
        delete_friend_butn.pack(pady=2)

        self.friends.append((check, var))
        self.friends_entry.delete(0, tk.END)

    def delete_friend(self, checkbox):
        checkbox.destroy()

    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    app = Vibhor(root)
    app.run()