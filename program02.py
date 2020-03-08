#Q 02.Enter three integers (i)print the largest of the three.
                     #(ii)sum of all inputs.
                      #(iii)sum of non-duplicate number.
#(i):

x, y, z =input("enter three numbers\n").split(" ")
print(f"{x} {y} {z}")
if(x>=y and x>=z):
       print("x is the largest number among them",x)
elif (y>=z):
   print("y is largest number among them",y)
else:
       print("z is the largest number among them",z)
       
#(ii):

x=int(input("enter your 1st number"))
y=int(input("enter your 2nd number"))
z=int(input("enter your 3rd number"))
print(f"{x} {y} {z}")
k=x+y+z
print(k)

#(iii):
x=int(input("enter your 1st number"))
y=int(input("enter your 2nd number"))
z=int(input("enter your 3rd number"))
if(x != y and y != z and x != z):
   k=x+y+z
   print(k)
elif (x==y==z):
   print('sum is=',0)
elif (x==y):
   print('sum is=',z)
elif (y==z):
   print("sum is=",x)
elif (x==z):
   print("sum is=",y)


