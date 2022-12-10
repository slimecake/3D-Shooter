import pygame as pg
import sys
from settings import *  # import the settings file
from map import *  # import the map file
from player import *  # import the player file
from raycasting import *  # import the raycasting file


class Game:
    def __init__(self):
        pg.init()  # done in any pygame program, initialize pygame
        self.screen = pg.display.set_mode(RES)  # set resolution
        self.clock = pg.time.Clock()
        self.delta_time = 1  # prevents movement speed being effected by FPS
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)

    def update(self):
        self.player.update()  # update player movement
        self.raycasting.update()  # update raycasting live
        pg.display.flip()
        self.delta_time = self.clock.tick(
            FPS
        )  # set FPS and prevent movement speed being effected by it
        pg.display.set_caption(f"{self.clock.get_fps() :.1f}")  # .1f round to 1dp

    def draw(self):
        self.screen.fill("black")
        self.map.draw()
        self.player.draw()

    def check_events(self):
        for event in pg.event.get():  # check for user input
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):  # close game if esc pressed
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
