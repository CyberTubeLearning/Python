 
 
                                       ##Tuples 
 
##1. Write a python program to traverse all the elements of a tuple using a loop. 
name = [('Ankit',7058,98.45),
		('Anshul',7059,90.67),
		('Parkash',7060,78.90),
		('rohit',7081,67.89),
		('Juhi',7084,98.01)]

# iterate using for loop
for x in name:

# iterate in each tuple element
 for y in x:
 	print(y)
	
print()

##2. Write a python program to create a tuple of only one item. 
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)

##3. Write a python program to unpack a tuple in different variables. 
a = ("Ankit Bihar", 5000, "Engineering")

(college, student, type_ofcollege) = a

# print college name
print(college)

# print no of student
print(student)

# print type of college
print(type_ofcollege)

##4. Write a python program to create a tuple from a list. 
def convert(list):
	return tuple(list)

# Driver function
list = [1, 2, 3, 4]
print(convert(list))

##5. # Python3 program to convert a
# list into a tuple
def convert(list):
	return tuple(list)

# Driver function
list = [1, 2, 3, 4]
print(convert(list))


##6. Write a python program to print the modulus of the elements of a tuple. 
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

# Printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple modulo
# using zip() + generator expression
res = tuple(ele1 % ele2 for ele1, ele2 in zip(test_tup1, test_tup2))

# Printing result
print("The modulus tuple : " + str(res))

##7. Write a python program to reverse a tuple. 
def Reverse(tuples):
	new_tup = tuples[::-1]
	return new_tup
	
# Driver Code
tuples = ('z','a','d','f','g','e','e','k')
print(Reverse(tuples))

##8. Write a python program to copy specific values of one tuple to another. 
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)

# Creating a Tuple
# with the use of string
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

# Creating a Tuple
# with the use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)

##9. Write a python program to count the frequency of elements of a tuple. 
from collections import defaultdict

# initializing tuple
test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)

# printing original tuple
print("The original tuple is : " + str(test_tup))

res = defaultdict(int)
for ele in test_tup:
	
	# incrementing frequency
	res[ele] += 1

# printing result
print("Tuple elements frequency is : " + str(dict(res)))

##10. Write a python program to print second element from the last of a tuple.
 # Python3 code to demonstrate
# get nth tuple element from list
# using list comprehension

# initializing list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension to get names
res = [lis[1] for lis in test_list]
	
# printing result
print ("List with only nth tuple element (i.e names) : " + str(res))

##11. Write a python program to modify the tuple. 
test_list1 = [('Geeks', 1), ('for', 2), ('Geeks', 3)]
test_list2 = [4, 5, 6]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# modifying tuple elements
res=[]
for i in range(0,len(test_list1)):
	x=(test_list1[i][0],test_list2[i])
	res.append(x)

# print result
print("The modified resultant list of tuple : " + str(res))

##12. Write a python program to get the minimum and maximum of the values in a tuple. 
test_list = [(2, 3), (4, 7), (8, 11), (3, 6)]

# printing original list
print ("The original list is : " + str(test_list))

# using min() and max()
# to get min and max in list of tuples
res1 = min(test_list)[0], max(test_list)[0]
res2 = min(test_list)[1], max(test_list)[1]

# printing result
print ("The min and max of index 1 : " + str(res1))
print ("The min and max of index 2 : " + str(res2))
