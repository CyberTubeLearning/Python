print("hello")
print("kfbgjfdrn")

#arithmetic operators
# +,-,*,/, %, //, **

print(2+3)
print(2-3)
print(2*3)
print(13/3) #- Quotient - division
print(13%3)  # remainder  - 0 - modulus
print(13//3)   #  whole number quotient - 4
print(3**2)  # - exponentiation - raise to power


#relational operators - 
#<,>,<=,>=,!=,==

print(12 == 3)

#assignment

a = 10

#logical operators 
# and, or ,not

# and
#             and     or
# 1       0   0       1       
# 0       1   0       1     
# 1       1   1       1
# 0       0   0       0

print((2>3) or (13>5))

a = 10
b = 20
print("Sum of the numbers is ", a+b)

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
print("Sum of the numbers is ", a+b)

a = 'n'
b = 'm'
print(a+b)

side = float(input("Enter the length of side of square: "))
area = side**2
print("Perimeter of the square with side ", side, "is",area)

##


##

n = int(input("Enter the number:"))

if n>0:

    print("Positive")

else:

    print("negative")

##

#conditional statements - if, else, elif

a = int(input("Enter the value of a:"))

if a>=60:

    print("You got first division")

else:

    print("You got second division")
    ###
marks_1 = float(input("Enter the marks: "))
marks_2 = float(input("Enter the marks in the test: "))
if marks_1>=65 and marks_2>=60:
    print("Eligible")
else:
    print("Not eligible")


   

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

#(Question-08)

age = int(input('Please enter your age in years: '))
income = int(input('Please enter your annual income: '))
if age >= 21 and income >=21000:
    print('You can apply for a loan')
else:
    print('You CANNOT apply for a loan')

#(question -10)
def calculate_discount(amount_spent_today, historical_shopping):
    if amount_spent_today > 7000:
        discount = 0.25
    else:
        if historical_shopping > 50000:
            discount = 0.25
        elif 35000 <= historical_shopping <= 50000:
            discount = 0.15
        else:
            discount = 0

    total_discount = amount_spent_today * discount
    total_amount_payable = amount_spent_today - total_discount

    return f"Discount applied: {discount*100}%\nTotal amount payable: INR {total_amount_payable}"







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



amnt=1000
while(amnt>50):
    print("college",amnt)
    amnt=amnt-50


    count = 50
while(count>=0):
    print("daily count",count)
    count = count-1



amount=50

while(amount>=0):

 print("per day amount",amount)

 amount= amount-1

a=int(input("Enter starting value :"))
b=int(input("Enter Ending value :"))
if a%2!=0:
    a += 1
if b%2 != 0:
    b -= 1

while(a>b):
    a -= 2
    print(a)


a = int(input("enter starting value : "))

b = int (input("enter ending value  :"))

while a<=b:

     print(a)

     a=a+2


#  only even no from 72 to 47

a = int(input(" enter the end value:"))

b = int(input(" enter the start value :"))

while(a<=b):

    if a%2==0:

      print(a)

    a=a+1


#  print sum of first 20 integers:

a = int(input(" enter the start value:"))

b = int(input(" enter the end value :"))

sum = 0

while(a<=b):

    sum = sum + a

    print(sum)

    a= a+1


    x2=int(input("entr starting"))

y2=int(input("enter ending"))

z = 0

while x2<=y2:
    z = z+x2
    print(z)
    x2=x2+12


##
a = int(input(" enter the start value:"))

b = int(input(" enter the end value :"))

sum = 0

while(a<=b):

    if a%2==0:

     sum = sum + a

    a= a+1

print("the sum is :",sum)


##
for n in range(1,6):

    n = int(input(" enter the values : "))

    print(n)

    if n%3==0 and n%5==0:

        print("this is mult of 5 and 3 :", n)

        break

    else :

        print("this is not mult of 5 nd 3:",n)

        continue

## Write a C program that displays the n terms of square natural numbers and their sum.

##print terms of fibonacci series upto a certain number
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

##Write a program in python to read 10 numbers from the keyboard and find their sum and average
Sum = 0

print("Please Enter 10 Numbers\n")
for i in range(1, 11):
    num = int(input("Number %d = " %i))
    Sum = Sum + num

avg = Sum / 10

print("The Sum of 10 Numbers     = ", Sum)
print("The Average of 10 Numbers = ", avg)
##Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."
##take 10 inputs of user, cube the number if odd and not multiple of three and 5, if multiple  of 3 and 5 both- add the numbers
# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

###
n = 18
i = 2
f = 0
while i<17:
    if n%i == 0:
        f = 1
        break
    i = i+1
print(f)
if f == 1:
    print("number is not prime")
else:
    print("number is prime")
##
    a=int(input("Enter the number :"))
b=2
while a%b!=0:
    b=b+1
    print(b)
if b==a:
    print("it is a prime")
else:
    print("not prime")

#variable-length arguments

def var1(a,c,*b):

    print(a)

    print(c)

    print("Tuple",b)

 

var1(10,20,30,40,50,60,70)



#positional arguments

def fun1(a,b):

    print(a-b)


fun1(b=20,a=30)



#default arguments

 

def fun(a,b=10):

    print(a)

    print(b)

fun(20,50)



# function with arguments

 

#required arguments

def f1(a,b):#formal arguments

    print(a+b)


f1(10,20)    #actual arguments

f1(20,40)



a=7
b=9
c=22

if a>b and a>c:
   print(a)
elif b>a and b>c:
   print(b)
else:
   print(c)


# Sum of natural numbers up to num

num = 20

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)




