"""
make map of entire game
"""

import pygame as pg

_ = False  # used for better perception of map, could use anything eg. 0
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):  # j is counter of each element in rows
            for i, value in enumerate(row):  # i is counter of each element in each row
                if value:
                    self.world_map[(i, j)] = value  # coordinates of each "wall"

    def draw(self):
        [
            pg.draw.rect(
                self.game.screen, "darkgray", (pos[0] * 100, pos[1] * 100, 100, 100), 2
            )
            for pos in self.world_map  # draws a rectange, aka square, in each pos of the walls
        ]
