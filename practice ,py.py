
Age = int(input('Enter the age of person:'))
if Age>0 and Age<=4:
    print("person is Toddler")
elif Age>5 and  Age<=10:
    print("Person is child")
elif Age>11 and  Age<=19:
    print("Person is teenager")
elif Age>20 and Age<=45:
    print("Person is Adult")
elif Age>46 and Age<=65:
    print("Person is Senior Adult")
elif Age>45 and Age<=65:
    print("Senior citizen")
else:
    print("no person")

#credit card
#<1000, within the deadline - no cashback
#>1000  -  <5000 - within the deadline - 1.2% upto INR 30
#>5000  -  <10000 - within the deadline - 1.5% upto INR 60
#>10000 - within the deadline - 1.5% upto INR 70
 
#deadline has passed - penalty of 10

bill = float(input("Enter the bill: "))
deadline = int(input("Enter the date:"))
if deadline <= 25:
    if bill < 1000:
        print("No cashback.")
        print("Bill to be paid is:", bill)
    elif bill > 1000 and bill <=5000:
        print("You have received a cashback of 1.2% upto INR 30.")
        cb = bill*.012
        if cb>30:
            print("You have received a cahback of INR 30")
            bill_paid = bill - cb
            print("Bill to be paid is:", bill_paid)

#person has to apply for visa
#1. Adhaar card
#2. Age > 18
#3. IELTS score > 6.5
#4. scored more than 50% in 10+2
#5. passport number

visa  = input("are you applying for visa")
if visa == "yes":
    print("you have to met conditions:")
elif visa == "no":
    print('NO ISSUE')
aadhar = input("Do you have a valid adhaar card:")
if aadhar == "yes":
    print("you are valid:")


#while/for loop

count = 50
while(count>=0):
    print("daily count",count)
    count = count-1

n = int(input("Enter the number:"))
m = int(input('Enter the ending value:'))
while n<=m:
    if n%2 == 0:
        print('it is a even number')
              
#Even numbers
n = 0
while n<=20:
     if n%2 ==0:
        print(n)
num = int(input("Enter the value :"))
if num%2 == 0:
    print(num**2)
elif num%3==0:
    print(num**3)
else:
    print(num,"not a modulus of 2 and 3")

num = int(input("Enter the value:"))
if num%2 == 0:
    print('Even:')
else:
    print('Odd')

admission = int(input("Enter the percentage you got in 12th:"))
if admission >=78:
    print("You are eligible for entrance")
else:
    print("You are not Eligible")




        #conditional statements - if, else, elif
a = int(input("Enter the value of a:"))
if a>=60:
    print("You got first division")
else:
    print("You got second division")


amt = int(input('Enter the amount:'))
if amt>=5000:
    print('The discount is 12.5%')
    disc = amt*.125
    print("The amountof discount is",disc)
    amount_payable = amt-disc
    print("The amountis to be paid is",amount_payable)
elif amt> 4000 and amt<5000:
    print('The discount is 10%')
    disc = amt*.1
    print("The amountof discount is",disc)
    amount_payable = amt-disc
    print("The amountis to be paid is",amount_payable)
else:
    print('No discount is applicable.')
    print("The amountis to be paid is",amt)

#Credit card
bill = int(input("Enter the bill:"))
Deadline = int(input("Enter the days of month:"))
if Deadline>25:
    print('you have a penalty that issued on your amount of RS10',bill+10)
    if Deadline<25:
        if bill<1000:
            print("No cashback",bill)
elif bill>1000 and bill<=5000:
    print('you got 1.2% of discount that is of Rs30.')
    cb = bill*1.2/100
    if cb<=30:
        bill_payable = bill-cb
        print('You have to be paid.',bill_payable)
elif bill>5000 and bill<=10000:
    print("You got 1.5% of discount INR 60.")
    cb = bill*1.2/100
    if cb<=60:
        bill_payable = bill-cb
        print("You have to be paid",bill_payable)
elif bill>=10000:
    print("you got 1.5% of INR 70")
    cb = bill*1.5/100
    if cb<=70:
        bill_payable = bill - cb
        print("you have to be paid.",bill_payable)
else:
    print("No Cashback")


#for loop
for i in range (20,0,-1):
    print(i)


for i in range(1,51):
    if i%13 ==0:
        continue
    print(i)

for i in range(5):
    n = int(input("Enter the number"))
    if n%3 == 0 and n%5 == 0:
        break
    print(n)



#take 10 numbers if even do square if odd cube if multiple of both 3 and 5 print those numbers
for i in range (10):
    n = int(input("Enter the value:"))
    if n%5 ==0 and n%3 ==0:
        print(n)
    elif n%2 == 0:
        print(n**2)
    elif n%3 == 0:
        print(n**3)
else:
    print("Number is not a multiple")
    



#Write a program in python to read 10 numbers from the keyboard and find their sum and average.
n = 0
sum = 0
for i in range(0,11):
    if n<=9:
        sum = sum+n  
        print(sum)
    n +=1
print(n)
    
#print terms of fibonacci series upto a certain number
n = 0
x = 1
m = 0
while n<= 20:
    n = n+x
    x = +1
    x = m
    m = n
    print(n)


#Write a C program that displays the n terms of square natural numbers and their sum.


   



#check if the number is prime or not?
n = 17
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

def f1():
    n =- 10
    while n<= 10:
        print(n)
        n = n+1
print (f1()) 

f1()


def f3(a,b):
    # return a+b
    print(a+b)
 
if f3(10,20)>25:
    print("hello")
else:
    print("bie")

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

def fun(a,b):
    print(a,b)
fun(b =30,a = 40)


#default arguments
 
def fun(a,b=10):
    print(a)
    print(b)
fun(20,50)

def f(a,b):
    print(a+b)
f(b = 3,a=4)


# function with arguments
 
#required arguments
def f1(a,b):#formal arguments
    print(a+b)
    
f1(10,20)    #actual arguments
f1(20,40)



# Example of lambda function using if-else
M = lambda a, b : a if(a > b) else b
print(M(1, 2))

 

Square = lambda x : x**2
print(Square(6))
 
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


numbers = [1, 2, 3, 4]
# print(type(numbers))
result = map(lambda x: x + x, numbers)
# print(tuple(result))
print(list(result))

n = [2,4,6,8]
result = map(lambda  x:x**2, n ) 
print(list(result))

import functools
import operator
 
# initializing list
lis = [1, 3, 5, 6, 2]
print("The sum of elements is:",end="")
print(functools.reduce(operator.add, lis))
print(functools.reduce(operator.mul,lis))


# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