n = int(input("Input a number: "))
sum_num = (20 * (20 - 1)) / 2
print("Sum of the first", n ,"positive integers:", sum_num)


sum=0
for i in range (1,21):
    sum=sum+i
    
n=0
for n in range (1,40):
  if n%2==0:
    n=n+2
    print(n)


# Example of lambda function using if-else

M = lambda a, b : a if(a > b) else b

print(M(1, 2))

M = lambda a, b : "a is greater" if(a > b) else "b is greater"

print(M(1, 2))



cube_v2 = lambda x : x**3
print(cube_v2(3))

def addition(n):

    return n+(0.1*n)




# We double all numbers using map()

numbers = (10000, 20000, 30000, 40000)

result = map(addition, numbers)

print(list(result))



import functools




# initializing list

lis = [1, 3, 5, 6, 2]




# using reduce to compute sum of list

print("The sum of the list elements is : ", end="")

print(functools.reduce(lambda a, b: a+b, lis))




# using reduce to compute maximum element from list

print("The maximum element of the list is : ", end="")

print(functools.reduce(lambda a, b: a if a > b else b, lis))


# try block to handle the exception
try:
	my_list = []

	while True:
		my_list.append(int(input()))

# if the input is not-integer, just print the list
except:
	print(my_list)



    # Code to take input of a list
# from the user.

# 'try' part to handle the exception
try: 
    list = []
    print("Enter elements: ")
    while True:
        x = int(input())
        list.append(x)
except:
    print("List: ", list)


def reverse_slicing(s):
    return s[::-1]
my_number = '123456'

print('Revers number=', reverse_slicing(my_number))
## 9 th class

##9th
# list - 
list = [1,2,3,4,5]
list

l = [1,2,'jnj',10.2,"A"]
for i in l:
    print(i,end = " ")

#index - position - 0
# why?
#index - number of elements a particular element is away from the first position

l = [1,2,'jnj',10.2,"A"]
l[3]

l = [1,2,3,4,5]
l1 = ['a','b','c','d']
nl = [l,l1]
nl[0][2]

l = [1,2,3,4,5]
len(l)

l = [1,2,3,4,5]
sum(l)

