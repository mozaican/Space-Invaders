import turtle


# screen
class Screen(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.title("Space Invaders")


# border
class Border(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.color("white")
        self.penup()
        self.setposition(-300, -300)
        self.pendown()
        self.pensize(3)

    def draw(self):
        for side in range(4):
            self.fd(600)
            self.lt(90)
        self.hideturtle()


# player
class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.color("red")
        self.shape("triangle")
        self.speed(0)
        self.setposition(0, -255)
        self.setheading(90)


if __name__ == "__main__":
    screen = Screen()
    border = Border()
    border.draw()
    player = Player()
    delay = input("Press q to quit the program")
