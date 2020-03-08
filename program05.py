#05.Write a program to display a menu for calculating area of a circle or preimeter.
#(i)Ask for radius of a circle?
import math
r=float(input("enter the radius of a circle"))
area=math.pi*r*r
print("the area of a circle is:",area)
perimeter=2*math.pi*r
print("the perimeter of a circle is :",perimeter)