#FILTER FUNCTION  = 
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False

 
# sequence
sequence = ['n', 'e', 'e', 'j', 'k', 's', 'p', 'r']
 
# using filter function
filtered = filter(fun, sequence)
 
print('The filtered letters are:')
for s in filtered:
    print(s)

def f1(variables):
    letters = ['a','e','i','o','u']
    if (variables in letters):
        return True
    else:
        return False
    
sequence = ['n','e','t','i','a','u']
filter = filter(f1,sequence)
for s in filter:
    print(s)
    




seq = [0, 1, 2, 3, 5, 8, 13]
 
# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
 
# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))


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

#input the numbers from user and print list
n = int(input("Enter the number of elements:"))
l = []
for i in range(n):
    ele = int(input("Enter the element: "))
    l.append(ele)
    
print(l)


List = [1, 2, 3, 1, 2, 1, 22, 2, 3, 2, 1]
n = int(input("Enter the element to be searched:"))
for i in range(len(List)):
    if List[i] == n:
        print(i)



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

List = [1, 2, 'Gdkj fvs', 4, 'For', 6, 'Gajv1']
print(List[2])
print("Accessing element using negative indexing")
print(List[-1])
print(List[-3])

List = [2.3, 4.445, 3, 5.33,3, 1.054, 2.5]
List.remove(3)
print(List)
del List[0]
print(List)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop(1))
print(List)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop())
print(List)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(sorted(List,reverse=True))
print(List)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
#Reverse flag is set True
List.sort(reverse = True)
#List.sort().reverse(), reverses the sorted list
print(List) 
List1 = [-1, 2, 3]
List2 = [2, 3, 4, 5]
List1.extend(List2)        
print(List1)

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(1))


list = [1,2,3,4,5,6,7,8,9]
for i in list:
    i = i-1
    print(i)

List = [1, 2, 3, 1, 2, 1, 22, 2, 3, 2, 1]
for i in range(len(List)-1,-1,-1):
    print(List[i])



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

#tuples
t = (1,2,3,4)
print(t)

tup = tuple([1,2,3,4,5])
print(tup)

a=[1,2,3]
print(type(a))

Tuple1 = ('Welcome', 7.4, 'Steve',78)
print(Tuple1)
print(Tuple1[1])
print(Tuple1.index(7.4))

Tuple2 = tuple(['python', 'greek'])
# print(type(Tuple2))
Tuple3 = (Tuple1, Tuple2)
print("Tuple with nested tuples: ")
print(Tuple3)
Tuple1=(4,) * 3
print("Tuple with repetition: ")
print(Tuple1)

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Steve', 'For', 'Steve','jhv','rthsh')
# for i in range(len(Tuple2)):
#   print(Tuple1[i])
#   print(Tuple2[i])
Tuple3 = Tuple1 + Tuple2
print(Tuple3)

 
Tuple1 = (0, 1, 2, 3, 4)
del Tuple1
print(Tuple1)

n = tuple() 
n = tuple(input("Enter the value:"))
print(n)

# Creating a String
# with single Quotes
 
String1 = 'Welcome to the Python World'
print("String with the use of Single Quotes: ")
print(String1)
 
# Creating a String
# with double Quotes
String1 = "I'm a kjdbfi"
print("\nString with the use of Double Quotes: ")
print(String1)
 
# Creating a String
# with triple Quotes
String1 = '''I'm a kjdbfi and I live in a world of "Python"'''
print("\nString with the use of Triple Quotes: ")
print(String1)
 
# Creating String with triple
# Quotes allows multiple lines
String1 = '''Python
            For
Life'''
print("\nCreating a multiline String: ")
print(String1)

String1 = "I love learning python"
print("Initial String: ")
print(String1)

String1 = "I love learning python"
print("Initial String: ")
print(String1)
 
# Printing First character
print("\nFirst character of String is: ")
print(String1[0])
 
# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])
String1 = "I love python kjhufylgjkhjliogufy"
print("Initial String: ")
print(String1)

String1 = "Hello, I'm Nikhil"
# String1 = "Hello I am Nikhil"
# print("Initial String: ")
# print(String1)
 
# Updating a character
# of the String
String1[2] = 'p'
print("\nUpdating character at 2nd Index: ")

String1 = "Hello, I'm Nikhil"
String1 = "Hello, I am Nikhil"
 
print("Initial String: ")
print(String1)

# Updating a String
String1 = "Welcome to the Python World"
print("\nUpdated String: ")
print(String1)

a="Hello, my name is \"Nikhil\""
print(a)


a="Hello, my name is \"Nikhil\""
print(a)

    # use of Escape Sequences
String1 = "C:\\Python\\tkin\\"
print("\nEscaping Backslashes: ")
print(String1)

text = "i love python"
print(text.endswith("jon"))

text = 'i love python'
 
# returns False
# result = text.endswith('on')
result1=text.startswith('i')
print (result1)

string = "this is India and i love India "
 
# counts the number of times substring occurs in
# the given string and returns an integer
print(string.count("India"))

string = "MY NAME IS NIKHIL"
str="ghetyjdgyjdjdhg"
# print lowercase string
print(str.swapcase())
print("lowercase string: ",string.casefold())
print("lowercase string: ",str.casefold())

name = "nIKHIL rana"
 
print(name.capitalize())
print(name.title())


ch = "india is a great country and i live in india india"
 
# initializing argument string
ch1 = "india"
 
# starting from 2nd index
# prints 8
pos = ch.index(ch1,2)
 
print ("The first position of india after 2nd index : ",end="")
print (pos)

string = "89#fghyj76"
print(string.isalnum())

text = 'Nikhil Rana'
 
print("Original String:")
print(text)
 
# lower() function to convert
# string to lower_case
print("\nConverted String:")
print(text.lower())
print(text.upper())

# initializing string
isupp_str = "INDIA"
not_isupp = "INa"
 
# Checking which string is
# completely uppercase
print ("Is INDIA full uppercase ? : ",isupp_str.isupper())
print ("Is india full uppercase ? : " ,not_isupp.islower())

string = "cook book hook"
print(string)

l = ['make','cake','take','bake']
f = 0
for i in l:
    if i.endswith('ake') == False:
        f = 1
        break
print(f)
if f == 0:
    print('rhyming')
else:
    print('not rhyming')



#create a list and define in alfabetic order

n = ["a","c","b","d","s","f","g","h","j","k","l"]
print(list.sort(n))

d = {1:2,3:4,5:6}
print(d[3])

Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Steve','A' : {1 : 'Steve', 2 : 'For', 3 : 'Steve'},
        'B' : {1 : 'Steve', 2 : 'Life'}}
