import math
import numpy as np

from constants import *

def linear_map(x, x_min, x_max, _min, _max):
    return _min + (x - x_min) * ((_max - _min) / (x_max - x_min))

def moving_mountain(x, y, iteration):
    scale_min = 0.9
    scale_max = 1.1

    t = iteration/PERIOD * 2*math.pi
    
    scale = linear_map(
        math.sin(t), 
        -1, 1,
        scale_min, scale_max
    )

    C_X_MIN = -10
    C_X_MAX = 10

    c_x = linear_map(
        math.sin(t * 1.1),
        -1, 1,
        C_X_MIN, C_X_MAX
    )

    c_y = linear_map(
        math.cos(t * 1.2),
        -1, 1,
        C_X_MIN, C_X_MAX
    ) * scale

    return scale * H - min(scale * H, math.hypot(x-c_x, y*scale-c_y))

def deforming(x, y, i):
    return np.linalg.norm(
        [
        moving_mountain(x / 1.2, y, i),
        moving_mountain(x + y, x - y, i * 1.1),
        moving_mountain(x - y/2, x + y/2, i * 1.2), 
        moving_mountain(x/2 - y, x + y/2, i / 1.2 +
            PERIOD / 2),
        ]
    )


def get_field(t):
    f = np.vectorize(moving_mountain)
    #f = np.vectorize(deforming)

    x, y = np.mgrid[X_MIN:X_MAX, Y_MIN:Y_MAX]

    return x, y, f(x, y, t)
