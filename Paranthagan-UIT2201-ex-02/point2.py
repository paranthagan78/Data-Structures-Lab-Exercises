'''
    This module generates the random sequence of N points, takes integer "k", 
    takes New point and returns K nearest neighbours of that point

    Orginal Author: Paranthagan S
    Created On: 20/04/23
'''

from point1 import Point                #importing required module
import random


x1=float(input("Enter point x1: "))
y1=float(input("Enter point x2: "))
Pnew=Point(x1,y1)
print("New Point: ",Pnew)

def generate_point(l):                  #this function is to generate Number of random points
    n=int(input("Enter Number Points: "))
    for i in range(n):
        x2=random.randint(1,100)
        y2=random.randint(1,100)
        point=Point(x2,y2)
        l.append((str(point),Pnew.distance(point)))

k=int(input("Enter Number of Nearest Neighbours: "))    #getting the integer 'k'
l=[]
generate_point(l)                       #calling the function for generating points
l.sort(key = lambda x : x[1])
print ("Number of Point: ",l)           #returns list of points in ascending order
print (f"Number of {k} Nearest Neighbours: ",l[0:k])    #return 'k' nearest neighbours from new point
