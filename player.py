from settings import *  # import the settings file
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        """
        complex math that works out how amount to move by depending on a bunch of factors
        don't bother trying to understand
        you won't, it for some reason uses triginometry and pi
        """

        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()  # check for key presses
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (
            x,
            y,
        ) not in self.game.map.world_map  # check if player position is in wall

    def check_wall_collision(self, dx, dy):
        """
        will only allow movement if there is no wall
        """

        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        """
        test method
        """

        """pg.draw.line(
            self.game.screen,
            "blue",
            (self.x * 100, self.y * 100),
            (
                self.x * 100 + WIDTH * math.cos(self.angle),
                self.y * 100 + WIDTH * math.sin(self.angle),
            ),
            2,
        )"""
        pg.draw.circle(self.game.screen, "green", (self.x * 100, self.y * 100), 15)

    def update(self):
        self.movement()

    @property  # A decorator is a function which takes another function as an argument and returns a modified version of it, enhancing its functionality in some way
    def pos(self):
        return self.x, self.y

    @property  # A decorator is a function which takes another function as an argument and returns a modified version of it, enhancing its functionality in some way
    def map_pos(self):
        return int(self.x), int(self.y)
