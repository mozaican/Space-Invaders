import turtle


class Screen(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)

        # create screen
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.title("Space Invaders")

        # create border
        self.speed(0)
        self.color("white")
        self.penup()
        self.setposition(-300, -300)
        self.pendown()
        self.pensize(3)

        # draw border
        for side in range(4):
            self.fd(600)
            self.lt(90)
        self.hideturtle()


class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)

        # create player
        self.penup()
        self.color("red")
        self.shape("triangle")
        self.speed(0)
        self.setposition(0, -255)
        self.setheading(90)
        self.player_speed = 15

    # move player left and right
    def move_left(self):
        x = self.xcor()
        x -= self.player_speed
        if x < -280:
            x = -280
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        x += self.player_speed
        if x > 280:
            x = 280
        self.setx(x)

    def binding(self):
        self.screen.listen()
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")


if __name__ == "__main__":
    screen = Screen()
    player = Player()
    player.binding()
    turtle.done()
