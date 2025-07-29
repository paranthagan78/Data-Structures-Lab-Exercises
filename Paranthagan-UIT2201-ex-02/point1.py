import random


class Point:
    '''
    This class represents 2-Dimensional point and gives the Euclidean distance
    between the two points

    Orginal Author: Paranthagan S
    Created On: 20/04/23
    '''
    
    def __init__(self,a,b):     #constructor of point class
        self.x=a
        self.y=b
    
    
    def __str__(self):          #display the value for object
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def distance(self,other):   #find Euclidean distance between two points by using formula
        xdis=(self.x-other.x)**2
        ydis=(self.y-other.y)**2
        dis=(xdis+ydis)**0.5
        return dis

#Driver Code
if __name__ == "__main__":      
    x1=float(input("Enter Coordinate of X1: "))
    y1=float(input("Enter Coordinate of Y1: "))
    x2=float(input("Enter Coordinate of X2: "))
    y2=float(input("Enter Coordinate of Y2: "))
    p1=Point(x1,y1)
    p2=Point(x2,y2)
    print(f"Distance Between {p1} and {p2} is ",p1.distance(p2))
