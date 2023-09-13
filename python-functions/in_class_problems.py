# 1. Find the intersection of two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

output: [3, 4, 5]

def intersection(list1, list2):
    intersect = []

    for item in list1:
        if item in list2:
            intersect.append(item)
    print(intersect)

# 2. Find the longest sublist with consecutive elements
num_list = [1, 9, 3, 10, 4, 20, 2]

output [1, 2, 3, 4]

# 3. Rotate list by k steps

numbers = [1, 2, 3, 4, 5]
k= 2

output: [4, 5, 1, 2, 3]

def rotate_by_k():
    rotated = [0] * len(numbers)

    for num in range(len(numbers)):
        if num + 2 <= len(numbers) -1:
            rotated[num+2] = numbers[num]
        else:
            rotated[num+2 - len(numbers)] = numbers[num]

    print(rotated)

# 4. Remove duplicates from a sorted list
# Given a sorted list, remove the duplicates in-place such that each element appears only once and return the new length
sorted_list = [1, 1, 2, 3, 3, 3, 4, 5, 5]

output: [1, 2, 3, 4, 5]

def remove_duplicates():
    no_duplicates = {}

    for item in sorted_list:
        no_duplicates[item] = item

    sorted_list = list(no_duplicates)
    print(sorted_list)

# 5. Find missing numbers in a range
# Given a list of numbers in a specific range, find the missing numbers within that range
output =  [4, 6, 7]
input = [3, 5, 8, 9, 10]

def missing_numbers(input):
    missing = []
    for value in range(num_list[0], num_list[len(num_list)-1]):
        if not value in num_list:
            missing.append(value)

    print(missing)

# 6. Counting word Frequencies in a text
# Given a text, count the frequency of each word and store the results in a dictionary

text = "this is a simple text text example"

def word_frequencies():
    results = {}
    text_list = text.split()

    for item in text_list:
        if results.get(item) == None:
            results[item] = 1
        else:
            results[item] += 1

    print(results)

# 7. Find common keys and values
dict1 = {'a': 1, 'b':2, 'c':3}
dict2 = {'b': 2, 'c':4, 'd': 5}

output: {'b': 2}

def common_keys_and_values():
    common = {}

    for key in dict1:
        if key in dict2 and dict1[key] == dict2[key]:
            common[key] = dict1[key]

    print(common)

# 8. Invert a dictionary
# given a dictionary, create a new dictionary where the keys are the values from the original dictionary, and the values are lists of keys from the original dictionary that had the corresponding value

original_dict = {'a':1, 'b':2, 'c':1, 'd':3}

output: {1: ['a', 'c'], 2: ['b'], 3: ['d']}

def inverted():
    inverted = {}

for key, value in original_dict.items():
    if value in inverted:
        inverted[value].append(key)
    else:
        inverted[value] = list(key)

    print(inverted)

# 9. Count character frequencies
text = 'hello party'

# given the string, count the frequency of each character and store the results in a dictionary where the key is the character and the value is its frequency.
def count_frequencies():
    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    print(frequency)

# 10. Group by category
items = [ {'name': 'apple', 'category': 'fruit'}, {'name': 'banana', 'category': 'fruit'}, {'name': 'carrot', 'category': 'vegetable'}, {'name': 'grape', 'category': 'fruit'}, {'name': 'broccoli', 'category': 'vegetable'},]

# output has the key as the category and the names in a list as values
# 'fruit': ['apple' etc...]

def categorize():
    categorized = {}

    for item in items:
        category = item["category"]
        name = item["name"]
        if category in categorized:
            categorized[category].append(name)
        else:
            categorized[category] = [name]

    print(categorized)

# 11. Dictionary key sorting
# sort the keys of a dictionary based on their values in descending order

grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David':95}

# output sorted keys ['David', 'Bob', 'Alice', 'Charlie']

def key_sorting():
    index = []
    return_list = []
    for key, value in grades.items():
        index.append([key, value])

    def sortFunc(sub_arr):
        return sub_arr[1]

    index.sort(key = sortFunc)
    index.reverse()

    for name in index:
        return_list.append(name[0])

    print(return_list)

# 12. Anagram grouping
# given a list of words, group the anagrams together in a dictionary
words = ['listen', 'silent', 'earth', 'heart', 'python', 'typhon']

output: {'eilnst': ['listen', 'silent'], 'aehrt': ['earth', 'heart'], 'hnopty': ['python', 'typhon']}

def anagrammer(word):
    split = list(word)
    split.sort()
    return ''.join(split)

def anagram_grouping(word):
    anagram = {}
    for word in words:
        key_word = anagrammer(word)

        if key_word in anagram:
            anagram[key_word].append(word)
        else:
            anagram[key_word] = [word]

    print(anagram)