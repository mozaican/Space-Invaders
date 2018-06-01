import turtle
import math


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


class Weapon(Player):

    def __init__(self):
        turtle.Turtle.__init__(self)

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

    def is_collision(self, t1, t2):
        distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
        if distance < 15:
            return True
        else:
            return False

    def binding(self):
        self.screen.onkey(self.fire_bullet, "space")


class Game(Enemy, Weapon, Player):

    def __init__(self):
        turtle.Turtle.__init__(self)

    def run(self):
        while True:
            x = enemy.xcor()
            x += enemy.enemy_speed
            enemy.setx(x)

            if enemy.xcor() > 280:
                y = enemy.ycor()
                y -= 30
                enemy.enemy_speed *= -1
                enemy.sety(y)

            if enemy.xcor() < -280:
                y = enemy.ycor()
                y -= 30
                enemy.enemy_speed *= -1
                enemy.sety(y)

            y = weapon.ycor()
            y += weapon.bullet_speed
            weapon.sety(y)

            # check if the bullet has gone to the top
            if weapon.ycor() > 275:
                weapon.hideturtle()
                weapon.bullet_state = "ready"

            # check for a collision between the bullet and the enemy
            if self.is_collision(weapon, enemy):
                # reset the bullet
                weapon.hideturtle()
                weapon.bullet_state = "ready"
                weapon.setposition(0, -400)
                # reset the enemy
                enemy.setposition(-200, 250)

            # check if the enemy hits the player
            if self.is_collision(player, enemy):
                player.hideturtle()
                enemy.hideturtle()
                print("Game Over")
                break


if __name__ == "__main__":
    screen = Screen()
    player = Player()
    player.binding()
    weapon = Weapon()
    weapon.binding()
    enemy = Enemy()
    game = Game()
    game.run()
    turtle.done()
