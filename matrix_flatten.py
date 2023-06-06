matrix= [[1,2,3],[4,5,6],[7,8,9]]
flattened_list = []

# Using python for loop
for list in matrix:
    for j in list:
        flattened_list.append(j)
print(flattened_list)

# Using python list comprehension
flattened_list2 = [j for list in matrix for j in list]
print(flattened_list2)
