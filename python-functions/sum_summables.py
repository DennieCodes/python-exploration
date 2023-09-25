'''
This function takes a dictionary and returns the sum of all of the summable values in it. Here "summable" means any value that is:

an int or a float
is a string and isnumeric(). These should be cast to float()
Example:

dictionary = {
    "dog": 1,
    "number": "three",
    "size": "2",
    "heavy": True,
    "weight": 3.4,
}
total = sum_summables(dictionary)
print(total) # --> 7.4
Hint: use isinstance(value, type) like this:

print(isinstance(1, int))       # --> True
print(isinstance("cat", str))   # --> True
print(isinstance(True, int))    # --> True, what?! Did you know this?
print(isinstance("cat", int))   # --> False
print(isinstance(1, str))       # --> False

'''

def sum_summables(dictionary):
    total = 0

    for key, value in dictionary.items():
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str) and value.isnumeric():
            total += float(value)

    return total