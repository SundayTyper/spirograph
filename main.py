import turtle

# test to draw a square

end = turtle.pos()

turtle.forward(10)
turtle.right(1)

while turtle.pos() != end:
    turtle.forward(10)
    turtle.right(1)

turtle.mainloop()