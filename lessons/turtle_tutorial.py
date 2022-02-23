"""A tutorial on Turtle."""

from turtle import Turtle, colormode, done
colormode(255)

leo: Turtle = Turtle()


leo.color(0, 0, 0)
leo.penup()
leo.goto(45, 60)
leo.pendown()
i = 0

leo.fillcolor(122, 112, 224)

leo.begin_fill()

while i < 2:
    leo.forward(20)
    leo.left(90)
    leo.forward(40)
    leo.left(90)
    i += 1
    
leo.end_fill()

leo.speed(100)
leo.hideturtle()


bob: Turtle = Turtle()

side_length: float = 50


bob.penup()
bob.goto(300, 150)
bob.pendown()
i = 0

bob.speed(100)


bob.fillcolor(199, 253, 255)
bob.begin_fill()

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(122)
    i = i + 1
    side_length = side_length * 0.97


bob.end_fill()

done()