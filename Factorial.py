#Factorial of a number
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*(fact(n-1))
num=int(input("Enter the number:"))
print("The factorial of",num, "is",fact(num))


#using Factorila Function
import math
n=int(input("Enter the Number:"))
print("The Factorial of ",n, "is", math.factorial(n))