import turtle
turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(width=300, height=400)
t = turtle.Turtle()
t.color("black")
n=4
while n > 0:
    t.forward(100)
    t.left(90)
    n = n - 1

turtle.done()