print(Dict)
print(Dict['B'][2])


#Define a dictionary and print it with for loop.

Dict = {1:"m",2:"n",3:"k",4:"f"}
for i in Dict:
    print(i,':',Dict[i])

Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Steve',
        'A' : {8 : 'Steve', 2 : 'For', 3 : 'Steve'},
        'B' : {1 : 'Steve', 2 : 'Life'}}
# Deleting a Key value
del Dict[6]
print("Deleting a specific key: ")
print(Dict)

Dict = {1: 'Steve', 'name': 'For', 3: 'Steve'}
 
# Deleting a key
# using pop() method
pop_ele = Dict.pop(3)
print(pop_ele)
print(Dict)

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

Dictionary1 = {'A':'Steve', 2:'For', 'C':'For'}
print(Dictionary1.values())
print(Dictionary1.keys())

country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
# search dictionary for country code of India
print(country_code.get('Austria', 'Not Found'))

#take information from user of students.
roll_no= int(input("Enter the Roll no. of students:"))
d ={}
for i in roll_no:
    name = str(input("Enter the students name:"))
    marks = int(input("Enter the marks of students:"))
print(d)

#roll_no.,name,subjects, from user
student = int(input("Enter the number of students:"))
dict ={}
for i in student:
    name_st = (input("Enter the name of students:"))
    marks = float(input("Enter the marks of students:"))
    dict[name_st]= marks
print(dict)




def f1(n):

   

    if (n == 0):

        return 1

    else:

        return n * f1(n-1)

   

# print the result

print(f1(7))




set1 = set(["shdfhy", "shdrthv", "srhrths","srhrths"])

print("\nSet with the use of List: ")

print(set1)


set1 = set(["shdfhy", "shdrthv", "srhrths","srhrths"])

print("\nSet with the use of List: ")

print(set1)

set1=set((1,2,3,4,5,5))

print(set1)

set1=set([1,2,3,4,1,2,3])

print("\nSet with the use of String: ")

print(set1)

set1 = set([1, 2, 'ouuigui', 4, 'kjyu', 6, 'lufykf'])

print("Set with the use of Mixed Values",set1)

print(set1)

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

set1 = set()

print("blank set: ")

tuple = (1,2,3,4,5,6,6,4)

a=set(tuple)

print(a)

set1.add(tuple)

print(set1)
set1 = set([ 4, 5, (6, 7)])

set1.update([10, 11])

print("\nSet after Addition of elements using Update: ")

print(set1)

s = set()

for i in range(16):

    s.add(i*3)




print(s)

print(s.pop())
# using Discard() method

set1 = set([156, 2, 33, 4, 5, 6, 7, 8,5, 9, 10, 11, 12])

# set1.remove(55)

set1.discard(256757)

print("\nSet after Discarding two elements: ")

print(set1)


print("\nEmpty FrozenSet: ")

print(frozenset())

my_set = {'fo', 'ba', 'bz', 'az', 'oo','oo'}

print(my_set)

new = frozenset(my_set)

print(new.pop())


s = set ()
for i in range(11,48):
    if i%2==0:
        s.add(i)
print(s)


file = open("custom.txt","r")
print(file.read())

import os
print(os.getcwd())

f = open("custom.txt","w")
data = f.write("\n this is the write mode kjscniuwqdlm")
f1 = open("custom.txt","r")
print(f1.read())

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



file = open("demo.txt", "r")

print (file.read(5))


#username,url,password from user store in a file.

name = input("Enter the name:")
url = input("Enter the url:")
password = input("Enter the password:")
f = (name,url,password)
file.append(f)
file = open("storepassword.txt","a")
print(file.read())


with open("demo.txt") as file:

    data = file.read()

    print(data)

f1=open('demo.txt','r')

print(f1.readlines())

with open("demo12.txt", "w") as f:

    f.write("writing with 'with' keyowrd")

with open("demo.txt", "r") as file:

    data = file.readlines()

print(data)

for line in data:

    word = line.split('e')

    print (word)

#URL: SHOULD HAVE .COM, .IN - ENd Password - 8 and 20, one special character-atleast, no space
#username - no space, no special charcter, can have dot, but not consecutive dots
#email ID : @ - 1
# .com or .in at the end
#username of the email should not be less than 8 and greater than 20

URL =input("Enter the url")
m = URL.find(".com")
n = URL.find(".in")
if m >=0 or n>=0:
    print("URL is valid:")
else:
    print("URL is not valid")

username = input("Enter your user name:")
nospace = username.find("")
spc = username.isalnum()
dot = username.find("..")
if(nospace and dot is True or spc is not True):
    print("The user name is not valid")
else:
    print("The user name is valid")

Email = input("Enter your Email ID:")
atr = Email.find("@")
ate = Email.find(".com")
ate1 = Email.find(".in")
if ate or ate1 is True and  atr is True:
    print("Email is valid")
else:
    print('Email is not valid')

#r+ - It opens the file and places the pointer at the beginning of the file to read.




# w+ - It deletes all the content of the file and keeps the point at the beginning of the file.




# r+ - Creating a File (if file does not exist) If the file is not present while opening the file in ‘r+’ mode, it throws FileNotFound exception.   If the file is not present while opening the file in ‘w+’ mode, it creates new empty file.

# w+ - Reading File You can read the complete file text.    As opening file in ‘w+’ modes deletes the file content, you can not read the file.

# r+ - Writing File Content If you open file in ‘r+’ mode and try to write the content, it start writing from the beginning and overwrite the old content with new. It deletes all the old contents from the text file and save new text inside the file.has context menu
def fun(a):
    if a <= 3:
        # throws ZeroDivisionError for a = 3
        b = a/(a-3)
    # throws NameError if a >= 4
    print("Value of b = ", b)
try:
     fun(3)
    #fun(5)
# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("Denominator becomes zero in this case.")
except NameError:
    print("NameError Occurred and Handled")



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
    def divide(x, y):
        try:
             # Floor Division : Gives only Fractional Part as Answer
            result = x // y
            print("Yeah ! Your answer is :", result)
        except ZeroDivisionError:
            print("Sorry ! You are dividing by zero ")
    # Look at parameters and note the working of Program
divide(3, 2)

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

a = int(input("Enter the number"))
for i in a:
    i = a%2 !=0
    print("It is prime",a)
try:
    a
except ArithmeticError:
    print("this statement rise a arthmetic error")
else:
    print("success.")

#making an home fully furnished
#two bedroom
#land cost
#per square feet.
#2 bhk two bedroom price
#raw and labour cost
#paint furniture cost
#use of functions
#functions cost to build a housr land cost - static material raw material -  electric appliances