l = [1,2,3,4,5]
min(l)

l = [1,2,3,4,5]
max(l)

l = [1,2,3,4,5]
n = 'rtty'
l.append(n)
l

l = [1,2,3,4,5]
n = 'rtty'
l.insert(2,n)
l

n = int(input("Enter the number of elements:"))
l = []
for i in range(n):
    ele = int(input("Enter the element: "))
    l.append(ele)
    
l

List = [1, 2, 3, 1, 2, 1, 22, 2, 3, 2, 1]
for i in range(len(List)-1,-1,-1):
    print(List[i])
# n = int(input("Enter the element to be searched:"))
# for i in range(len(List)):
#     if List[i] == n:
#         print(i)
        
# print(List.index(22))

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(1))

List1 = [-1, 2, 3]
List2 = [2, 3, 4, 5]
List1.extend(List2)		
print(List1)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

#Reverse flag is set True
List.sort(reverse = True)

#List.sort().reverse(), reverses the sorted list
print(List)	

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(sorted(List,reverse=True))
print(List)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop())
print(List)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop(1))
print(List)

List = [2.3, 4.445, 3, 5.33,3, 1.054, 2.5]
List.remove(3)
print(List)
del List[0]
print(List)

List = [1, 2, 'Gdkj fvs', 4, 'For', 6, 'Gajv1']
print(List[2])

print("Accessing element using negative indexing")

print(List[-1])
print(List[-3])

List = ['r','a','E','d','S','F','O','R','b','d','E','T','S']
print("Initial List: ")
print(List)

Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)

Sliced_List = List[5:]
print("\nElements sliced from 5th "
	"element till the end: ")
print(Sliced_List)

Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)


# Creating a List
List = ['R','D','E','K','S','F','N','W','N','Q','E','S']
print("Initial List: ")
print(List[6:])

Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)

Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)

List = ['R','D','E','K','S','F','N','W','N','Q','E','S','@']
Sliced_List = List[::-2]
print("\nPrinting List in reverse: ")
print(Sliced_List)
## 10 clss
n = int(input("Enter the number of elements:"))

l = ()

for i in range(n):

    ele = int(input("Enter the element: "))

    l = l+(ele,)

    print(l)

    ##11 class


Dict = {1: 'Steve', 'name': 'For', 3: 'Steve'}




# Deleting an arbitrary key

# using popitem() function

pop_ele = Dict.popitem()

print(pop_ele)

print(Dict)



Dict = {1: 'Steve', 'name': 'For', 3: 'Steve'}





# Deleting entire Dictionary

Dict.clear()

print("\nDeleting Entire Dictionary: ")

print(Dict)



original = {1:'Steve', 2:'for'}




# copying using copy() function

new = original.copy()

# print(new)

# del new[1]

# removing all elements from new list

# and printing both

new.clear()

print('new: ', new)

print('original: ', original)




original = {1:'one', 2:'two'}




# copying using =

new = original

# print(id(new))

# print(id(original))

del new[1]

# removing all elements from new list

# and printing both

# new.clear()

print('new: ', new)

print('original: ', original)


text1 = {1: "efgs", 2: "for"}

text2 = text1




# Using clear makes both text1 and text2

# empty.

text1.clear()




print('After removing items using clear()')

print('text1 =', text1)

print('text2 =', text2)




text1 = {1: "one", 2: "two"}

text2 = text1




# This makes only text1 empty.

text1 = {}




print('After removing items by assigning {}')

print('text1 =', text1)

print('text2 =', text2)






# Dictionary with three items

Dictionary1 = { 'A': 'dict1', 'B': 'For' }

Dictionary2 = { 'C': 'dtyjdtyj46745785','A':10 }

# Dictionary1['C'] = Dictionary2

# print(Dictionary1)




# Dictionary before Updation

print("Original Dictionary:")

print(Dictionary1)




# update the value of key 'B'

