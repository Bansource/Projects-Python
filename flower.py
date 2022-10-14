import turtle

wn = turtle.Screen()
wn.bgcolor("black")

flower = turtle.Turtle()
flower.pensize(1)
flower.pencolor('crimson')

flower.penup()
flower.goto(0,200)
flower.pendown()
"""
def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)
"""
flower.speed(0)
def drawCircle():
    for i in range(300):
        flower.circle(190-i, 90)
        flower.left(90)
        flower.circle(190 - i, 90)
        flower.left(18)
    # The leaves
    flower.penup()              
    flower.goto(0,200)
    flower.pendown()

    flower.fillcolor("green")
    flower.begin_fill()
    flower.right(63)
    flower.forward(300)
    flower.left(90)
    flower.forward(45)

    flower.circle(-80, 90)
    flower.right(90)
    flower.circle(-80,90)

    flower.right(135)
    flower.forward(60)
    flower.forward(-60)
    
    flower.right(135)
    flower.forward(45)





drawCircle()

wn.exitonclick()