#product jeans tshirst shirts trousers casual formal pajamas
# reward points  discounts
    #membership
    #5%
    #reward points
    #birthday month, anniversary month
    #2%

###################### 13/07/2023  numpy     ###################
##################### new terminal pip install numpy #######################

import numpy as np
 
# Defining Array 1
a = np.array([[1, 2],
              [3, 4]])
# print(a)
 
# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])
               
# Adding 1 to every element
print ("Adding 1 to every element:", a + 1)
 
# Subtracting 2 from each element
print ("\nSubtracting 2 from each element:", b - 2)
 
# sum of array elements
# Performing Unary operations
print ("\nSum of all array "
       "elements: ", a.sum())
 
# Adding two arrays
# Performing Binary operations
print ("\nArray product:\n", a * b)
print ("\nArray product:\n", a + b)
########################
import numpy as np
arr = np.array([1,2,3,4,5])
for i in arr:
    if i%2 == 0:
        print(i)
####################
import numpy as np 
a = np.array([1,2,3,4,5,6,7,8])
for i in arr:
    n = a%2==0
    print("\neven numbers",n)

###############
import numpy as np
# Integer datatype
# guessed by Numpy
x = np.array([198765, 2])  
print("Integer Datatype: ")
print(x.dtype)        
 ################
# Float datatype
# guessed by Numpy
import numpy as np
x = np.array([1.0, 2.0])
print("\nFloat Datatype: ")
print(x.dtype)  
 ################
# Forced Datatype
import numpy as np
x = np.array([1, 2], dtype = np.int16)  
print("\nForcing a Datatype: ")
print(x.dtype)

#######################
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
####################################
import numpy as np
arr1 = np.array([[4, 7], [2, 6]],
                 dtype = np.float64)
print(arr1)
# Transpose of Array
# using In-built function 'T'
Trans_arr = arr1.T
print("\nTranspose of Array: ")
print(Trans_arr)
###############
import numpy as np
# making a 3x3 array
ab = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
# before transpose
print(ab, end ='\n\n')
# after transpose
print(ab.transpose())



# making a 3x3 array
ab = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
# before transpose
print(ab, end ='\n\n')
# after transpose
print(ab.transpose())
  ################
import numpy as np
print('array:',np.arange(6))
print("A\n", np.arange(4).reshape(2, 2), "\n")
print("A\n", np.arange(4, 10), "\n")
print("A\n", np.arange(4, 20, 3), "\n")
#################
import numpy as np
array = np.arange(24).reshape(2, 2, 6)
print("\nOriginal array reshaped to 3D : \n", array)

######################
import numpy as np 
array = np.array(8).reshape(2, 2, 2)
print("\nOriginal array reshaped to 3D : \n", array)
#######################
import numpy as np
array = np.arange(24).reshape(2, 2, 6)
print("\nOriginal array reshaped to 3D : \n", array)
##################
import numpy as np
print("\nBool Value with axis = 0 : ",
    np.any([[False,False],
             [False,True]], axis = 0))
#######################
import numpy as np
# creating array
ary = np.array([2, 4, 6, 8, 10])
# assigning arr to nc
nc = ary
# both arr and nc have same id
# print("id of arr", id(arr))
# print("id of nc", id(nc))
# updating nc
nc[0]= 12
# printing the values
print("original array- ", ary)
print("assigned array- ", nc)


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

#######################
# importing Numpy package
import numpy as np
 
# Creating a numpy array using np.array()
org_array = np.array([1.54, 2.99, 3.42, 4.87, 6.94,8.21, 7.65, 10.50, 77.5])
 
print("Original array: ")
 
# printing the Numpy array
print(org_array)
 
# Now copying the org_array to copy_array
# using np.copy() function
copy_array = np.copy(org_array)
 
print("\nCopied array: ")
 
# printing the copied Numpy array
print(copy_array)
###############
import numpy as np
 
# creating an array
arr1 = np.array([1, 2, 3])
print('First array is : ', arr1)
 
# creating another array
arr2 = np.array([4, 5, 6])
print('Second array is : ', arr2)
 
# appending arr2 to arr1
arr = np.append(arr1, arr2)
print('Array after appending : ', arr)
##############
import numpy as np
# create an array
arr = np.arange(1, 13).reshape(2, 6)
print('Original Array')
print(arr, '\n')
# create another array which is
# to be appended column-wise
col = np.arange(5, 11).reshape(2, 3)
print('Array to be appended column wise')
print(col)
arr_col = np.append(arr, col, axis = 1)
print('Array after appending the values column wise')
print(arr_col, '\n')
# create an array which is
# to be appended row wise
row = np.array([1, 2,3,4,5,6]).reshape(1, 6)
print('Array to be appended row wise')
print(row)
arr_row = np.append(arr, row, axis = 0)
print('Array after appending the values row wise')
print(arr_row)

###############3
import numpy as np
print(np.zeros((3,3)))
print(np.ones((3,3)))
print(np.ones((3,3),dtype=bool))
print(np.zeros((3,3), dtype=bool))
#################
import numpy as np
arr = np.array([0, 11, 22, 23, 4, 52, 60, 7, 8, 9])
# for i in arr:
#     if i%2==1:
#         print(i)
# print(arr[arr % 2 ==0])
 
# How to replace items that satisfy a condition with another value in numpy array?
 
arr[arr % 2==1] = -1
print(arr)

########################3
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
for i in arr:
    if i%2 ==1:
         print(np.array.__init__())

###################
import numpy as np
arr = np.arange(5,20,2)
print(arr)
out = np.where(arr % 2 == 1, -1, arr)
print(out)
print(arr)
    
#####################
import numpy as np
a = np.arange(40).reshape(-1,5)
print(a)
b = np.repeat(2, 10).reshape(2,-1)
print(b)
print(np.vstack([a, b]))
######################
import numpy as np
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print(np.hstack([a, b]))
###################
import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.intersect1d(a,b))

###################
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
print(np.setdiff1d(b,a))
####################################
import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.where(a == b))
 #####################
# How to extract all numbers between a given range from a numpy array?
import numpy as np
a = np.arange(15)
print(a)
# Method 1
index = np.where((a >= 6) & (a <= 10))
print(a[index])
# Method 2:
import numpy as np
index = np.where(np.logical_and(a>=5, a<=10))
print(a[index])
#> (array([6, 9, 10]),)
# Method 3:
print(a[(a >= 5) & (a <= 10)])

########################## 24/07/2023   pandas ##############################
########################### new terminal pip install pandas#########################

