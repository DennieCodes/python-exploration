# 1. Reverse a list

list1 = [100, 200, 300, 400, 500]

list1.reverse()
# print(list1)

# 2. Turn every item of a list into its square

numbers = [1, 2, 3, 4, 5, 6, 7]

for idx in range(len(numbers)):
    numbers[idx] *= numbers[idx]

# print(numbers)

# 3. Add new item to a list after a specified item
# Task: Add item 7000 after 6000 in the following list

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# list1[2][2].append(7000)
# another version
list1[2][2].insert(2, 7000)

# print(list1)
