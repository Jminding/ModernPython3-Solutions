import turtle

t = turtle.Turtle()
t.speed(2)

for i in range(4):#square
    t.forward(100)
    t.left(90)

t.circle(50)#circle


t.left(120)#triangle
t.forward(110)
t.left(120)
t.forward(110)
t.left(120)
t.forward(110)
turtle.done()
