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
    agent = Agent()

    def animate(t):
        print(t)
        ax.clear()

        ax.set_xlim([X_MIN, X_MAX])
        ax.set_ylim([Y_MIN, Y_MAX])

        x, y, field = scalar_field.get_field(t)
        cs = ax.contour(x, y, field, levels = [6, 10, 14, 18])
        ax.clabel(cs)

        agent.update(field)
        plt.plot(agent.x, agent.y, marker='o')

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
        fps=15,
        dpi=30,
    )

if __name__ == '__main__':
    main()
