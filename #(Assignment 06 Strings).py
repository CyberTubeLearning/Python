                                                   ##Strings


 ##1.Write a Python program to calculate the length of a string
str = "geeks"
print(len(str))

 ##2 Write a Python program to count the number of characters (character frequency) in a string

test_str = "GeeksforGeeks"

all_freq = {}

for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1

# printing result
print("Count of all characters in GeeksforGeeks is :\n "
	+ str(all_freq))

 ##3.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itsel##4 Write a program to split a given string on hyphens and display each substring
str = "Amdani athani kharcha rupaiya."

# declaring an empty string variable for storing modified string
modified_str = ''

# iterating over the string
for char in range(0, len(str)):
	# checking if the character at char index is equivalent to 'a'
	if(str[char] == 'a' or str[char] == 'a'.upper()):
		# append $ to modified string
		modified_str += '$'
	else:
		# append original string character
		modified_str += str[char]

print("Modified string : ")
print(modified_str)
##4 Write a program to split a given string on hyphens and display each substring
def split_string(string):

	# Split the string based on space delimiter
	list_string = string.split(' ')
	
	return list_string

def join_string(list_string):

	# Join the string based on '-' delimiter
	string = '-'.join(list_string)
	
	return string

# Driver Function
if __name__ == '__main__':
	string = 'Geeks for Geeks'
	
	# Splitting a string
	list_string = split_string(string)
	print(list_string)

	# Join list of strings into one
	new_string = join_string(list_string)
	print(new_string)

 ##5 Write a program to count occurrences of all characters within a string

def count(s, c) :
	
	# Count variable
	res = 0
	
	for i in range(len(s)) :
		
		# Checking character in string
		if (s[i] == c):
			res = res + 1
	return res
	
	
# Driver code
str= "geeksforgeeks"
c = 'e'
print(count(str, c))
	
 ##6 Write a program to remove empty strings from a list of strings.
test_list = ["", "GeeksforGeeks", "", "is", "best", ""]

# Printing original list
print("Original list is : " + str(test_list))

# using remove() to
# perform removal
while("" in test_list):
	test_list.remove("")

# Printing modified list
print("Modified list is : " + str(test_list))

 ##7 Write a program to replace every special character in the string with #.
def manipulateString(str) :

	# looping through each character of string
	for i in range(len(str)) :
		
		# storing integer ASCII value of
		# the character in 'asc'
		asc = ord(str[i])

		# 'rem' contains coded value which
		# needs to be rounded to 26
		rem = asc - (26 - (ord(str[i]) - ord('a')))

		# converting 'rem' character in range
		# 0-25 and storing in 'm'
		m = rem % 26

		#printing character by adding ascii value of 'a'
		# so that it becomes in the desired range i
		str[i] = chr(m + ord('a'))

	# join method join all individual
	# characters to form a string
	print(''.join(str))

# Driver code	
if __name__ == "__main__" :

	str = "geeksforgeeks"

	# convert string into list of characters
	str = list(str)

	# Function calling
	manipulateString(str)

 ##8 Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string isless than 3, leave it unchanged
def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))

 ##9 Write a Python program to remove the characters which have odd index values of a given string.
def removeOddIndexCharacters(s):
	
	
	
	# Stores the resultant string
	new_s = ""

	i = 0
	while i < len(s):

		# If the current index is odd
		if (i % 2 == 1):
		
			# Skip the character
			i+= 1
			continue

		# Otherwise, append the
		# character
		new_s += s[i]
		i+= 1
		

	# Return the modified string
	return new_s

# Driver Code
if __name__ == '__main__':
	str = "abcdef"

	# Remove the characters which
	# have odd index
	str = removeOddIndexCharacters(str)
	print(str)

 ##10.Write a Python program to count the occurrences of each word in a given
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))




