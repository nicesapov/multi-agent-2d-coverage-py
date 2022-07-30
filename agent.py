import scalar_field
from constants import *

class Agent:
    def __init__(self):
        self.x = INITIAL_X
        self.y = INITIAL_Y

    def update(self, field):
        self.x += 1