import pandas as pd
import numpy as np
# Creating empty series
ser = pd.Series()
# print(ser)
# simple array
data = np.array(['xdfh','zdty' 'k', 's','Est'])
ser = pd.Series(data)
print(ser)
###############

import pandas as pd
# Calling DataFrame constructor
df = pd.DataFrame()
# print(df)
# list of strings
lst = ['conor', 'For', 'conor', 'is', 'for', 'conor']
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)
#############
    # import pandas as pd
import pandas as pd
# list of strings
lst = ['Steve', 'For', 'Steve', 'is','for', 'Steve']
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)
###############
import pandas as pd
# # intialise data of lists.
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
# # Create DataFrame
df = pd.DataFrame(data)
# # Print the output.
print(df)
      
###############
import pandas as pd
# # Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
# # Convert the dictionary into DataFrame
df = pd.DataFrame(data)
print(df)
# # select two columns
print(df[['Name', 'Qualification']])
 ##############
import os
print(os.getcwd())
##############   file as  nba.csv#############
import pandas as pd
# # making data frame from csv file
data = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\nba.csv.csv')
# data = pd.read_csv(r"DAProjects\nba1.csv", index_col ="Name")
print(data)
######################
import pandas as pd
# # making data frame from csv file
data = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\nba.csv.csv',index_col='Name')
# data = pd.read_csv(r"DAProjects\nba1.csv", index_col ="Name")
print(data)
# # retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]

print(first, "\n\n\n", second)
############################
import pandas as pd
data = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\nba.csv.csv',index_col = 'Age')
print(data)
first = data.loc[23]
print(first)
####################### 25/7/2023###################

import pandas as pd
# # making data frame from csv files
data = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\nba.csv.csv',index_col = 'Age')
print(data)
Age = data.iloc[4]
print(Age)
####################
import pandas as pd

data = pd.read_csv('pokemon.csv')
print(data)

############
import pandas as pd
# importing numpy as np
import numpy as np
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
print(df)
################ 1st uper wala
# filling missing value using fillna()  
print(df.fillna(0))
############## fir print(df.fillna(0)) ke sath me karna hai.

import pandas as pd
# importing numpy as np
import numpy as np
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score':[52, 40, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, 65]}
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
print(df)
# using dropna() function  
print(df.dropna())
######################
import pandas as pd
# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
                'Height': [5.1, 6.2, 5.1, 5.2],
                'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
# Declare a list that is to be converted into a column
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
# Using 'Address' as the column name
# and equating it to the list
df['Address'] = address
# Observe the result
print(df)

####################
import pandas as pd
# making data frame from csv file
data = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\nba.csv.csv', index_col ="Name" )
print(data)
# dropping passed columns
data.drop(["Team", "Weight"], axis = 1, inplace = True)
# display
print(data)
##################
import pandas as pd
# dataframe of height and weight football players
df = pd.DataFrame({
    'Height': [167, 175, 170, 186, 190, 188, 158, 169, 183, 180],
    'Weight': [65, 70, 72, 80, 86, 94, 50, 58, 78, 85],
    'Team': ['A', 'A', 'B', 'B', 'B', 'C', 'A', True, 'B', 'C']
})
# display the dataframe
print(df)
df.drop(df.index[df['Team'] == True], inplace=True)
print(df)
#####################  file as [pokemon]################
    # importing Pandas library
