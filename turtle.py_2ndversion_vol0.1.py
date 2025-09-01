import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.color("blue")

t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

t.penup()
t.forward(150)
t.pendown()

t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

turtle.done()