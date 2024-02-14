import turtle
import turtleWindow

class outerCircle:

    def __init__(self):
        outer = turtle.Turtle()
        outer.speed('fastest')
        outer.up()
        outer.goto(0,500)
        outer.down()
        outer.circle(-500)