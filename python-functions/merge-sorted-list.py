'''

You're given two sorted lists. Your job is to write a function that merges those two sorted lists into one big sorted list.

List 1	List 2	Output
[1, 3, 5]	[2, 100]	[1, 2, 3, 5, 100]
[]	[2, 4, 5]	[2, 4, 5]
[1, 2, 3]	[1, 2, 4]	[1, 1, 2, 2, 3, 4]
To figure out how to solve this problem, think about how you would do this given two lists on a piece of paper. Try to come up with a step-by-step way that you would do it. Then, try to write that as code.

'''

def merge_sorted_lists(list1, list2):
    newList = list1 + list2
    newList.sort()
    return newList

data1 = [1, 3, 5]
data2 = [2, 100]

result = merge_sorted_lists(data1, data2)
print(result)
