from ball import ball

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

trail = True

oliverJohn = ball("green")


def animate(i):
    plt.cla()
    oliverJohn.step()
    if trail:
        plt.plot(oliverJohn.Xs, oliverJohn.Ys, color=oliverJohn.color)
    plt.plot(oliverJohn.Xs[-1], oliverJohn.Ys[-1], marker="o", markersize=8, markeredgecolor=oliverJohn.color, markerfacecolor=oliverJohn.color)
    plt.axis('equal')
    plt.axis([-300, 300, -300, 300])

fig, ax = plt.subplots()

ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.show()