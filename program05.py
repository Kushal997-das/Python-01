#05.Write a program to display a menu for calculating area of a circle or preimeter.
#(i)Ask for radius of a circle?
#(ii)if-elif statement:

import math
r=float(input("enter the radius of a circle"))
area=math.pi*r*r
print("the area of a circle is:",area)
perimeter=2*math.pi*r
print("the perimeter of a circle is :",perimeter)

#if-elif statement:
#If            >=90 A
#elif          >=80 <=90 B
#elif          >=70 <=80 C
#else         fail
mark=float(input("enter the mark"))
if(mark>=90):
   print("A")
elif(mark>=80 and mark<=90):
   print("B")
elif(mark>=70 and mark<=80):
   print("C")
else:
   print("fail")
