import turtle

t = turtle.Turtle()
t.color("magenta")
t.speed(0)

for i in range(36):
    for _ in range(2):
        t.circle(100, 60)
        t.left(120)
    t.left(10)

turtle.done()