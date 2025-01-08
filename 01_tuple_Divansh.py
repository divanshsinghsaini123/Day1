#creating touple
fruit_tuple = ("apple", "banana", "cherry")
print(fruit_tuple)

# Tuple with duplicates
duplicate_fruit_tuple = ("apple", "banana", "cherry", "apple")
print(duplicate_fruit_tuple)

# Length of tuple
print(len(duplicate_fruit_tuple))

# Mixed data types tuple
mixed_data_tuple = (1, 'a', "apple", True)
print(mixed_data_tuple)

# Checking data type
print(type(fruit_tuple))

# Accessing elements from num_tuple
num_tuple = (1, 2, 3, 4, 5)
print(num_tuple[2])
print(num_tuple[1:4])

# Count occurrence and index of an element
count_tuple = (1, 2, 3, 4, 4, 2, 4)
print(count_tuple.count(4))
print(count_tuple.index(4))

# Nested tuple
nested_tuple = ((1, 2), 3, 4)
print(nested_tuple)

# Single element tuple
single_element_tuple = (42,)
print(single_element_tuple)