Dictionary1.update(Dictionary2)

print("Dictionary after updation:")

print(Dictionary1)



Dictionary1 = {'A':'Steve', 2:'For', 'C':'For'}

print(Dictionary1.values())

print(Dictionary1.keys())



country_code = {'India' : '0091',

                'Australia' : '0025',

                'Nepal' : '00977'}




# search dictionary for country code of India

print(country_code.get('Austria', 'Not Found'))



dict={}

a=int(input("Enter number of students :"))

for i in range(a):

    n=input("Enter the name :")

    m=int(input("Enter the marks :"))

    dic2={n:m}

    dict.update(dic2)

print(dict)

###12 class
def f1(n):

   

    if (n == 0):

        return 1

    else:

        return n * f1(n-1)

   

print the resultprint(f1(7))


string="python"

l=list(string)

t=tuple(string)

s=set(string)

print(l)

print(t)

print(s)

set1=set([1,2,3,4,1,2,3]) print("\nSet with.....

set1=set([1,2,3,4,1,2,3])

print("\nSet with the use of String: ")

print(set1)




set1 = set([1, 2, 'ouuigui', 4, 'kjyu', 6, ...])

set1 = set([1, 2, 'ouuigui', 4, 'kjyu', 6, 'lufykf'])

print("Set with the use of Mixed Values",set1)

print(set1)




set1 = set() print("Initial blank Set: ") p...

set1 = set()

print("Initial blank Set: ")

print(set1)




# Adding element and tuple to the Set

set1.add(8)

set1.add(9)

set1.add((6,7))

set1.add((10.11,))

print("\nSet after Addition of Three elements: ")

print(set1)

set1 = set() print("blank set: ") tuple = (...)

set1 = set()

print("blank set: ")

tuple = (1,2,3,4,5,6,6,4)

a=set(tuple)

print(a)

set1.add(tuple)

print(set1)

set1 = set([ 4, 5, (6, 7)]) set1.update([10...]) 

set1 = set([ 4, 5, (6, 7)])

set1.update([10, 11])

print("\nSet after Addition of elements using Update: ")

print(set1)

s = set() for i in range(16):     s.add(i*3... )

s = set()

for i in range(16):

    s.add(i*3)




print(s)

print(s.pop())

# using Remove() method set1 = set([156, 2,...
# using Remove() method

set1 = set([156, 2, 33, 4, 5, 6, 7, 6,8,5, 9, 10, 11, 12])

# set1.remove(5)

set1.remove(6)

print("\nSet after Removal of two elements: ")

print(set1)

# using Discard() method set1 = set([156, 2...

# using Discard() method

set1 = set([156, 2, 33, 4, 5, 6, 7, 8,5, 9, 10, 11, 12])

# set1.remove(55)

set1.discard(256757)

print("\nSet after Discarding two elements: ")

print(set1)




Isaac (Guest) has temporarily joined the chat.
Isaac (Guest) has temporarily joined the chat.
Isaac Sir by Isaac (Guest)
Isaac (Guest)


print("\nEmpty FrozenSet: ") print(frozense..)

print("\nEmpty FrozenSet: ")

print(frozenset())

my_set = {'fo', 'ba', 'bz', 'az', 'oo','oo'}

print(my_set)

new = frozenset(my_set)

print(new.pop())

has context menu

set1 = set()

for i in range(11,48):

    if i%2 == 0:

        set1.add(i)

print(set1)

file=open("D:\\Nikhil\\Backup\\demo12.txt",'r')

for s in file:

    print (s)

    file = open("demo.txt", "r")

print(file.read())




import os

print(os.getcwd())




file=open("D:\\Nikhil\\Backup\\demo12.txt",'r')

for s in file:

    print (s)




f=open("demo-34.txt","w")

data=f.write("\nthis is the write mode.ghjghjhjdfh56748576")

f1=open("demo.txt","r")

print(f1.read())

has context menu000


##13 class
# This is simplest Student data management program in python
 
# Create class "Student"
class Student:
 
  # Constructor
    def _init_(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
 
    # Function to create and append new student
    def accept(self, Name, Rollno, marks1, marks2):
   
  # use ' int(input()) ' method to take input from user
        ob = Student(Name, Rollno, marks1, marks2)
        ls.append(ob)
 
    # Function to display student details
    def display(self, ob):
        print("Name : ", ob.name)
        print("RollNo : ", ob.rollno)
        print("Marks1 : ", ob.m1)
        print("Marks2 : ", ob.m2)
        print("\n")
 
    # Search Function
    def search(self, rn):
        for i in range(ls._len_()):
            if(ls[i].rollno == rn):
                return i
 
    # Delete Function
    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]
 
    # Update Function
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll
 
 
# Create a list to add Students
ls = []
# an object of Student class
obj = Student('', 0, 0, 0)
 
print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")
 
# ch = int(input("Enter choice:"))
# if(ch == 1):
obj.accept("A", 1, 100, 100)
obj.accept("B", 2, 90, 90)
obj.accept("C", 3, 80, 80)
 
# elif(ch == 2):
print("\n")
print("\nList of Students\n")
for i in range(ls._len_()):
    obj.display(ls[i])
 
# elif(ch == 3):
print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])
 
