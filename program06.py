#Q 06.Write a program that reads two numbers of an arithmetic operator & display the computed result.
#(i)enter 1&2
#op=input(enter operator[+ - * / %]:
num1=1
num2=2
print("enter which operator would you like to perform")
op=input("enter any of these given operator +,-,*,/,%\n")
if op=='+':
   result=num1+num2
elif op=='-':
   result=num1-num2
elif op=='*':
   result=num1*num2
elif op=='/':
   result=num1/num2
elif op=='%':
   result=num1%num2
else:
   print(" you press invalid operator")
print(num1,op,num2,"=",result)

