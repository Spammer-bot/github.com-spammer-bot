import turtle

colors = ['red', 'orange', 'blue', 'violet', 'green', 'yellow']
vibhor = turtle.Turtle()
vibhor.speed(3)
sides = 10
angle = 360 / sides
length = 100
for i in range(10):
    vibhor.color(colors[i % 6])
    vibhor.forward(100)
    vibhor.right(36)
turtle.done()