# elif(ch == 4):
obj.delete(2)
print(ls._len_())
print("List after deletion")
for i in range(ls._len_()):
    obj.display(ls[i])
 
# elif(ch == 5):
obj.update(3, 2)
print(ls._len_())
print("List after updation")
for i in range(ls._len_()):
    obj.display(ls[i])
 
# else:
print("Thank You !")


def _init_(self):
        self.name = input("Enter Your Name: ")
        self.cname = input("Enter Your College Name: ")
        self.roll = int(input("Enter Your Roll Number: "))


class Temp(Student_Details):
    def display(self):
        print("============ Student Details are ==========")
        print("Name: ", self.name)
        print("College Name:", self.cname)
        print("Roll number:", self.roll)


obj1 = Temp()
obj1.display()
####
n = input("Enter name of student: ")
c = int(input("Enter class of student: "))
a = int(input("Enter age of student: "))
print("Name:", n, "Class:", c, "Age:", a)
print()
print()
print("Name:", n)
print("Class:", c)
print("Age:", a)
####
n = int(input("Enter number of students: "))

result = {}

for i in range(n):

print("Enter Details of student No.", i+1)

rno = int(input("Roll No: "))

name = input("Name: ")

marks = int(input("Marks: "))

result[rno] = [name, marks]

print(result)

# Display names of students who have got marks more than 75

for student in result:

if result[student][1] > 75:

print(result[student][0])

####
n={}

stu =int(input("no of student :"))

for i in range(stu):

  rollno = int(input("student roll_no :"))

  name = str(input("student name :"))

  subj= str(input("subj name :"))

  marks= int(input("enter the marks :"))

  subj2=str(input("subj name :"))

  marks2=int(input("enter the marrks :"))

  rollno = name    

  print(n)
  ###
  student = {}
n= int(input("enter the number of student:"))
for i in range(n):
  rollno=int(input("student rollno:"))
  name=input("name of student:")
  english=int(input("enter the english marks  : "))
  hindi=int(input("enter the hindi marks  : "))
  student[rollno]= {name :{english:hindi}}

print(student)

#####
class students:
    count = 0
    def __init__(self, name):
        self.name = name
        self.marks = []
        students.count = students.count + 1
        
    def enterMarks(self):
        for i in range(3):
            m = int(input("Enter the marks of %s in %d subject: "%(self.name, i+1)))
            self.marks.append(m)
            
    def display(self):
        print (self.name, "got ", self.marks)
             
