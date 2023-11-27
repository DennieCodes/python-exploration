'''
Given a 2D integer list nums (a list of lists) where each list in nums is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.

Here are some examples:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].

Input: nums = [[1,2,3],[4,5,6]]
Output: []
Explanation: There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].

Look at the built-in data type set and its methods to see if something can help you there.

input: 2d list of nums
  - each list is a non-empty array of distinct positive integers
output: a list of integers that are present in each array of nums sorted in ascending order


'''


def intersection(nums):
    result = []

    nums.sort(key=lambda x: len(x), reverse=True)

    for num in nums[0]:
        flag = True

        for lis in range(1, len(nums)):
            if num not in nums[lis]:
                flag = False

        if flag == True:
            result.append(num)

    return sorted(result)


result = intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]])

print(result)