# list creation 
fruits = ["apple", "banana", "cherry"]
print("Displaying fruit list:", fruits)

# to find duplicate elements
fruits_with_duplicates = ["apple", "banana", "cherry", "apple"]
print("List with duplicate items:", fruits_with_duplicates)

# To find Length of the list
print("Length of the list:", len(fruits_with_duplicates))

# List with mixed data types (integer, character, string, boolean)
# All data types are allowed in the list 
mixed_list = [1, 'a', "apple", True]
print("List with mixed data types:", mixed_list)

# Checking data type of the list
print("Data type of the list:", type(fruits))

# some another example of list ( all are interger data types are their )
numbers = [1, 2, 3, 4, 5]

# Appending elements into the list
numbers.append(6)
numbers.insert(4, 7)  # Insert at a specific position
print("After appending and inserting:", numbers)

# Extending list with multiple elements
numbers.extend([9, 10])
print("List after extension:", numbers)

# Removing elements
numbers.remove(6)  # Remove specific element ( you have to give the value of that element)
print("After removing an element:", numbers)

# Popping the last element from thelist 
numbers.pop()
print("After popping the last element:", numbers)

# Accessing elements 
# 1. form a perticular index
# 2. from a perticular range 
print("Element at index 4:", numbers[4])  # Access by index
print("Range of elements [0:2]:", numbers[0:2])  # Access by range

# Counting the occurrence of a specific element 
number_list = [1, 2, 3, 4, 4, 2, 4]
print("Count of element 4:", number_list.count(4))

# Finding the index of an element
print("First occurrence of element 4 is at index:", number_list.index(4))

# Nested list
nested_example = [[1, 2], 3, 4]
print("Nested list structure:", nested_example)
