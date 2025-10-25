import tkinter as tk
import random

WIDTH = 600
HEIGHT = 400
SEG_SIZE = 20
UPDATE_DELAY = 100

DIRECTIONS = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0)
}

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Trophy Snake Game")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.car = [(SEG_SIZE*5, SEG_SIZE*5), (SEG_SIZE*4, SEG_SIZE*5), (SEG_SIZE*3, SEG_SIZE*5)]
        self.direction = "Right"

        self.draw_car()

        self.trophy = None
        self.spawn_trophy()

        self.score = 0
        self.score_text = self.canvas.create_text(50, 10, fill="white", font="Arial 14 bold", text=f"Score: {self.score}")

        self.root.bind("<KeyPress>", self.change_direction)
        self.after_id = None
        self.move_car()

    def draw_car(self):
        self.canvas.delete("car")
        for i, (x, y) in enumerate(self.car):
            color = "red" if i == 0 else "orange"
            self.canvas.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill=color, tags="car")

    def spawn_trophy(self):
        while True:
            x = random.randint(0, (WIDTH - SEG_SIZE) // SEG_SIZE) * SEG_SIZE
            y = random.randint(0, (HEIGHT - SEG_SIZE) // SEG_SIZE) * SEG_SIZE
            if (x, y) not in self.car:
                break
        if self.trophy:
            self.canvas.delete(self.trophy)
        self.trophy = self.canvas.create_oval(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="gold", tags="trophy")
        self.trophy_pos = (x, y)

    def move_car(self):
        dx, dy = DIRECTIONS[self.direction]
        head_x, head_y = self.car[0]
        new_head = (head_x + dx*SEG_SIZE, head_y + dy*SEG_SIZE)

        if (
            new_head in self.car or
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT
        ):
            self.game_over()
            return

        self.car.insert(0, new_head)

        if new_head == self.trophy_pos:
            self.score += 1
            self.canvas.itemconfigure(self.score_text, text=f"Score: {self.score}")
            self.spawn_trophy()
        else:
            self.car.pop()

        self.draw_car()
        self.after_id = self.root.after(UPDATE_DELAY, self.move_car)

    def change_direction(self, event):
        if event.keysym in DIRECTIONS:
            new_dir = event.keysym
            opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
            if new_dir != opposites.get(self.direction):
                self.direction = new_dir

    def game_over(self):
        self.canvas.create_text(WIDTH//2, HEIGHT//2, fill="white", font="Arial 20 bold", text="GAME OVER")
        self.canvas.create_text(WIDTH//2, HEIGHT//2 + 30, fill="white", font="Arial 14", text=f"Final Score: {self.score}")

    def stop_game(self):
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None

def restart_game():
    global game, root
    try:
        game.stop_game()
    except:
        pass

    root.destroy()
    root = tk.Tk()
    game = SnakeGame(root)

    restart_btn = tk.Button(root, text="Restart", font="Arial 12 bold", bg="lightgray", command=restart_game)
    restart_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)

    restart_btn = tk.Button(root, text="Restart", font="Arial 12 bold", bg="lightgray", command=restart_game)
    restart_btn.pack(pady=10)

    root.mainloop()
