'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

input: string with dash/underscore delimited words
output: convert to camel case string
note: if the first letter of input is capitalized then make sure result is capitalized
      the input can have both underscore and dashes

1. take the string and parse into list
2. Check first letter capitalized
3. Turn back into string
'''

def to_camel_case(text):
    # replace dash and underscore with space
    replace = text.replace('-', ' ')
    replace = replace.replace('_', ' ')
    # convert to list and capitalize
    result = [item.capitalize() for item in replace.split()]

    # Check for capitalization of first letter
    if not text[0] == text[0].upper():
        result[0] = result[0].lower()

    return ''.join(result)

dataset = [
    "the-stealth-warrior",
    "The_Stealth_Warrior",
    "The_Stealth-Warrior"
]

for test in dataset:
    print(to_camel_case(test))

'''
Great Codewars solution

def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

'''