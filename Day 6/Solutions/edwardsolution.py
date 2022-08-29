import turtle

# drawing a square
square = turtle.Turtle()

#moves the pen to the side for space
square.penup()
square.forward(100)

# uses a for loop to repeat drawing "one side" 4 times
square.pendown()
for x in range(4):
    square.forward(100)
    square.left(90)

#drawing a triangle (equilateral)
triangle = turtle.Turtle()

for x in range(3):
    triangle.left(180 - 60)
    triangle.forward(130)


#drawing a cricle
circle = turtle.Turtle()

#adjusts pen position to draw circle
circle.penup()
circle.right(90)
circle.forward(100)
circle.pendown()

circle.circle(70)



turtle.done()