name = input("Enter the name of Student:")
s1 = students(name)
s1.enterMarks()
s1.display()
print ("")
name = input("Enter the name of Student:")
s2 = students(name)
s2.enterMarks()
s2.display()

s2.displayCount()

#######
class Student:
    marks = []
    def getData(self, rn, name, m1, m2, m3):
        Student.rn = rn
        Student.name = name
        Student.marks.append(m1)
        Student.marks.append(m2)
        Student.marks.append(m3)
        
    def displayData(self):
        print ("Roll Number is: ", Student.rn)
        print ("Name is: ", Student.name)
        #print ("Marks in subject 1: ", Student.marks[0])
        #print ("Marks in subject 2: ", Student.marks[1])
        #print ("Marks in subject 3: ", Student.marks[2])
        print ("Marks are: ", Student.marks)
        print ("Total Marks are: ", self.total())
        print ("Average Marks are: ", self.average())
        
    def total(self):
        return (Student.marks[0] + Student.marks[1] +Student.marks[2])
    
    def average(self):
        return ((Student.marks[0] + Student.marks[1] +Student.marks[2])/3)
    
r = int (input("Enter the roll number: "))
name = input("Enter the name: ")
m1 = int (input("Enter the marks in the first subject: "))
m2 = int (input("Enter the marks in the second subject: "))
m3 = int (input("Enter the marks in the third subject: "))

s1 = Student()
s1.getData(r, name, m1, m2, m3)
s1.displayData()
#####
student = {}
n= int(input("enter the number of student:"))
for i in range(n):
  rollno=int(input("student rollno:"))
  name=input("name of student:")
  english=int(input("enter the english marks  : "))
  hindi=int(input("enter the hindi marks  : "))
  student[rollno]= {name :{english:hindi}}

print(student)
#####
student = {}
n= int(input("enter the number of student:"))
for i in range(n):
  rollno=int(input("student rollno:"))
  name=input("name of student:")
  subject= input("subject name:")
  english=int(input("enter the english marks  : "))
  subject2=input("subject name:")
  hindi=int(input("enter the hindi marks  : "))
  student[rollno]= {name :{subject:english,subject2:hindi}}

print(student)
####3


n={}

stu = int(input("enter  the no of student:"))

for i in range(stu):

  rollno = int(input("student roll_no :"))

  name = str(input("student name :"))

  subj= str(input("subj name :"))

  marks= int(input("enter the marks :"))

  subj2=input("subject name:")

  marks2=int(input("enter the marks:"))

  n[rollno]={name:{subj:marks,subj2:marks2}}

  print(n)
  ###
file = open("demo.txt", "r")
print (file.read(5))
##
#open the file
text_file = open('/Users/Ankit/abc.txt','r')

#get the list of line
line_list = text_file.readlines();

#for each line from the list, print the line
for line in line_list:
    print(line)

text_file.close() #don't forget to close the file
##


Class name :

Total Students:

Total Subjects:

Name of Subjects :

                    Msths       Eng         Hindi       CGPA      percentage        pass/fail

1       Name  

2

3




Average of the marks :

Maths :

ENg:

Hindi:




Top3

Bottom 3
## paswod
#open the file
text_file = open('/Users/Ankit Kumar singh/abc.txt','r')

#get the list of line
line_list = text_file.readlines();

#for each line from the list, print the line
for line in line_list:
    print(line)

text_file.close() #don't forget to close the file
#######################
def fun(a):

    if a <= 3:

        # throws ZeroDivisionError for a = 3

        b = a/(a-3)




    # throws NameError if a >= 4

    print("Value of b = ", b)

   

try:

    # fun(3)

    fun(5)




# note that braces () are necessary here for

# multiple exceptions

except ZeroDivisionError:

    print("Denominator becomes zero in this case.")

except NameError:

    print("NameError Occurred and Handled")
    #############################
    def f1(a , b):

    try:

        c = ((a+b) / (a-b))

    except ZeroDivisionError:

        print ("a/b result in 0")

    else:

        print (c)




