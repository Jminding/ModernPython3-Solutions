import turtle

def square(t):
    for _ in range(4):
        t.forward(100)
        t.left(90)

def triangle(t):
    for _ in range(3):
        t.forward(100)
        t.left(120)

def circle(t):
    t.circle(50)

def star(t):
    t.left(36)
    for _ in range(5):
        t.forward(100)
        t.left(180 - 36)

t = turtle.Turtle()

turtle.done()
