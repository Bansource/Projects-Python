# Pong game turtle

# Creating the base
import turtle

wn = turtle.Screen()
wn.title("Pong by @Bansource")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)                               # stops the window from updating, to manually update. Lets the game speed up.

# Score
score_a = 0
score_b = 0


# Paddle A left side
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)        # stretches the width by 5 * 20. 
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B right side
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)        # stretches the width by 5 * 20. 
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white") 
ball.penup()
ball.goto(0,0)

# Pen ( The written score)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# separte ball movement into a y and x movement
ball.dx = .1                                            # d means delta,Change. .1 means it moves by .1 pixels
ball.dy = -.1

# Function to move the paddles
def paddle_a_up():
    y = paddle_a.ycor()                                 # y.cor returns the y coordinate
    y += 20                                             # adds 20 pixels to the y coordinate
    paddle_a.sety(y)                                    # sets y to the new y 

def paddle_a_down():
    y = paddle_a.ycor()                                 # y.cor returns the y coordinate
    y -= 20                                             # subtracts 20 pixels to the y coordinate
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()                                 # y.cor returns the y coordinate
    y += 20                                             # adds 20 pixels to the y coordinate
    paddle_b.sety(y)                                    # sets y to the new y 

def paddle_b_down():
    y = paddle_b.ycor()                                 # y.cor returns the y coordinate
    y -= 20                                             # subtracts 20 pixels to the y coordinate
    paddle_b.sety(y)


# Keyboard binding
wn.listen()                                             # tells it to listen for keyboard input
wn.onkeypress(paddle_a_up, "w")                         # when the user presses lower case "w" call the function paddle up line 57. 
wn.onkeypress(paddle_a_down, "s")                       # when the user presses lower case "s" call the function paddle down line 62.
wn.onkeypress(paddle_b_up, "Up")                         # when the user presses lower case "Up arrow" call the function paddle up line 68. 
wn.onkeypress(paddle_b_down, "Down")                      # when the user presses lower case "Down arrow" call the function paddle down line 73.
# Main game loop
while True:
    wn.update()                             # every time the loop runs, the screen is updated.


    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking. bouncing off.
    if ball.ycor() > 290: # top of screen                           
        ball.sety(290)                               
        ball.dy *= -1                               # reverses the direction of the ball
    
    if ball.ycor() < -290: # bottom of screen                        
        ball.sety(-290)                               
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

