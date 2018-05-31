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


class Enemy(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)

        # create enemy
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.setposition(-200, 250)
        self.enemy_speed = 2

    # move enemy back and down
    def move(self):
        while True:
            x = self.xcor()
            x += self.enemy_speed
            self.setx(x)

            if self.xcor() > 280:
                y = self.ycor()
                y -= 30
                self.enemy_speed *= -1
                self.sety(y)

            if self.xcor() < -280:
                y = self.ycor()
                y -= 30
                self.enemy_speed *= -1
                self.sety(y)


class Weapon(Player):

    def __init__(self):
        turtle.Turtle.__init__(self)
        Player.__init__(self)

        # create the bullet
        self.color("yellow")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(0.5, 0.5)
        self.hideturtle()
        self.bullet_speed = 20
        self.bullet_state = "ready"

    # make the bullet appear above the player
    def fire_bullet(self):
        if self.bullet_state == "ready":
            self.bullet_state = "fire"
            x = player.xcor()
            y = player.ycor() + 10
            self.setposition(x, y)
            self.showturtle()

    # shoot the alien
    def shoot(self):
        while True:
            y = self.ycor()
            y += self.bullet_speed
            self.sety(y)

            if self.ycor() > 275:
                self.hideturtle()
                self.bullet_state = "ready"

    def binding(self):
        self.screen.onkey(self.fire_bullet, "space")


if __name__ == "__main__":
    screen = Screen()
    player = Player()
    player.binding()
    weapon = Weapon()
    weapon.binding()
    weapon.shoot()
    enemy = Enemy()
    enemy.move()
    turtle.done()
