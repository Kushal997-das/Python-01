#Q 03.Write a program to test the divisibility of a number with another number.
n=int(input("enter the number"))
k=int(input("enter the divisible number"))
if(n%k==0):
   print("yes number is divisible by",k)
else:
   print("no number is not divisible by",k)
print("final answer is=",n//k)
