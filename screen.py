import turtle

# screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders")

# border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300, -300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()

# player
player = turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -255)
player.setheading(90)

delay = input("Press q to quit the program")
