...
                                            # (Assignment-01 )#                                                                        
                                            
...

#(number-01)#

a = 7
b = 2
# add.
print ('Sum: ', a + b)  
# sub.
print ('Subtraction: ', a - b)   
# multi.
print ('Multiplication: ', a * b)  
# div.
print ('Division: ', a / b) 
# floor div.
print ('Floor Division: ', a // b)
# modulus
print ('Modulus: ', a % b)  
# Expo.
print ('Power: ', a ** b)   

#(number-02)# Python program to swap two variables

A = 2
B = 5
temp = A
A = B
B = temp
print('The value of A after swapping: {}'.format(A))
print('The value of B after swapping: {}'.format(B))
#For example swap two variables
A = 2
B = 5
print(A)
print(B)

#(number-03)#

w = 21
x = 30
y = 44
print(w+y)
print(y -w)
print(y % x)
print(y // w)
print(y ** w)
print(w * x)
print(y / x)

#(number-04)# This program adds two number

num1 = 5.2
num2 = 1.4
# Add two numbers
sum = num1 + num2
# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
# Add two numbers
sum = float(num1) + float(num2)
# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

#(question-05)#

# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.
#Even
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
   #Odd
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

#(number-06)#

a = True
b = False
print(not(a))
print(not(b))

a = False
b = False
x = not(a)
y = not(b)
print(a or b)
print(x or y)
print(a or x)
print(x or b)
print(y and b) 

a = False
b = False
x = not(a)
y = not(b)
print(a and b)
print(a and x)
print(x and y)

#(Question-07)#
a = 1
b = 20
if a < 10:
    print('Demo string 1')
else:
    print('Demo string 2')

    a = 1
b = 20
if a < 10 or b == 20:
    print('Demo string 1')
else:
    print('Demo string 2')

    a = 1
b = 20
if a < 10 and not(b == 20):
    print('Demo string 1')
else:
    print('Demo string 2')

#(Question-08)

age = int(input('Please enter your age in years: '))
income = int(input('Please enter your annual income: '))
if age >= 21 and income >=21000:
    print('You can apply for a loan')
else:
    print('You CANNOT apply for a loan')

#(question -09)

age = float(input("Student age:"))
Qualifing = input("student qualifiction in examination:")
if age>=20 and Qualifing == "yes":
   print("You can enrol on the course")
else:
   print("You cannot enrol on the course")

#(question -10)#
Amount = float(input("Enter the amount of products:"))
if Amount == 7000:
    Q = Amount -(Amount*0.25)
    print("Your today's discount is 25% that is ",Q)
elif Amount<7000:
    print('Shopping done till date')
elif Amount>=50000:
    S =Amount - (Amount*0.50)
    print("Your today's discount is 50% that is",S)
elif Amount>35000 and Amount <= 50000:
    N = Amount-(Amount*0.15)
    print("Your today's discount is 15% that is",N)
else:
    print("you cant get any discount",Amount)


#(question-11)#

w = 20
x = 10
y = 15
z = 2
result_1 = (w+x)*y/z
result_2 = ((w+x)*x)/z
result_3 = ((w+x)*(y/z))**z
result_4 = w+(x*y)/z
print('The value of (w+x)* y/z is',result_1)
print('The value of ((w+x)*x)/z is',result_2)
print('The value of ((w+x)*(y/z))**z is',result_3)
print('The value of w+(x*y)/z is',result_4)