import pandas as pd
print(pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\pokemon.csv'))
import os
print(os.getcwd())
print(pd.read_csv(filepath_or_buffer = r'E:\Croma campus traning $developer (p) ltd\Python\pokemon.csv'))
# makes the passed rows header
print(pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\pokemon.csv', header =[0]))
# # make the passed column as index instead of 0, 1, 2, 3....
print(pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\pokemon.csv', index_col ='Type'))
# uses passed cols only for data frame
print(pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\pokemon.csv', usecols =["Type"]))

    # skips the passed rows in new series
import pandas as pd
print(pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\pokemon.csv',skiprows = [1, 2, 3, 4]))
###########################
# # importing pandas as pd
import pandas as pd
# list of name, degree, score
nme = ["aparna", "nikhil", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]
# dictionary of lists
dict = {'name':nme, 'degree': deg, 'score':scr}

df = pd.DataFrame(dict)
# saving the dataframe
df.to_csv('E:\Croma campus traning $developer (p) ltd\Python\Bhai_Ankit.csv')
######################################
import pandas as pd
# list of name, degree, score
nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]
 
# dictionary of lists
dict = {'name': nme, 'degree': deg, 'score': scr}
   
df = pd.DataFrame(dict)
 
# saving the dataframe
df.to_csv('E:\Croma campus traning $developer (p) ltd\Python\Bhai_Ankit.csv', header=False, index=False)

#######################
import pandas as pd
# list of name, degree, score
nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]
# dictionary of lists
dict = {'name': nme, 'degree': deg, 'score': scr}
df = pd.DataFrame(dict)
# saving the dataframe
df.to_csv('E:\Croma campus traning $developer (p) ltd\Python\Bhai_Ankit.csv', header=False, index=False)
###############
import pandas as pd
# making data frame
data = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\nba.csv.csv')
# calling head() method
# storing in new variable
data_top = data.head()
data_tail = data.tail(7)
# display
print(data_top)
print(data_tail)

####################### MEAN AND MEDIAN ##########
import pandas as pd

import statistics as st

data=pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\nba.csv.csv')

print(data)

data.dropna(inplace=True)

mean=st.mean(data['Salary'])

med=st.median(data["Salary"])

print(f'mean = {mean}')

print(f'median = {med}')
########################

import pandas as pd
# making data frame
data = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\nba.csv.csv')
# number of rows to return
n = 9
# creating series
series = data["Name"]
# returning top n rows
top = series.head(n)
# display
print(top)
##########################
    # importing pandas module
import pandas as pd
# importing regex module
# import re
# making data frame
data = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\nba.csv.csv')
# removing null values to avoid errors
data.dropna(inplace = True)
print(data.describe())


######## pahale wper walaa bad me niche wal###########
# percentile list
perc =[.20, .40, .60, .80]
# list of dtypes to include
include =['object', 'float', 'int']
# calling describe method
desc = data.describe(include = include,percentiles=perc)
# display
print(desc)

#####################26/07/2023##########################

import pandas as pd

# making data frame from csv file

data = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\nba.csv.csv', index_col ="Name" )

# dropping passed values

data.drop(["Avery Bradley", "John Holland", "R.J. Hunter"], inplace = True)

# display

print(data)
################################
import pandas as pd
# read csv file

data = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\nba.csv.csv')

data.dropna(inplace = False)

# creating DataFrame form weight column

abc = pd.DataFrame(data['Weight'].head())

# providing dtype

print(abc.to_numpy(dtype ='float32'))

######################## ##PIP INSTALL METLPOTLIB  ####################

# importing matplotlib module

from matplotlib import pyplot as plt

# x-axis values

x = [5, 2, 9, 4, 7]

# Y-axis values

y = [10, 5, 8, 4, 2]

# Function to plot

plt.plot(x,y)
# function to show the plot
plt.show()  

###################

from matplotlib import pyplot as plt

# x-axis values

x = [5, 2, 9, 4, 7]

# Y-axis values

y = [10, 5, 8, 4, 2]

# Function to plot the bar

plt.bar(x,y)

# function to show the plot

plt.show()
#############################

import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'C':20, 'C++':15, 'Java':30,'Python':35}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(courses, values, color ='brown',width = 0.5)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

#############################

import matplotlib.pyplot as plt

labels = ['Python', 'C++', 'Ruby', 'Java','a','b','c']

sizes = [215, 130, 245, 210,340,547,120]

# Plot

plt.pie(sizes, labels=labels,autopct='%1.2f%%', shadow=False, startangle=60)

# plt.axis('equal')

plt.show()
########################
import matplotlib.pyplot as plt

labels = ['Python', 'C++', 'Ruby', 'Java','a','b','c']

sizes = [215, 130, 245, 210,340,547,120]

# Plot

plt.pie(sizes, labels=labels,autopct='%1.2f%%', shadow=True, startangle=90)

# plt.axis('equal')

plt.show()
###################
import matplotlib.pyplot as plt
x = [5, 7, 8, 7, 2, 17, 2, 9, 
     4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 100, 86, 
     103, 87, 94, 78, 77, 85, 86]
plt.scatter(x, y)
# to show the plot
plt.show()
################
import matplotlib.pyplot as plt
# Dataset-1
x1 = [88, 33, 45, 67, 89, 45, 23, 88, 100, 89]
y1 = [12, 34, 56, 78, 90, 22, 44, 55, 66, 77 ]
#Dataset-2
x2 = [23, 44, 34, 43, 76, 98, 78, 97, 96, 95]
y2 = [56, 68, 65, 98, 56, 74, 94, 79, 26, 69]

plt.scatter(x1, y1, c ="blue", linewidths = 2, marker ="s", edgecolor ="green", s = 50)
plt.scatter(x2, y2, c ="yellow", linewidths = 2, marker ="^", edgecolor ="red", s = 200)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
#####################3

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\nba.csv.csv')
name = data['Name'].head(10)
age = data['Age'].head(10)

plt.bar(name,age)
plt.show()
#################

import matplotlib.pyplot as plt

fig = plt.figure()
#[left, bottom, width, high]
ax = plt.axes([0.1, 0.1, 0.8, 0.8])
print(ax)
#################

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.axis([0, 6, 0, 20])
plt.show()
################
import matplotlib.pyplot as plt
#year contains the x-axis values
#and e-india & e- bangladesh
#are the y-axis value for plotting
year = [1972, 1982, 1992, 2002, 2012]
e_india = [100.6, 158.61, 305.54, 394.96, 724.79]
e_bangladesh = [10.5, 25.21, 58.65, 119.27, 224.87]
#plotting of x-axis (year) and
#y-axis(power consumption)
#with diffrent colored lables of two countries
plt.plot(year, e_india, color ='orange', label ='india')
plt.plot(year, e_bangladesh, color ='g', label ='bangladesh')
#naming of x-axis and y- axis
plt.xlabel('years')
plt.ylabel('power consumption in kWh')
#naming the tittle of the plot
plt.title('Electricity consumption per capita\of india and bangladesh')
plt.legend()
plt.show()
###################### 27/07/2023########################

# importing library import matplotlib.pyplot
# importing library

import pandas as pd
from matplotlib import pyplot as plt

# Read csv into pandas
data = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\car.csv')
print(data.head())
df = pd.DataFrame(data)

name = df['car'].head(12)
price = df['price'].head(12)

#figure Size
fig = plt.figure(figsize =(5, 7))

#horizontal Bar plot
plt.bar(name[0:10], price[0:10])
#show plot
plt.show()
########################3

import matplotlib.pyplot as plt

import numpy as np

# Data for plotting

x = np.arange(0.0, 2.0, 0.01)

# print(x)

y = 1 + np.sin(2 * x)

z = 14-np.tan(4+x)

# Creating 6 subplots and unpacking the output array immediately

fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3,2)

# fig, ((ax1, ax2, ax3),(ax4, ax5, ax6)) = plt.subplots(2,3)

ax1.plot(x, y, color="orange")

ax2.plot(x, z, color="green")

ax3.plot(z, y, color="blue")

ax4.plot(y, z, color="magenta")

ax5.plot(x, y, color="black")

ax6.plot(x, y, color="red")

plt.show()

#######################
#importng packages

import numpy as np

import matplotlib.pyplot as plt

# create data

x=np.array([1, 2, 3, 4])

# making subplots

fig, ax = plt.subplots(2, 2)

# set data with subplots and plot

ax[0, 0].plot(x, x)

ax[0, 1].plot(x, x*2)

ax[1, 0].plot(x, x*x)

ax[1, 1].plot(x, x*x*x)


# set the title to subplots

ax[0, 0].set_title("Linear")

ax[0, 1].set_title("Double")

ax[1, 0].set_title("Square")

ax[1, 1].set_title("Cube")


# set spacing

fig.tight_layout()

plt.show()

##########################
# importing packages import numpy as np import
# importing packages

import numpy as np

import matplotlib.pyplot as plt

# create data

x=np.array([1, 2, 3, 4])
# making subplots

fig, ax = plt.subplots(2, 2)

# set data with subplots and plot

title = ["Linear", "Double", "Square", "Cube"]

y = [x, x*2, x*x, x*x*x]

for i in range(4):

    # subplots

    plt.subplot(2, 2, i+1)

    # ploting (x,y)

    plt.plot(x, y[i])

    # set the title to subplots

    plt.gca().set_title(title[i])

# set spacing

fig.tight_layout()

plt.show()
##############################

import matplotlib.pyplot as plt

import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))


x1 = [1, 2, 3, 4, 5, 6]

y1 = [45, 34, 30, 45, 50, 38]

y2 = [36, 28, 30, 40, 38, 48]

labels = ["student 1", "student 2"]

fig.suptitle(' Student marks in different subjects ', fontsize=30)

# Creating the sub-plots.

l1 = ax1.plot(x1, y1, '^--', color='g')