# Driver program to test above function

# f1(2.0, 3.0)

f1(3.0, 3.0)
#####################
try:

    k = 5//0 # raises divide by zero exception.

    print(k)




# handles zerodivision exception

except ZeroDivisionError:

    print("infinite value")




finally:

    # this block is always executed

    # regardless of exception generation.

    print('This is always executed')
    ###############
    def divide(x, y):

    try:

            # Floor Division : Gives only Fractional Part as Answer

        result = x // y

        print("Yeah ! Your answer is :", result)

    except ZeroDivisionError:

        print("Sorry ! You are dividing by zero ")




    # Look at parameters and note the working of Program

divide(3, 2)
##################


try:

    amount = int(input("Enter the amount to be withdrawn:"))

    acc=6000

    if acc-amount < 2000:

       

        # raise the ValueError

        raise ValueError("please add money in your account")

    else:

        print("You are eligible to purchase DSA Self Paced course")

           

# if false then raise the value error

except ValueError as e:

        print(e)

finally:

    print("Thanks")




###########################





try:

    a = 10/0

    print (a)

except ArithmeticError:

        print ("This statement is raising an arithmetic exception.")

else:

    print ("Success.")






try:

    a = [1, 2, 3]

    print (a[3])

except LookupError:

    print ("Index out of bound error.")

else:

    print ("Success")
    #############
# importing required libraries

import mysql.connector as ms




dataBase = ms.connect(

host ="localhost",

user ="root",

passwd =""


)




# preparing a cursor object

cursorObject = dataBase.cursor()




# creating database

cursorObject.execute("CREATE DATABASE demo_db12")
######
# importing required library

import mysql.connector




# connecting to the database

dataBase = mysql.connector.connect(

                    host = "localhost",

                    user = "root",

                    passwd = "",

                    database = "demo_db1" )




# preparing a cursor object

cursorObject = dataBase.cursor()




# creating table

studentRecord = """CREATE TABLE STUDENT (

                NAME VARCHAR(20) NOT NULL,

                BRANCH VARCHAR(50),

                ROLL INT NOT NULL,

                SECTION VARCHAR(5),

                AGE INT

                )"""




# table created

cursorObject.execute(studentRecord)




# disconnecting from server

dataBase.close()
##############
import mysql.connector





mydb = mysql.connector.connect(

host = "localhost",

user = "root",

password = "",

database = "demo_db1"

)




mycursor = mydb.cursor()

sql = "INSERT INTO Student (Name, Branch,Roll,Section,Age) VALUES (%s, %s,%s, %s,%s)"

val = ("Ram", "85","76543","A","18")




mycursor.execute(sql, val)

mydb.commit()




print(mycursor.rowcount, "details inserted")




# disconnecting from server

mydb.close()
###############


import mysql.connector




mydb = mysql.connector.connect(

  host="localhost",

  user="root",

  password="",

  database="mydatabase"

)




mycursor = mydb.cursor()




sql = "INSERT INTO fruits (name, quantity, country) VALUES (%s, %s, %s)"

val = [

  ("Banana", 40, "Mexico"),

  ("Mango", 15, "India"),

  ("Avocado", 37, "Mexico")

]




try:  

  mycursor.executemany(sql, val)

  print(mycursor.rowcount, "records inserted.")

except:

  print('Something went wrong.')




mydb.commit()
######


def login(users):
    while true:
      username = input("please enter a username: ")
      passwod = input("please inter a password: ")

 for u in users:
   if username == u[0]:
      if password == u[1]:
              return username
  print("username or password is incorrect. please try again!")
   users = [['ankit','ank123'],['juhi','jugi456'],['prakash','par789']]
   username = login(users)

   print(username,"has logged in")

###

username = 'Ankit1234'

password = 'raja'

