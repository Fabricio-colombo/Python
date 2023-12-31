import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(2)

for _ in range(5):
    t.color("yellow")
    t.forward(100)
    t.right(144)

turtle.exitonclick()
