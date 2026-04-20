import turtle

turtle.screensize(2000, 2000)
t = turtle.Turtle()
t.speed(0)
turtle.tracer(0)

k = 10


t.penup()
t.goto(-600, -600)
t.setheading(90)
t.pendown()


for _ in range(6):
    t.forward(k*71)
    t.right(90)
    t.forward(k*73)
    t.right(90)

t.penup()
t.forward(k*18)
t.right(90)
t.forward(k*22)
t.left(90)

t.pendown()
for _ in range(6):
    t.forward(k*45)
    t.right(90)
    t.forward(k*58)
    t.right(90)


t.penup()
for x in range(-100,90):
    for y in range(-100,90):
        t.goto(x*k, y*k)
        t.dot(3, 'red')

turtle.update()
turtle.done()