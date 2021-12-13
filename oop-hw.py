#Problem 1
#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

import math

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        a = self.coor2[0] - self.coor1[0]
        b = self.coor2[1] - self.coor2[1]

        c = a**2 + b**2

        return math.sqrt(c)

    
    def slope(self):
        pass


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())