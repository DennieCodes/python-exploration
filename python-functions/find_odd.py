'''
Complete the function find_odd to find the single number in a list that occurs an odd number of times.

For example, assume you are given the following list:

[3, 3, 18, 4, 4, 4, 4]
The single number in the list that occurs an odd number of times is the number 18.

You are not guaranteed to have them grouped like that. Here's that list, again, in a "messed up" order:

[3, 4, 4, 3, 4, 18, 4]
The answer would still be 18.

input: a list of numbers
output: the one number in the group that occurs an odd # of times

'''

def find_odd(nums):
  dict = {}
  result = 0

  for num in nums:
    dict[num] = dict.get(num, 0) + 1

  result = list(filter(lambda num: dict[num] % 2 != 0, dict))
  return result[0]


data = [3, 3, 18, 4, 4, 4, 4]

result = find_odd(data)
print(result)
