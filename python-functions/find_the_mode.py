'''
You're given a list of numbers. The mode of the numbers is the number (or numbers) that appear most often in the list.

For example, consider the following list:

9, 2, 9, 6, 8, 7, 1, 3, 9, 6
The number 9 appears most often (3 times) in the list, so the mode of the list is 9.

Consider this list:

9, 2, 9, 6, 8, 2, 1, 2, 9, 6
The number 9 and the number 2 both appear 3 times in the list, more than any other number. The modes of the list are 2 and 9.

1
Find the modes
Submitted on Today at 5:00 PM
Given a list of numbers numbers, complete the function mode that returns a list of all of the modes of the list of numbers.

The list of numbers will always have at least one number in it.
'''

def mode(numbers):
    nums = {}
    modes = []
    sublist = []

    for number in numbers:
        nums.setdefault(number, 0)
        nums[number] += 1

    highest = max(nums.values())

    subset = list(filter(lambda item: item[1] == highest, nums.items()))

    for set in subset:
        sublist.append(set[0])

    return sublist