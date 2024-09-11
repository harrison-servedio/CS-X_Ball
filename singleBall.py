from ball import ball

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

trail = True

a = ball("green")


def animate(i):
    plt.cla()
    a.stepToCenter()
    if trail:
        plt.plot(a.Xs, a.Ys, color=a.color)
    plt.plot(a.Xs[-1], a.Ys[-1], marker="o", markersize=8, markeredgecolor=a.color, markerfacecolor=a.color)
    plt.axis('equal')
    plt.axis([-300, 300, -300, 300])

fig, ax = plt.subplots()

ani = FuncAnimation(plt.gcf(), animate, interval=500, cache_frame_data=False)

plt.show()