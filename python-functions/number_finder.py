nums = [4, 5, 3, 2, 8, 1, 6]

def find_missing(nums):
  comp_sum = sum(list(range(min(nums), max(nums)+1)))
  actual_sum = sum(nums)

  return comp_sum - actual_sum


print(find_missing(nums))