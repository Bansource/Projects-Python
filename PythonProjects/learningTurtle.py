import turtle               # allows us to use the turtle library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex
alex.forward(150)           # tell alex to move forward by 150 units
alex.left(90)               # turn by 90 degrees
alex.forward(75)            # complete the second side of a rectangle

wn.bgcolor("maroon")        # set the window background color

alex = turtle.Turtle()
alex.color("goldenrod")              # make tess red
alex.pensize(3)                 # set the width of her pen

wn.exitonclick()            # wait for a user click on the canvas

