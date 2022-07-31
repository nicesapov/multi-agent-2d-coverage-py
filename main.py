#!/usr/bin/env python3

from agent import *
import scalar_field
import time
from constants import * 

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def main():
#    fig = plt.figure()
#    ax = fig.add_subplot(111)

    fig, ax = plt.subplots()
#    fig.set_figwidth(10)#X_MAX - X_MIN)
#    fig.set_figheight(12)#Y_MAX - Y_MIN)
    agents = [Agent(x, y, c, a) for [x, y, c, a] in INITIAL_POSITIONS]

    def animate(t):
        nonlocal agents
        print(t)
        ax.clear()

        ax.set_xlim([X_MIN, X_MAX])
        ax.set_ylim([Y_MIN, Y_MAX])

        x, y, field, func = scalar_field.get_field(t)
        cs = ax.contour(x, y, field, levels = LEVELS)
        ax.clabel(cs)

        updated = [agent.updated(func, t, agents) for agent in agents]
        agents = updated
        [plt.plot(agent.p[0], agent.p[1], marker='o', color=agent.color) for agent in agents]

        return cs

    anime = animation.FuncAnimation(
        fig,
        animate,
        frames = OVERALL_DURATION,
#        interval = DISPLAY_FREQUENCY, 
        repeat = True,
    )

    anime.save(
        'anime.gif', 
        writer='imagemick', 
        fps=20,
        dpi=120,
    )

if __name__ == '__main__':
    main()
