import math
import random
import turtle
from typing import List


class Screen(turtle.Turtle):
    def __init__(self):
        super().__init__()

        # create screen
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.title("Space Invaders")
        self.screen.bgpic("img/background.png")
        self.screen.register_shape("img/invader2.png")
        self.screen.register_shape("img/player2.png")

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
        super().__init__()

        # create player
        self.penup()
        self.color("red")
        self.shape("img/player2.png")
        self.speed(0)
        self.setposition(0, -255)
        self.setheading(90)
        self.player_speed = 15

        # binding
        self.screen.listen()
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")

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


class Enemy(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.enemy_speed = 2

        # create enemy
        self.color("blue")
        self.shape("img/invader2.png")
        self.penup()
        self.speed(0)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        self.setposition(x, y)


class Weapon(turtle.Turtle):
    def __init__(self):
        super().__init__()

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

        # binding
        self.screen.onkey(self.fire_bullet, "space")

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


class Game:
    def __init__(self, player: Player, enemies: List[Enemy], weapon: Weapon):
        super().__init__()
        
        self.player = player
        self.enemies = enemies
        self.weapon = weapon

        # create the game score
        self.score = 0
        self.score_pen = turtle.Turtle()
        self.score_string = "Score: %s" % self.score
        self.score_pen.speed(0)
        self.score_pen.color("white")
        self.score_pen.penup()
        self.score_pen.setposition(-290, 280)
        self.score_pen.write(self.score_string, False, align="left", font=("Arial", 14, "normal"))
        self.score_pen.hideturtle()

    def run(self):
        while True:
            for e in self.enemies:
                # move the enemy
                x = e.xcor()
                x += e.enemy_speed
                e.setx(x)

                # move the enemies back and down
                if e.xcor() > 280:
                    for i in self.enemies:
                        y = i.ycor()
                        y -= 40
                        i.sety(y)
                    e.enemy_speed *= -1

                if e.xcor() < -280:
                    for i in self.enemies:
                        y = i.ycor()
                        y -= 40
                        i.sety(y)
                    e.enemy_speed *= -1

                # check for a collision between the bullet and the enemy
                if self.weapon.is_collision(self.weapon, e):
                    # reset the bullet
                    self.weapon.hideturtle()
                    self.weapon.bullet_state = "ready"
                    self.weapon.setposition(0, -400)
                    # reset the enemy
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    e.setposition(x, y)
                    # update the score
                    self.score += 10
                    self.score_string = "Score: %s" % self.score
                    self.score_pen.clear()
                    self.score_pen.write(self.score_string, False, align="left", font=("Arial", 14, "normal"))

                # check if the enemy hits the player
                if self.weapon.is_collision(player, e):
                    player.hideturtle()
                    e.hideturtle()
                    print("Game Over")
                    break

            y = self.weapon.ycor()
            y += self.weapon.bullet_speed
            self.weapon.sety(y)

            # check if the bullet has gone to the top
            if self.weapon.ycor() > 275:
                self.weapon.hideturtle()
                self.weapon.bullet_state = "ready"


if __name__ == "__main__":
    screen = Screen()

    player = Player()
    enemies = [Enemy() for _ in range(5)]
    weapon = Weapon()

    game = Game(player, enemies, weapon)
    game.run()

    turtle.done()

# TODO:   Fix the enemies -> when they reach the bottom of the screen
# TODO:   make them move left/right (now they are passing below the screen).

# TODO:   Fix the register_shape -> bad arguments
