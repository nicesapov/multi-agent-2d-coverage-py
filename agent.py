import scalar_field
from constants import *
import numpy as np 
import math
import copy

class Agent:
    def __init__(self, x, y):
        self.p = np.array([float(x), float(y)])

        self.angle = 0
        self.e = np.array([1., 0.])

        #TODO convert meters per second to this custom scale
        self.vmax = 0.6 #distance per frame
        self.v = self.vmax

        self.prev_f = None
        
        self.we = 0.2
        self.mu = 0.8
        self.f_delta_max = 0.1

    def updated(old, field_func, t, agents):
        self = copy.deepcopy(old)

        de = 0

        f = field_func(self.p[0], self.p[1], t)
        if self.prev_f:
            df = (f - self.prev_f) / self.v 

            def chi(z):
                if (z > self.f_delta_max):
                    z = self.f_delta_max

                if (z < -self.f_delta_max):
                    z = -self.f_delta_max

                return z * self.mu

            de = np.sign(df + chi(f - TARGET_ISOLINE))

        self.angle -= de * self.we
        self.e = np.array([math.cos(self.angle), math.sin(self.angle)])

        print(f, self.prev_f, self.e, de)

        self.p += self.e * self.v

        self.prev_f = f

        return self