l2 = ax2.plot(x1, y2, 'o-')

fig.legend([l1, l2], labels=labels, loc="lower left")

# plt.subplots_adjust(left=0.9)
plt.show()

################

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(2, 2)
fig.suptitle('** Main Title for all sub plots **', fontsize=20)
plt.style.use('seaborn')

labels = ['first line', 'second line',
        'third line', 'fourth line', 'fifth line']


ax[0, 0].plot([1, 2, 3, 4, 5], [9, 3, 5, 7, 9], '-.', color='g')
ax[0, 0].set_title('first subplot')
ax[0, 0].set_yticks(np.arange(1, 10))


ax[0, 1].plot([1, 2, 3, 4, 5, 6], [1, 4, 9, 7, 9, 8], '-*', color='m')
ax[0, 1].set_title('second subplot')
ax[0, 1].set_yticks(np.arange(1, 10))


ax[1, 0].plot([1, 2, 3, 4, 5], [8, 5, 2, 3, 3], '-v', color='r')
ax[1, 0].set_title('third subplot')
ax[1, 0].set_yticks(np.arange(1, 9))


ax[1, 1].plot([1, 2, 3, 4, 5, 6], [1, 3, 5, 7, 9, 6], 'o-', color='b')
ax[1, 1].plot([1, 2, 3, 4, 5, 6, 7, 7], [7, 8, 6, 5, 2, 2, 4, 6], 'o-', color='g')
ax[1, 1].set_title('fourth subplot')
ax[1, 1].set_yticks(np.arange(1, 10))


fig.tight_layout()
fig.legend(ax, labels=labels, loc="upper right", borderaxespad=0.1)
fig.subplots_adjust(top=0.85)

plt.show()

###################  PIP INSTALL SEABORN###################31/07/2023

import matplotlib.pyplot as plt

import seaborn as sns

# print(sns.get_dataset_names())

# loading dataset

data = sns.load_dataset("iris")

# print(data)

# draw lineplot

sns.lineplot(x="sepal_length", y="sepal_width", data=data)

plt.show()
#####################
import seaborn as sns

import matplotlib.pyplot as plt

# loading dataset

data = sns.load_dataset("iris")

# draw lineplot

sns.lineplot(x="sepal_length", y="sepal_width", data=data)

# setting the title using Matplotlib

plt.title('Title using Matplotlib Function')

plt.show()
####################
# importing packages

import seaborn as sns

import matplotlib.pyplot as plt
# loading dataset

data = sns.load_dataset("iris")
# draw lineplot

sns.lineplot(x="sepal_length", y="sepal_width", data=data)

# setting the x limit of the plot

# plt.xlim(2)

# plt.ylim(1)

plt.show()
########################## ye vs code me nahi chalta hai sirf jupyter me chlega ####################
import seaborn as sns

import matplotlib.pyplot as plt
# loading dataset

data = sns.load_dataset("iris")
# draw lineplot

sns.lineplot(x="sepal_length", y="sepal_width", data=data)
# changing the theme to dark

sns.set_style("darkgrid")

plt.show()
#######################
import seaborn as sns

import matplotlib.pyplot as plt
# load the tips dataset present by default in seaborn

tips = sns.load_dataset('tips')

# print(tips)

sns.set_style('white')
# make a countplot

sns.countplot(x ='sex', data = tips)
plt.show()
################
import seaborn as sns

import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# print(tips)

sns.set_style('ticks')

sns.countplot(x ='sex', data = tips, palette = 'deep')

plt.show()
###########
import seaborn as sns

import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

sns.set_context('poster', font_scale = 0.5)

sns.countplot(x ='sex', data = tips, palette ='coolwarm')

plt.show()

 #########################

import seaborn as sns

import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

sns.set_context('paper', font_scale = 2)

sns.countplot(x ='sex', data = tips, palette ='coolwarm')

plt.show()
###############
import seaborn as sns

import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

sns.set_context('notebook', font_scale = 2)

sns.countplot(x ='sex', data = tips, palette ='coolwarm')

plt.show()
####################
import seaborn as sns

import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

sns.set_context('talk', font_scale = 2)

sns.countplot(x ='sex', data = tips, palette ='coolwarm')

plt.show()
##############################
import seaborn as sns

import matplotlib.pyplot as plt

# loading dataset

data = sns.load_dataset("iris")


# draw lineplot

sns.lineplot(x="sepal_length", y="sepal_width", data=data)

# Removing the spines

sns.despine()

plt.show()
##############
import seaborn as sns

import matplotlib.pyplot as plt

# loading dataset

data = sns.load_dataset("iris")

# changing the figure size

plt.figure(figsize = (6,4))

# draw lineplot

sns.lineplot(x="sepal_length", y="sepal_width", data=data)
# Removing the spines

sns.despine()
plt.show()
####################3
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
# current colot palette
palette = sns.color_palette("colorblind")
# plots the color palette as a
# horizontal array
sns.palplot(palette)
plt.show()
#####################
import seaborn
import matplotlib.pyplot as plt
# loading of a dataframe from seaborn
df = seaborn.load_dataset('tips')
# Form a facetgrid using columns with a hue
graph = seaborn.FacetGrid(df, col ="sex", hue ="day")
# map the above form facetgrid with some attributes
graph.map(plt.bar, "total_bill", "tip").add_legend()
# show the object
plt.show()
#############
import seaborn

import matplotlib.pyplot as plt
# loading of a dataframe from seaborn

df = seaborn.load_dataset('tips')
# Form a facetgrid using columns with a hue

graph = seaborn.FacetGrid(df, row ='smoker', col ='time')

# map the above form facetgrid with some attributes

graph.map(plt.hist, 'total_bill', bins = 15, color ='orange')

# show the object

plt.show()
###############
import seaborn

# print(sns.get_dataset_names())

import matplotlib.pyplot as plt
seaborn.set(style='whitegrid')

fmri = seaborn.load_dataset("fmri")

# print(fmri)
seaborn.boxplot(x="timepoint",

                y="signal",

                data=fmri)

plt.show()
###################
# importing the required module

import seaborn

import matplotlib.pyplot as plt

# use to set style of background of plot

seaborn.set(style="whitegrid")
# loading data-set

tip = seaborn.load_dataset("tips")

seaborn.boxplot(x = 'day', y = 'tip',

                data = tip,

                linewidth=2.5)

