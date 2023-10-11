'''
Create a function named third_largest_value that accepts a single parameter, values.

The values parameter will be a list
Find the third largest value in the list
If the length of the list is less than 3, return None
'''

def third_largest_value(values):
    if len(values) < 3:
        return None

    val_sorted = sorted(values)

    return val_sorted[len(values)-3]

result = third_largest_value([1,9, 3,5,6])
print(result)
