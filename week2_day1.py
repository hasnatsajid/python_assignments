# 1. Challenge: String Reversal
# Description: Write code that takes a string as input and prints the reverse of that string. (using while loop)
# Example: Input: "Python", Output: "nohtyP"
# inputStr = input('Enter input string : ')
# str_letters = []
# i=len(inputStr)-1
# while i >= 0:
#     str_letters.append(inputStr[i])
#     i -= 1
# else:
#     print('Reversed String : ', "".join(str_letters))

# 2. Challenge 3: List Concatenation
# Write a program that takes two lists as input from the user and uses a while loop to concatenate them into a single list. Display the concatenated list as the output.
# Example: Input: [1, 2] and [3, 4], Output: [1, 2, 3, 4]
# list1_str = input('Enter first list (space-separated) : ')
# list1 = list1_str.split()
# list2_str = input('Enter second list (space-separated) : ')
# list2 = list2_str.split()
# concatenated_list = list1
# i = 0
# while i<len(list2):
#     concatenated_list.append(list2[i])
#     i += 1
# else:
#     print(concatenated_list)


# 3. Challenge: Tuple Unpacking
# Description: Write code that takes a tuple of two elements as input and prints each element separately.
# Example: Input: (3, 7), Output: 3, 7
# input_tuple  = eval(input("Enter the elements of the tuple (comma-separated): "))
# print(input_tuple)
# element1, element2 = input_tuple
# print(element1)
# print(element2)

# Challenge: Set Intersection
# Description: Write code that takes two sets as input and prints a new set containing the common elements.
# Example: Input: {1, 2, 3}, {2, 3, 4}, Output: {2, 3}
# set1={1, 2, 3}
# set2={2, 3, 4}
# intersection_set = set1.intersection(set2)
# print(intersection_set)

# Challenge: Dictionary Lookup
# Description: Write code that takes a dictionary and a key as input and prints the corresponding value if the key exists in the dictionary, or "Key not found" otherwise. (using while loop)
# Example: Input: {'a': 1, 'b': 2}, 'b', Output: 2
# input_str=input("Enter dictionary in format (key1: value1, key2: value2): ")
# input_dic=eval(input_str)
# input_key=input("Enter key to search in dictionary : ")
# if input_key in input_dic:
#     print(f"key {input_key} exists in the dictionary :)")
# else:
#     print(f"key {input_key} does not exists in the dictionary :(")

# Challenge: Ternary Maximum
# Description: Write code that takes three numbers as input and uses a ternary expression to print the maximum value among them.
# Example: Input: 5, 9, 3, Output: 9
# num1=int(input("Enter the first number : "))
# num2=int(input("Enter the second number : "))
# num3=int(input("Enter the third number : "))
# print( num1 if num1>num2 and num1>num3 else num3 if num2 < num3 else num2)

# Challenge: Nested Ternary
# Description: Write code that takes a number as input and uses a nested ternary expression to print "Positive" if the number is greater than 0, "Negative" if it's less than 0, or "Zero" if it's equal to 0.
# Example: Input: -7, Output: "Negative"
# num=int(input("Enter the number : "))
# print('Positive' if num>0 else "Negative" if num<0 else "Zero")

# Challenge: Compound If-Else
# Description: Write code that takes an integer as input and checks if it's divisible by both 2 and 3, divisible by only 2, divisible by only 3, or not divisible by either, and prints the result.
# Example: Input: 9, Output: "Divisible by 3"
# num=int(input("Enter the integer : "))
# if (num%2==0 and num%3==0):
#     print("Integer is divisible by both 2 and 3")
# elif num%2 == 0:
#     print("Integer is divisible by only 2")
# elif num%3 == 0:
#     print("Integer is divisible by only 3")
# else:
#     print("Integer is not divisible by either")

# Challenge 1: Reversing a List
# Write a program that takes a list of numbers as input and uses a while loop to reverse the elements in the list. The reversed list should be stored in a new list and displayed as output.
input_str=input("Enter the list of numbers seperated by spaces : ")
input_list=input_str.split()
input_list=[int(num) for num in input_list]
new_list=[]
i=len(input_list)-1
while i>=0:
    new_list.append(input_list[i])
    i-=1
print(new_list)

# Challenge 2: Removing Duplicates
# Create a program that prompts the user to enter a list of integers and uses a while loop to remove any duplicate values from the list. Display the modified list without duplicates as the output.
input_str=input("Enter the list of numbers seperated by spaces : ")
input_list=input_str.split()
input_list=[int(num) for num in input_list]
i=0
while i<len(input_list):
    if input_list.count(input_list[i]) > 1:
        input_list.remove(input_list[i])
    else:
        i+=1
print(input_list)

# Challenge 3: List Sum
# Write a program that calculates the sum of all the numbers in a given list using a while loop. Display the sum as the output.
nums=[1,2,3,4]
sum=0
i=0
while i<len(nums):
    sum+=nums[i]
    i+=1
print(sum)

# Challenge 4: List Search
# Create a program that asks the user to enter a list of strings. Then, prompt the user to enter a string to search for within the list. Use a while loop to search for the given string in the list and display whether it is found or not.
num_strings=int(input("Enter the number of strings you want to add : "))
strings=[]
for i in range(0,num_strings):
    str = input("Enter the string : ")
    strings.append(str)
target=input("Enter the string to find in the list : ")
i=0
while i<len(strings):
    if strings[i] == target:
        print("String found :)")
        break
    i+=1
else:
    print("String not found")

# Challenge 5: List Sorting
# Write a program that sorts a given list of numbers in ascending order using a while loop and the bubble sort algorithm. Display the sorted list as the output.
nums=[6, 7, 3, 1, 0, 2]
n = len(nums)
sorted = False

while not sorted:
    sorted = True
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            sorted = False

    n -= 1
print(nums)

# Challenge 5: List Rotation
# Write a program that takes a list of numbers as input and uses a while loop to rotate the elements in the list to the right by a given number of positions. Display the rotated list as the output.
nums=[6, 7, 3, 1, 0, 2]
n = len(nums)
rotation_positions = 2
positions = rotation_positions % n  # To handle positions larger than the list size

while positions > 0:
    last_element = nums[-1]
    for i in range(n-1, 0, -1):
        nums[i] = nums[i-1]
    nums[0] = last_element
    positions -= 1

print(nums)