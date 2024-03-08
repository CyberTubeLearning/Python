##1question## Create a function with variable length arguments.
def sum(*args):
    print(type(args))
    print(args)

sum(10, 20)
sum(10, 20, 30)
sum(10, 20, 30, 40)
##2 question### Define a function in python that accepts3 values and return the maximum of three numbers.
def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest
res = maximum(2, 4, 7)
print("Largest Number: ", res)
##3question## Define a function tht returns the factorial of a number
def factorial(n):
       
    if n == 0:
        return 1
      
    return n * factorial(n-1)
# Driver Code
num = 5;
print("Factorial of", num, "is",
factorial(num))
##4 question## accepts the radius and returns the area of a circle.
def findArea(r):
    PI = 3.14
    return PI * (r*r);
print("Area of circle = %.6f" % findArea(6));
## 5question## Define a function that accepts tha interest rate and returns the amount(Simple Interest and compound interest separately).
def simple_interest(p,t,r):
	print('The principal is', p)
	print('The time period is', t)
	print('The rate of interest is',r)
	
	si = (p * t * r)/100
	
	print('The Simple Interest is', si)
	return si
	
# Driver code
simple_interest(8, 6, 8)

##6 question## Deffine a function that returns the square root of a number.
import math
print (math.sqrt(9))
print (math.sqrt(25))
print (math.sqrt(16))

##7question## Calculate the factorial of a number using the cohncept of recursion.
def factorial(n):
	if (n==1 or n==0):
		
		return 1
	
	else:
		
		return (n * factorial(n - 1))
num = 5;
print("number : ",num)
print("Factorial : ",factorial(num))
