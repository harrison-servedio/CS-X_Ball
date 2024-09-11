import random as r
import math



class ball:
    
    def __init__(self, color) -> None:
        self.Xs = [2]
        self.Ys = [2]
        
        self.color = color
        
    def stepToCenter(self, minVelo = 5, maxVelo = 100):
        size = r.randint(0, 180)
        angleToCenter = math.atan2(-self.Ys[-1], -self.Xs[-1])
        angleToCenter = angleToCenter*180/math.pi + 360 if angleToCenter < 0 else angleToCenter*180/math.pi
        travelAngle = r.randint(int(angleToCenter)-size, int(angleToCenter)+size)
 
        velo = r.randint(minVelo, maxVelo)

        self.Xs.append(self.Xs[-1] + velo*math.cos(travelAngle*math.pi/180))
        self.Ys.append(self.Ys[-1] + velo*math.sin(travelAngle*math.pi/180))