userInput = input("What is your username?\n")

if userInput == username:
    a=input("Password?\n")   
    if a == password:
        print("Welcome")
    else:
        print("That is the wrong password.")
else:
    print("That is the wrong username.")


    ###################



    attemps = 0

while attemps < 3:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'user123' and password == 'password123':
        print('You have successfully logged in.')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue

    #####


import random
import array

MAX_LEN = 12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

for x in range(MAX_LEN - 4):
	temp_pass = temp_pass + random.choice(COMBINED_LIST)

	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
		password = password + x
		print(password)

#########
#####Class 20/07/2023#####

# Python Program to create

# a data type object

import numpy as np

 

# First Array

arr1 = np.array([[4, 7], [2, 6]],

                 dtype = np.float64)




print(arr1)

                 

# Second Array

arr2 = np.array([[3, 6], [2, 8]],

                 dtype = np.float64)

 

# Addition of two Arrays

Sum = np.add(arr1, arr2)

print("Addition of Two Arrays: ")

print(Sum)

 

# Addition of all Array elements

# using predefined sum method

Sum1 = np.sum(arr1)

print("\nAddition of Array elements: ")

print(Sum1)

 

# Square root of Array

Sqrt = np.sqrt(arr1)

print("\nSquare root of Array1 elements: ")

print(Sqrt)


import numpy as np

arr1 = np.array([[4, 7], [2, 6]],

                 dtype = np.float64)

print(arr1)

# Transpose of Array

# using In-built function 'T'

Trans_arr = arr1.T

print("\nTranspose of Array: ")

print(Trans_arr)



import numpy as np




# making a 3x3 array

ab = np.array([[1, 2, 3],

                [4, 5, 6],

                [7, 8, 9]])




# before transpose

print(ab, end ='\n\n')




# after transpose

print(ab.transpose())





import numpy as np

print('array:',np.arange(6))

print("A\n", np.arange(4).reshape(2, 2), "\n")




print("A\n", np.arange(4, 10), "\n")




print("A\n", np.arange(4, 20, 3), "\n")


import numpy as np

array = np.arange(24).reshape(2, 2, 6)

print("\nOriginal array reshaped to 3D : \n", array)


import numpy as np

print("\nBool Value with axis = 0 : ",

    np.any([[False,False],

             [False,True]], axis = 0))


import numpy as np




# creating array

arr = np.array([2, 4, 6, 8, 10])




# assigning arr to nc

nc = arr




# both arr and nc have same id

# print("id of arr", id(arr))

# print("id of nc", id(nc))




# updating nc

nc[0]= 12




# printing the values

print("original array- ", arr)

print("assigned array- ", nc)



import numpy as np




# Creating a numpy array using np.array()

ary = np.array([13, 99, 100, 34, 65, 11,

                66, 81, 632, 44])




print("Original array: ")




# printing the Numpy array

print(ary)




# Creating an empty Numpy array similar

# to ary

copy = np.empty_like(ary)

print("kjhgf",copy)

# Now assign ary to copy

copy[:] = ary




print("\nCopy of the given array: ")




# printing the copied array

print(copy)

###############

mport numpy as np

# Integer datatype

# guessed by Numpy

x = np.array([198765, 2])  

print("Integer Datatype: ")

print(x.dtype)        

 

# Float datatype

# guessed by Numpy

import numpy as np

x = np.array([1.0, 2.0])

print("\nFloat Datatype: ")

print(x.dtype)  

 

# Forced Datatype

import numpy as np

x = np.array([1, 2], dtype = np.int16)  

print("\nForcing a Datatype: ")

print(x.dtype)
##############

import numpy as np

arr1 = np.array([[4, 7], [2, 6]],

                 dtype = np.float64)

print(arr1)

# Transpose of Array

# using In-built function 'T'

Trans_arr = arr1.T

print("\nTranspose of Array: ")

print(Trans_arr)
############
