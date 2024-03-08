##1. Write a python program to traverse all the elements of a list using loop.
list = [2, 4, 6, 8, 10]
length = len(list)
for i in range(length):
 print(list[i])
##2. Write a python program to get the elements of a list from the user. 



##3. Write a python program to sum all the elements of a list. 
list1 = [11, 5, 17, 18, 23]
total = sum(list1)
print("Sum of all elements in given list: ", total)

##4. Write a python program to find out the greatest of all the elements of a list. 
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Largest element is:", list1[-1])

##5. Write a python program to find out the smallest of all the elements of a list. 
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort(reverse=True)
print("Smallest element is:", list1[-1])

##6. Write a python program to sort the elements of a list in ascending order. 
numbers = [1, 3, 4, 2]
# Sorting list of Integers in ascending
print(numbers.sort()) # None
print(numbers)		 # [1, 2, 3, 4]

print(sorted(numbers)) # [1, 2, 3, 4]
print(numbers)		 # [1, 3, 4, 2]
##7. Write a python program to sort the elements of a list in descending order. 
numbers = [1, 3, 4, 2]

# Sorting list of Integers in descending
numbers.sort(reverse=True)

print(numbers)

##8. Write a python program to get the square of every of element of a list. 
data=[1,2,3,4,5,6,7]
result = [i*i for i in data if i%2!=0]
print(result)

##9. Write a python program to reverse the elements of a list. 
def Reverse(lst):
 new_lst = lst[::-1]
 return new_lst
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

##10. Write a python program to print the frequency of elements of a list. 
d = {}

test_list = [[3, 5, 4],
			[6, 2, 4],
			[1, 3, 6]]

for x in test_list:
 for i in x:
  	d[i] = d.get(i,0) + 1

# Original list
print(f"The original list : {test_list}" )

# printing result
print(f"The list frequency of elements is : {d}" )

##11. Write a python program to add the elements of a list index wise. 
# initializing lists
test_list1 = [1, 3, 4, 6, 8]
test_list2 = [4, 5, 6, 2, 10]

# printing original lists
print ("Original list 1 : " + str(test_list1))
print ("Original list 2 : " + str(test_list2))

# using naive method to
# add two list
res_list = []
for i in range(0, len(test_list1)):
	res_list.append(test_list1[i] + test_list2[i])

# printing resultant list
print ("Resultant list is : " + str(res_list))

##12. Write a python program to find the average of elements of a list. 
# Python program to get average of a list
def Average(lst):
	return sum(lst) / len(lst)

# Driver Code
lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(lst)

# Printing average of the list
print("Average of the list =", round(average, 2))

##13. Write a python program to find the second largest number of all the elements of a list.
# List of numbers
list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]

# Removing duplicates from the list
list2 = list(set(list1))

# Sorting the list
list2.sort()

# Printing the second last element
print("Second largest element is:", list2[-2])

##14. Write a python program to find the even numbers from a list. 
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

	# checking condition
	if num % 2 == 0:
		print(num, end=" ")

##15. Write a python program to find the odd numbers from a list. 
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

	# checking condition
	if num % 2 != 0:
	 print(num, end=" ")

##16. Write a python program to count even and odd numbers from the elements of a list.
list1 = [10, 21, 4, 45, 66, 93, 1]
even_count, odd_count = 0, 0
# iterating each number in list
for num in list1:
	# checking condition
	if num % 2 == 0:
		even_count += 1

	else:
		odd_count += 1
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)

##17. Write a python program to create a nested list. 
matrix = []

for i in range(5):
	
	# Append an empty sublist inside the list
	matrix.append([])
	
	for j in range(5):
		matrix[i].append(j)
		
print(matrix)

##18. Write a python program to count unique values inside a list. 
from collections import Counter
input_list = [1, 2, 2, 5, 8, 4, 4, 8]

# creating a list with the keys
items = Counter(input_list).keys()
print("No of unique items in the list are:", len(items))

##19. Write a Python program to append a list to the second list. 
Number = [10, 20, 30, 40]
animal = ["Cat", "Dog", "Lion", "Panda"]
final_list = Number + animal
print(final_list)
##20. # Python program to iterate
import itertools
num = [1, 2, 3]
color = ['red', 'while', 'black']
value = [255, 256]
for (a, b, c) in zip(num, color, value):
	print (a, b, c)
