"""
game settings
"""

import math

# window
RES = WIDTH, HEIGHT = 1600, 900  # size of the window
FPS = 0  # frames per second

# player
PLAYER_POS = 1.5, 5  # spawn location
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

# raycasting
FOV = math.pi / 3  # field of view aka angle of view
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS  # space inbetween each ray
MAX_DEPTH = 20  # length of the rays
