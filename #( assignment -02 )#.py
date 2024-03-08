                                    #( assignment -02 )#
              #(Control Structures Statements (if, elif, else and nested if))#

#(questuon -01)
age = int(input('Please enter your age: '))
if age >=18:
    print('Collect your polling card')
else:
    print('You are to young to vote')

#(question - 02)
age=int(input("Enter age"))
if age>=65:
    print ("You may apply for the concessionary travel card")
else:
    print ("Sorry you are not old enough to apply for a concessionary travel card")

#(question -03)
x = 7
y = 4
z = x + y
if z < 10:
    z = z + x
    z = z - y
else:
    if z > 10:
        x = z + 2
        z = x + y
print(z)

x = 7
y = 4
z = x + y
if z < 10:
    z = z + x
    z = z - y
else:
    if z == 10:
        x = z + 2
        z = x + y
print(z)

x = 3
y = 4
z = x + y
if z < 10:
    z = z + x
    z = z - y
else:
    if z == 10:
        x = z + 2
        z = x + y
print(z)

x = 3
y = 4
z = x + y
if z < 10:
    if z == 7:
        x = z + 3
        z = x * y
else:
    z = z * 2
print(z)

#(question-04)
num1, num2 = 20 , 30
if num1>num2:
  print(num1)
else:
  print(num2)

#(question-05)
num1 = 15
num2 = 20
num3 = 10

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

#(question-06)
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

                                                 #(Loops ) 
                         #Note : Perform the exercise given below with both for loop and while loop.)

 ## Question 1 ## 1. Write a python program to print the first 20 integers
print('first 20 integers ')
for i in range(1, 21):
   print(i, end= " ")
## Question 2 ## Write a python program to print the reverse counting from 100 to 1
print('first 100 integers ')
for i in range(100, 1):
   print(i, end= " ")
##3. Write a python program to print the sum of 1st 20 integers. 
n = int(input("Input a number: "))
sum_num = (20 * (20 - 1)) / 2
print("Sum of the first", n ,"positive integers:", sum_num)
##4. Write a python program to check if the number is an even number or odd. 
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
##5. Write a python program to print 1st 10 even numbers. 
print("1st 10 Even Numbers")
a = 1
while(a <= 10):
    print(2 * a)
    a = a + 1
##6. Write a python program to print 1st 10 odd numbers. 
print("1st 10 odd Numbers")
a = 1
while(a <= 10):
    print(2 * a-1)
    a = a + 1
##7. Write a python program to print the sum of 1st 20 even numbers. 
def evensum(n):
    return n * (n + 1)
n = 10
print("sum of first", n, "even number is: ",
       evensum(n))
##8. Write a python program to print the sum of 1st 20 odd numbers. 
def oddsum(n):
    return (n/2) * (2*n)
n = 10
print("sum of first", n, "odd number is: ",
       oddsum(n))
##9. Write a python program to print the multiplication table of a number in the format given below: 2*1=2 2*2=4 
n=int(input("Enter the number to print the tables for:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
##10. Write a python program to find those numbers which are divisible by 7 and multiple of 5, between 1000 and 2500 (both included). 
lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
for a in range (lower,upper+1):
    if(a%7==0 and a%5==0):
        print(a)
##11. Write a python program to count the number of digits in a number. 
num = 5462265
count = 0
while num != 0:
    num //= 10
    count += 1
print("Number of digits: " + str(count))
##12. Write a python program to print the reverse of a number. 
num = 5462265
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed Number: " + str(reversed_num))
##13. Write a python program to check if the number is a palindrome or not. 
num = input("Enter a number:")
if num == num[::-1]:
    print("\nYes, its a palindrome")
else:
    print("\nNo, its not a palindrome")

##14. Write a python program to check if the number is an amstrong number or not. 

##15. Write a python program to calculate the cube of all the numbers from 1 to a given number. 
def cube(num):
    return num * num * num
num = int(input("Enter an any number : "))
cb = cube(num)
print("Cube of {0} is {1}".format(num, cb))
##16. Write a python program to calculate the factorial of a given number. 
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
num = 5
print("Factorial of", num, "is",
factorial(num))