plt.show()
######################################### 31/08/2023 ########### INDIAN FLAG #################################################
import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch
#Plotting the tri colours in national flag
a = patch.Rectangle((0,1), width=12, height=2, facecolor='green', edgecolor='grey')
b = patch.Rectangle((0,3), width=12, height=2, facecolor='white', edgecolor='grey')
c = patch.Rectangle((0,5), width=12, height=2, facecolor='#FF9933', edgecolor='grey')
m,n = py.subplots()
n.add_patch(a)
n.add_patch(b)
n.add_patch(c)
#AshokChakra Circle
radius=0.8
py.plot(6,4, marker = 'o', markerfacecolor = '#000088ff', markersize = 9.5)
chakra = py.Circle((6, 4), radius, color='#000088ff', fill=False, linewidth=7)
n.add_artist(chakra)
#24 spokes in AshokChakra
for i in range(0,24):
   p = 6 + radius/2 * np.cos(np.pi*i/12 + np.pi/48)
   q = 6 + radius/2 * np.cos(np.pi*i/12 - np.pi/48)
   r = 4 + radius/2 * np.sin(np.pi*i/12 + np.pi/48)
   s = 4 + radius/2 * np.sin(np.pi*i/12 - np.pi/48)
   t = 6 + radius * np.cos(np.pi*i/12)
   u = 4 + radius * np.sin(np.pi*i/12)
   n.add_patch(patch.Polygon([[6,4], [p,r], [t,u],[q,s]], fill=True, closed=True, color='#000088ff'))
py.axis('equal')
py.show()
######################### 01/08/2023 ################## TUESDAY ##################
import statistics as st
# initializing list

li = [1, 2, 3, 3, 2, 2, 2, 1]

# using mean() to calculate average of list

# elements

print ("The average of list values is : ",end="")

print (st.mean(li))
#################
import statistics
# simple list of a set of integers

set1 = [1, 3, 3, 4, 5, 7]

# Print median of the data-set
# Median value may or may not

# lie within the data-set

print("Median of the set is % s"

    % (statistics.median(set1)))

# Print low median of the data-set

print("Low Median of the set is % s "

    % (statistics.median_high(set1)))
########################

from statistics import mode

# Importing fractions module as fr

# Enables to calculate harmonic_mean of a

# set in Fraction

from fractions import Fraction as fr

# tuple of positive integer numbers

data1 = (2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 7)

# tuple of a set of floating point values

data2 = (2.4, 1.3, 1.3, 1.3, 2.4, 4.6)

# tuple of a set of fractional numbers

data3 = (fr(1, 2), fr(1, 2), fr(10, 3), fr(2, 3))

# tuple of a set of negative integers

data4 = (-1, -2, -2, -2, -7, -7, -9)

# tuple of strings

data5 = ("red", "blue", "black", "blue", "black", "black", "brown")

# Printing out the mode of the above data-sets

print("Mode of data set 1 is % s" % (mode(data1)))

print("Mode of data set 2 is % s" % (mode(data2)))

print("Mode of data set 3 is % s" % (mode(data3)))

print("Mode of data set 4 is % s" % (mode(data4)))

print("Mode of data set 5 is % s" % (mode(data5)))
########################
# Sample Data

arr = [1, 2, 3, 4, 5]

#Finding Max
Maximum = max(arr)

# Finding Min
Minimum = min(arr)
# Difference Of Max and Min

Range = Maximum-Minimum

print("Maximum = {}, Minimum = {} and Range = {}".format(

    Maximum, Minimum, Range))
##########################
# Variance

# It is defined as an average squared deviation from the mean. It is being calculated by finding the difference between every data point and the average which is also known as the mean, squaring them, adding all of them, and then dividing by the number of data points present in our data set.

# The variance is a measure of variability. It is calculated by taking the average of squared deviations from the mean. Variance tells you the degree of spread in your data set. The more spread the data, the larger the variance is in relation to the mean.

# Python code to demonstrate variance()

# function on varying range of data-types

# importing statistics module

from statistics import variance

# importing fractions as parameter values

from fractions import Fraction as fr

# tuple of a set of positive integers

# numbers are spread apart but not very much

sample1 = (1, 2, 5, 4, 8, 9, 12)

# tuple of a set of negative integers

sample2 = (-2, -4, -3, -1, -5, -6)

# tuple of a set of positive and negative numbers

# data-points are spread apart considerably

sample3 = (-9, -1, -0, 2, 1, 3, 4, 19)

# tuple of a set of fractional numbers

sample4 = (fr(1, 2), fr(2, 3), fr(3, 4),

        fr(5, 6), fr(7, 8))

# tuple of a set of floating point values

sample5 = (1.23, 1.45, 2.1, 2.2, 1.9)

# Print the variance of each samples

print("Variance of Sample1 is % s " % (variance(sample1)))

print("Variance of Sample2 is % s " % (variance(sample2)))

print("Variance of Sample3 is % s " % (variance(sample3)))

print("Variance of Sample4 is % s " % (variance(sample4)))

print("Variance of Sample5 is % s " % (variance(sample5)))
############################################## 02/08/2023 ###### WEDNESDAY #######################################################
import statistics

# initializing list

li = [1.5, 2.5, 2.5, 3.5, 3.5, 3.5]

# using variance to calculate variance of data

print ("The variance of data is : ",end="")

print (statistics.variance(li))

# using pvariance to calculate population variance of data

print ("The population variance of data is : ",end="")

print (statistics.pvariance(li))

#####################

import statistics

# initializing list

li = [1.5, 2.5, 2.5, 3.5, 3.5, 3.5]

# using stdev to calculate standard deviation of data

print ("The standard deviation of data is : ",end="")

print (statistics.stdev(li))
########################
df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis=1)

################################
df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price" })
df.head()
#################
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
###############
df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape
#############

import pandas as pd

import numpy as np

import seaborn as sns                       #visualisation

import matplotlib.pyplot as plt             #visualisation

     

sns.set(color_codes=True)

 

df = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\car data set.csv')

# To display the top 5 rows

df.head(5)    

 

df.tail(5)  

df.dtypes

df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis=1)

df.head(5)

df.dtypes

df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price" })

df.head()

df.shape

df.count()  

df = df.drop_duplicates()

df.head(25)

df.count()

# print(df.isnull())

print(df.isnull().sum())

df = df.dropna()    # Dropping the missing values.

df.count()

print(df.isnull().sum())

Q1 = df.quantile(0.25)

Q3 = df.quantile(0.75)

IQR = Q3 - Q1

print(IQR)
######################################################## 03/08/2023 ########  THU   #################################
import pandas as pd
df = pd.DataFrame(

    [['abc', 22, 22.6],

    ['xyz', 25, 23.2],

    ['pqr', 31, 30.5]],

    columns=['name', 'age', 'bmi'])

result = df.select_dtypes(include='number')

print(result)
#######################




