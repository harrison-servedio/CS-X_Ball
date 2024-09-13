from ball import ball

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

trail = False

ballArray = [ball("blue"), ball("red"), ball("green")]


def animate(i):
    plt.cla()

    for b in ballArray:
        b.step()
        if trail:
            plt.plot(b.Xs, b.Ys, color=b.color)
        plt.plot(b.Xs[-1], b.Ys[-1], marker="o", markersize=8, markeredgecolor=b.color, markerfacecolor=b.color)
    
    plt.axis('equal')
    plt.axis([-300, 300, -300, 300])

fig, ax = plt.subplots()

ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.show()