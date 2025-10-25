import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Ms Paint")
root.geometry("800x600")

brush_color = "black"
brush_size = 6

canvas = tk.Canvas(root, bg='white', width=800, height=500)
canvas.pack()

def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1,y1,x2,y2, fill=brush_color, outline=brush_color)
    
canvas.bind("<B1-Motion>", paint)

def choose_color():
    global brush_color
    color = colorchooser.askcolor()[1]
    if color:
        brush_color = color
        
def change_size(size):
    global brush_size
    brush_size = int(size)
    
def clear_canvas():
    canvas.delete("all")
    
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Button(control_frame, text="Choose Color", command=choose_color).grid(row=0,column=0,padx=10)
tk.Button(control_frame, text="Clear",command=clear_canvas).grid(row=0,column=1,padx=10)
tk.Button(control_frame, text="Brush Size: ").grid(row=0, column=2, padx=10)
size_slider = tk.Scale(control_frame, from_=1, to=40, orient=tk.HORIZONTAL, command=change_size)
size_slider.set(6)
size_slider.grid(row=0,column=3)

root.mainloop()