"""
Python Classes Introduction

Objects are variables that contain data and functions that can be used to manipulate the data

Functions contained in an object are called methods

Variable Stored in an object are called attributes


"""
import random as r
import math


class ball:
    # init function runs with class is created
    # self argument is always needed and automatically passed 
    def __init__(self, color, startX = 2, startY = 2):
        
        # Defines the class attributes Xs and Ys
        # An attribute is a variable specific to a class
        self.Xs = [startX]
        self.Ys = [startY]
        
        # Defines the class attribute for the color
        self.color = color
    
    # Unnecessary function that can be used to modify the class attribute "color"
    def setColor(self, color):
        self.color = color

    # Unnecessary function that can be used to get the class attribute "color"
    def getColor(self):
        return self.color

    # Generates a random step in the movement of the ball
    # The step has a higher chances of going to the center so the ball does not leave the frame of the animation or graph
    def step(self, minVelo = 5, maxVelo = 100):
        size = r.randint(0, 180)
        angleToCenter = math.atan2(-self.Ys[-1], -self.Xs[-1])
        angleToCenter = angleToCenter*180/math.pi + 360 if angleToCenter < 0 else angleToCenter*180/math.pi
        travelAngle = r.randint(int(angleToCenter)-size, int(angleToCenter)+size)
 
        velo = r.randint(minVelo, maxVelo)

        self.Xs.append(self.Xs[-1] + velo*math.cos(travelAngle*math.pi/180))
        self.Ys.append(self.Ys[-1] + velo*math.sin(travelAngle*math.pi/180))