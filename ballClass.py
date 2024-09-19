"""
Objects are variables that contain data and functions that can be used to manipulate the data

Functions contained in an object are called methods

Variable Stored in an object are called attributes


"""


import random as r
import math


class ball:
    # init function runs with class is created
    # self argument is always needed and automatically passed 
    def __init__(self, color, startX = 2, startY = 2) -> None:
        
        # Defines the class attributes Xs and Ys
        # An attribute is a variable specific to a class
        self.Xs = [startX]
        self.Ys = [startY]
        
        # Defines the class attribute for the color
        self.color = color
    
    # Redundant function that can be used to modify the class attribute "color"
    def setColor(self, color):
        self.color = color

    # Function to take a random step and generate new data for the Xs list and the Ys list
    def step(self, minVelo = 5, maxVelo = 100):
        size = r.randint(0, 180)
        angleToCenter = math.atan2(-self.Ys[-1], -self.Xs[-1])
        angleToCenter = angleToCenter*180/math.pi + 360 if angleToCenter < 0 else angleToCenter*180/math.pi
        travelAngle = r.randint(int(angleToCenter)-size, int(angleToCenter)+size)
 
        velo = r.randint(minVelo, maxVelo)

        self.Xs.append(self.Xs[-1] + velo*math.cos(travelAngle*math.pi/180))
        self.Ys.append(self.Ys[-1] + velo*math.sin(travelAngle*math.pi/180))