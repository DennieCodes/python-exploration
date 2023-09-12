'''
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

input: some string or no string
output: a dictionary of all characters as keys and the number of their occurence as values
'''

def count(s):
    return { key:s.count(key) for key in s[:]}

result = count("aba")
print(result)