"""Forest scene using Turtle."""

__author__ = "730475197"


from random import randint
from turtle import Turtle, colormode, done

colormode(255)


def leaves(x: float, y: float, size: float) -> None:
    """Stacked triangles that serves as leaves."""
    triangle: Turtle = Turtle()
    triangle.color(33, 74, 35)
    triangle.penup()
    triangle.goto(x, y)
    triangle.pendown()
    i = 0

    triangle.fillcolor(3, 128, 11)

    triangle.begin_fill()

    while i < 3:
        triangle.forward(size)
        triangle.left(120)
        i += 1
        
    triangle.end_fill()

    triangle.speed(500)
    triangle.hideturtle()


def trunk(x: float, y: float) -> None:
    """Brown rectangle that serves as a trunk."""
    trunk: Turtle = Turtle()
    trunk.color(48, 23, 7)
    trunk.penup()
    trunk.goto(x, y)
    trunk.pendown()
    i = 0

    trunk.fillcolor(87, 34, 2)

    trunk.begin_fill()

    while i < 2:
        trunk.backward(20)
        trunk.left(90)
        trunk.backward(40)
        trunk.left(90)
        i += 1

    trunk.end_fill()
    trunk.speed(100)
    trunk.hideturtle()


def tree(loc_x: int, loc_y: int) -> None:
    """Combine triangle leaves and trunk to make tree."""
    i: int = 0
    size: int = 200
    while i < 3:
        leaves(loc_x, loc_y, size)
        loc_y += 50
        loc_x += 25
        size -= 50
        i += 1
    trunk(loc_x + 35, loc_y - 150)


def main() -> None:
    """The entrypoint of my scene."""
    i: int = 0
    while i < 10:
        tree(randint(-300, 300), randint(-300, 300))
        i += 1


if __name__ == "__main__":
    main()
    done()