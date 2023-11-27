'''
Given two lists, nums1 and nums2, return a list that contains all of the numbers that are in nums1 that are not in nums2. The output should be sorted from smallest to largest.

nums1	nums2	Output
[5, 2, 4, 3, 1]	[4, 2]	[1, 3, 5]
[1, 5, 4, 2, 3]	[6]	[1, 2, 3, 4, 5]
[4, 2, 5, 3, 1]	[2, 1, 3, 4, 5]	[]
[1, 4, 2, 5, 3]	[]	[1, 2, 3, 4, 5]
[]	anything	[]
'''

nums1 = [5, 2, 4, 3, 1]

nums2 = [4, 2]


def find_list_difference(nums1, nums2):
    result = []

    for num in nums1:
        if num not in nums2:
            result.append(num)

    return sorted(result)


result = find_list_difference(nums1, nums2)

print(result)