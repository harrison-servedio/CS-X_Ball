import random as r
import math

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class ball:
    
    def __init__(self) -> None:
        self.Xs = [2]
        self.Ys = [2]
        
        self.radius = 1
        
    def stepToCenter(self, minVelo = 5, maxVelo = 100):
        size = r.randint(0, 180)
        angleToCenter = math.atan2(-self.Ys[-1], -self.Xs[-1])
        angleToCenter = angleToCenter*180/math.pi + 360 if angleToCenter < 0 else angleToCenter*180/math.pi
        travelAngle = r.randint(int(angleToCenter)-size, int(angleToCenter)+size)
 
        velo = r.randint(minVelo, maxVelo)

        self.Xs.append(self.Xs[-1] + velo*math.cos(travelAngle*math.pi/180))
        self.Ys.append(self.Ys[-1] + velo*math.sin(travelAngle*math.pi/180))

        
a = ball()


def animate(i):
    plt.cla()
    a.stepToCenter()
    # plt.plot(a.Xs, a.Ys)
    plt.plot(a.Xs[-1], a.Ys[-1], marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")
    plt.
    plt.axis('equal')

fig, ax = plt.subplots()

ani = FuncAnimation(plt.gcf(), animate, interval=200, cache_frame_data=False)

plt.show()