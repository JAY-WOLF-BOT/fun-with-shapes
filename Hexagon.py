import turtle

turtle.Screen().bgcolor("black")

Sc = turtle.Screen()
Sc.setup(500,500)

draw = turtle.Turtle()
draw.color("white")

#draw.forward(100)
#draw.left(60)
#draw.forward(100)
#draw.left(60)
#draw.forward(100)
#draw.left(60)
#draw.forward(100)
#draw.left(60)
#draw.forward(100)
#draw.left(60)
#draw.forward(100)

for x in range(6):
    draw.forward(100)
    draw.left(60)
draw.done()
