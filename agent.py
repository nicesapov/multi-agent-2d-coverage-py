import scalar_field
from constants import *
import numpy as np 
import math
import copy

class Agent:
    def __init__(self, x, y, angle):
        self.p = np.array([float(x), float(y)])

        self.angle = angle
        self.e = np.array([math.cos(self.angle), math.sin(self.angle)])
        self.vision = VISION

        #TODO convert meters per second to this custom scale
        self.vmax = 0.6 #distance per frame
        self.v = self.vmax

        self.track = []
        self.prev_f = None
        
        self.we = 0.2
        self.mu = 0.8
        self.f_delta_max = 0.1

    def updated(old, field_func, t, agents):
        assert isinstance(agents, list)
        self = copy.deepcopy(old)

        if len(self.track) == MAX_TRACK:
            assert old is old
            assert not self is old
            
            closest_agent = None
            closest_projection = None

            def get_projection(agent):
                assert isinstance(agent, Agent)

                saw_latest = np.linalg.norm(agent.track[MAX_TRACK - 1] - self.track[MAX_TRACK - 1]) < VISION  
                saw_oldest = np.linalg.norm(agent.track[0] - self.track[0]) < VISION  

                return [saw_oldest and saw_latest, not saw_oldest and not saw_latest, max([np.linalg.norm(agent.track[i] - self.track[i])] for i in range(MAX_TRACK))]

            for agent, c in agents:
                if agent is old:
                    continue

                projection = get_projection(agent)
                if closest_agent is None or projection < closest_projection:
                    closest_agent = agent
                    closest_projection = projection

            distance_to_closest = np.linalg.norm(closest_agent.p - self.p) 
            if distance_to_closest < VISION:
                self.v = self.vmax * distance_to_closest / VISION

        self.track += [self.p]
        if (len(self.track) > MAX_TRACK):
            assert len(self.track) == MAX_TRACK + 1
            self.track = self.track[1:]


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

            de = np.sign(df + self.v * chi(f - TARGET_ISOLINE))

        self.angle -= de * self.we
        self.e = np.array([math.cos(self.angle), math.sin(self.angle)])

        print(f, self.prev_f, self.e, de)

        self.p += self.e * self.v

        self.prev_f = f

        return self
