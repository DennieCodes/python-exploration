'''
In this problem, you'll implement a function that takes a list of numbers and returns the sum of all of the even numbers in the list.

Sample input/outputs:

numbers	sum_evens(numbers)
[]	0
[3,7]	0
[4,7]	4
[1,2,3,4,5,6]	12
Implement sum_evens(numbers).
'''

def sum_evens(numbers):
    result = sum([item for item in numbers if item % 2 == 0])

    print(result)

sum_evens([1,2,3,4,5,6])