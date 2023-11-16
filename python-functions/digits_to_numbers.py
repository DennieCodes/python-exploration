'''

You are given a function that has two lists of digits in reversed order. The function should convert each list to an integer in reverse order, add them together, then return a list that contains each digit of the sum in reversed order.

reversed_digits1	reversed_digits2	(Sum)	Output
[3, 2, 1]	[3, 2, 1]	246	[6, 4, 2]
[3]	[3, 2, 1]	126	[6, 2, 1]
[9, 9, 9]	[0, 0, 0]	999	[9, 9, 9]
[7]	[0, 0, 0]	7	[7]
That seems pretty daunting. So, let's break it down piece-by-piece with some smaller functions to solve the larger problems:

Turn a list of digits into a number
Add two lists of digits after converting each into a number
Add two lists of reversed digits after converting each into a number
Turn a number into a an array of digits
Reverse an array of digits
Of course, this is only one way to break down the problem into smaller pieces. But, that's the way the problems are ordered in this exercise. 😉

1
A list of digits
1 PT

Complete the function that is given a list of single digits by combining the entries into a single number and returning that number.

digits	Output
[1, 2, 3]	123
[3]	3
[9, 9, 0]	990
[0, 0, 0]	0
The input will never be an empty list.

input: a list of numbers
'''


def digits_to_number(digits):
    joined = ""
    for digit in digits:
        joined = joined + str(digit)

    return int(joined)


def add_digits(digits1, digits2):
    return digits_to_number(digits1) + digits_to_number(digits2)


def add_reversed_digits(reversed_digits1, reversed_digits2):
    digit1 = reversed(reversed_digits1)
    digit2 = reversed(reversed_digits2)

    return add_digits(digit1, digit2)


def sum_reversed_digits_as_list(reversed_digits1, reversed_digits2):
    result = str(add_reversed_digits(reversed_digits1, reversed_digits2))
    return [int(item) for item in result]


def sum_reversed_digits_as_reversed_list(reversed_digits1, reversed_digits2):
    result = sum_reversed_digits_as_list(reversed_digits1, reversed_digits2)

    return list(reversed(result))


data = [
  [0, 0, 0, 0],
  [1, 2, 3, 4, 5, 6, 9, 8],
  [2],
  [3, 9]
]

result = digits_to_number(data[0])

print(result)