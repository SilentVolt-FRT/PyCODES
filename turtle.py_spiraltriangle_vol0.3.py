import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.width(2)
t.speed(20)

col = ('red', 'blue','purple')
for i in range(300):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)

