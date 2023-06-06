# String Challenge 1: Reverse a string.
# name="racecar"
name="hasnat"
reversed_name= name[::-1]

# String Challenge 2: Check if a string is a palindrome.
if (name == reversed_name):
    print('Yes the string is a palindrome!')

# String Challenge 3: Count the occurrences of a character in a string.
char_count = name.count('a')
# print(char_count)

# String Challenge 4: Replace a substring with another string.
string = "Hello world!"
old_substring = "world"
new_substring = "python"
replaced_string = string.replace(old_substring, new_substring)
# print(replaced_string)

# String Challenge 5: Convert a string to uppercase.
uppercase_string = string.upper()

# String Challenge 6: Split a string into a list of words.
splitted_string = string.split()
# print(splitted_string)

# String Challenge 7: Check if a string starts with a specific prefix.
# print(string.startswith('Hell'))

# String Challenge 8: Find the index of the first occurrence of a substring.
# Both find() and index() methods are used to find index of first occurence of a substring
# They differ in the behavior a bit
# print(string.find('ll'))     # Will return -1 on substring not found
# print(string.index('lil')) # Will return exception on substring not found

# String Challenge 9: Remove leading and trailing whitespace from a string.
string.strip()

# Array Challenge 1: Find the maximum element in an array.
array = [5, 8, 2, 10, 3]
# print(max(array))

# Array Challenge 2: Check if all elements in an array are unique.
unique_elements = set(array)
if len(array) == len(unique_elements):
    print('All elements in the array are unique')

# Array Challenge 3: Sort an array in ascending order.
array.sort()

# Array Challenge 4: Reverse the order of elements in an array.
array.reverse()
# print(array)

# List Challenge 1: Append an element to a list.
myList = [1, 2, 3, 4, 5, 2]
myList.append(6)

# List Challenge 2: Remove the last element from a list.
# myList.remove()
# del myList[0]

# List Challenge 3: Find the index of the first occurrence of an element in a list.
list_index = myList.index(2)

# List Challenge 4: Count the number of occurrences of an element in a list.
element_count = myList.count(2)

# Tuple Challenge 1: Access an element at a specific index in a tuple.
my_tuple = (10, 20, 30, 40, 50, 30)
# print(my_tuple[0])

# Tuple Challenge 2: Concatenate two tuples.
tuple1 = (1,2,3)
tuple2 = (4,5,6)
# print(tuple1+tuple2)

# Tuple Challenge 3: Find the index of the first occurrence of an element in a tuple.
# print(my_tuple.index(30))

# Set Challenge 1: Check if two sets have any common elements.
set1 = {1, 2, 3, 4}
set2 = {5, 6}
# set2 = {3, 4, 5, 6}
common_elements = set1&set2
if common_elements:
    print('The sets have common elements.')

# Set Challenge 2: Find the union of two sets.
set_union = set1 | set2
# print(set_union)

# Set Challenge 3: Find the intersection of two sets.
set_intersection = set1 & set2
# print(set_intersection)

# Frozenset Challenge 1: Check if a frozenset is a subset of another set.
set1 = {1, 2, 3, 4, 5}
frozenset1 = frozenset({3, 4, 5})
is_subset = frozenset1.issubset(set1)
# print(is_subset)

# Frozenset Challenge 2: Find the difference between two frozensets.
frozenset1 = frozenset({1, 2, 3, 4, 5})
frozenset2 = frozenset({4, 5, 6, 7})
difference_set = frozenset1.difference(frozenset2)
# print(difference_set)

# Dict Challenge 1: Access the value associated with a specific key in a dictionary.
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
value = my_dict['key2']
# print(value)

# Dict Challenge 2: Check if a key exists in a dictionary.
if 'key2' in my_dict:
    print("Key 'key2' exists in the dictionary.")
else:
    print("Key 'key2' does not exist in the dictionary.")

# Dict Challenge 3: Remove a key-value pair from a dictionary.
# del my_dict['key2']

# Dict Challenge 4: Get a list of all keys in a dictionary.
keys_list = list(my_dict.keys())

# Dict Challenge 5: Get a list of all values in a dictionary.
values_list = list(my_dict.values())

