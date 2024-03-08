import turtle
wn = turtle.Screen()
wn.bgcolor("maroon")
wn.screensize(1000,750)

t = turtle.Turtle()
u = turtle.Turtle()
v = turtle.Turtle()
w = turtle.Turtle()
x = turtle.Turtle()
y = turtle.Turtle()
y.pensize(6)
y.shape("classic")
y.speed(0)

t.speed(0)
u.speed(0)
v.speed(0)
w.speed(0)
x.speed(0)
u.penup(); u.forward(400); u.left(90); u.forward(200); u.pendown()
v.penup(); v.forward(400); v.right(90); v.forward(200); v.pendown()
w.penup(); w.forward(-400); w.left(90); w.forward(200); w.pendown()
x.penup(); x.forward(-400); x.right(90); x.forward(200); x.pendown()
angle = 90 # 90, 120, 135, 180
for i in range(100):
    j = i*1
    t.circle(i,angle)
    t.penup()
    t.forward(j)
    t.left(210)
    t.pendown()

    u.circle(i,angle)
    u.penup()
    u.forward(j)
    u.left(30)
    u.pendown()

    v.circle(i,angle)
    v.penup()
    v.forward(j)
    v.left(45)
    v.pendown()

    w.circle(i,angle)
    w.penup()
    w.forward(j)
    w.left(150)
    w.pendown()

    x.circle(i,angle)
    x.penup()
    x.forward(j)
    x.left(99)
    x.pendown()

a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
a.speed(0)
b.speed(0)
c.speed(0)


a.shape("circle")
a.pensize(5)


b.shape("arrow")
b.pensize(5)


c.shape("turtle")

a.penup()
b.penup()
c.penup()
for size in range(36):
    for aColor in ["OrangeRed", "DarkGreen", "Navy", "Gold"]:
        c.color(aColor)
        c.forward(235)
        c.stamp()
        c.forward(-235)
        c.left(10)
    
        b.color(aColor)
        b.forward(260)
        b.stamp()
        b.forward(-260)
        b.left(10)

        a.color(aColor)
        a.forward(290)
        a.stamp()
        a.forward(-290)
        a.left(10)



wn.exitonclick()