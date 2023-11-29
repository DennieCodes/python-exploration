'''
We don't know where Caris is grazing, but they have found another list of single-digit numbers. They'd like you to take those numbers, and using them in any order, create the smallest integer possible from those numbers of a certain length of digits.

For example, if Caris gives you the list [3, 1, 2, 6, 5, 9] and says the length of the number must be three digits, then the result you should give is 123, because that's the smallest three-digit integer you can make from the numbers in the list.

nums	length	Output
[3, 1, 2, 6, 5, 9]	3	123
[3, 1, 2, 6, 5, 9]	5	12356
[1]	1	1
[5, 9, 8, 3]	1	3
[5, 9, 8, 3]	2	35
[5, 9, 8, 3]	4	3589
'''

nums = [3, 1, 2, 6, 5, 9]
length = 3


def make_integer(nums, length):
    sort_nums = sorted(nums)
    sort_nums = sort_nums[0: length]
    result = ''
    for num in sort_nums:
        result += str(num)

    return int(result)


result = make_integer(nums, length)

print(result)
