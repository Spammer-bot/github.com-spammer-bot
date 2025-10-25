import turtle

colors = ['red', 'orange', 'blue', 'violet', 'green', 'yellow']
vibhor = turtle.Turtle()
vibhor.speed(-10)
for i in range(720):
    vibhor.color(colors[i % 6])
    vibhor.forward(i * 0.5)
    vibhor.left(59)
turtle.done()