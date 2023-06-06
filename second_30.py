# String Challenge 10: Count the number of words in a string.
# name="Hello python programmer"
# print(len(name.split()))

# String Challenge 11: Check if a string ends with a specific suffix.
# input_str = input("Enter a string: ")
# suffix = input("Enter a suffix: ")
# ends_with_suffix = input_str.endswith(suffix)
# if ends_with_suffix:
#     print("The string ends with the suffix.")
# else:
#     print("The string does not end with the suffix.")

# String Challenge 12: Convert a string to title case.
# lang="Python"
# print(lang.title())

# String Challenge 13: Remove all occurrences of a substring from a string.
# input_str = input("Enter a string: ")
# substring = input("Enter a substring to remove: ")
# new_str = input_str.replace(substring, '')

# String Challenge 14: Find the index of the last occurrence of a substring.
# input_str = input("Enter a string: ")
# substring = input("Enter a substring: ")
# last_index = input_str.rfind(substring)

# Array Challenge 5: Check if an array is sorted in ascending order.
# arr=[1,2,3]
# sorted_arr=sorted(arr)
# if(arr==sorted_arr):
#     print('Array is sorted')

# Array Challenge 6: Find the minimum element in an array.
# arr=[1,2,3]
# print(min(arr))

# Array Challenge 7: Remove all occurrences of an element from an array.
# arr=[1,2,3,4]
# element=2
# new_array = [x for x in arr if x != element]
# print(new_array)

# Array Challenge 8: Count the number of elements in an array.
# arr=[1,2,3,4,5]
# print(len(arr))

# List Challenge 5: Insert an element at a specific index in a list.
list1=[1,2,3,4,5]
# list1.insert(5,6)

# List Challenge 6: Reverse the order of elements in a list using the reverse() method.
# print(list1.reverse())

# List Challenge 7: Remove the first occurrence of an element from a list.
# el=2
# print(list1.remove(el))

# List Challenge 8: Sort a list in descending order.
# print(list1.sort(reverse=True))

# Tuple Challenge 4: Check if an element exists in a tuple.
my_tuple=(1,2,3,4)
# print(2 in my_tuple)

# Tuple Challenge 5: Find the number of elements in a tuple.
# print(len(my_tuple))

# Tuple Challenge 6: Convert a tuple to a list.
# print(list(my_tuple))

# Set Challenge 4: Check if a set is a subset of another set.
# set1={1,2,3}
# set2={1,2,3,4}
# print(set1.issubset(set2))

# Set Challenge 5: Check if two sets are disjoint (have no common elements).
# print(set1.isdisjoint(set2))

# Set Challenge 6: Find the symmetric difference between two sets.
# print(set1.symmetric_difference(set2))

# Frozenset Challenge 3: Check if a frozenset is a superset of another set.
# frozen_set1=frozenset({1,2,3,4,5})
# print(frozen_set1.issuperset(set1))

# Frozenset Challenge 4: Check if two frozensets are equal.
# frozen_set2=frozenset({1,2,3,4,5})
# print(frozen_set1 == frozen_set2)

# Dict Challenge 6: Get the number of key-value pairs in a dictionary.
dic1= {
    'id':3,
    'name': 'hasnat',
    'gender': 'male'
}
# print(len(dic1))

# Dict Challenge 7: Get a list of all keys in a dictionary using the keys() method.
# print(dic1.keys())

# Dict Challenge 8: Get a list of all values in a dictionary using the values() method.
# print(dic1.values())

# Dict Challenge 9: Check if all keys in a dictionary are unique.
# is_unique= len(dic1.keys()) == len(set(dic1.keys()))
# print(is_unique)

# Dict Challenge 10: Update a dictionary with key-value pairs from another dictionary.
dic2= {
    'id':5,
    'name': 'ahmad',
    'gender': 'male'
}
# print(dic1.update(dic2))

# String Challenge 15: Split a string into a list of characters.
str='hello world'
# print(list(str))

# String Challenge 16: Check if a string contains only numeric characters.
# print(str.isdigit(str))

# Array Challenge 9: Find the sum of all elements in an array.
arr=[1,2,3,4,5]
# print(sum(arr))

# Array Challenge 10: Check if an array contains a specific element.
# el=2
# print(el in arr)