'''
Given two strings of up to 100 characters each, yesterday and today, complete the function num_same_spaces to return the number of parking spaces that were occupied both yesterday and today.

Constraints:

1 <= len(yesterday) <= 100
len(yesterday) == len(today)
Example:

Here are two strings that you need to compare. Underneath the two strings are stars that show where the same parking space was filled on both mornings.

yesterday: CCEEECCECECECCCCECECCCE
today:     CECECECECCEEECCCECECEEC
matches:   ★     ★ ★    ★★★ ★ ★
Because there are eight matches, the function num_same_spaces will return 8.

'''

def num_same_spaces(yesterday, today):
    return len(list(filter(lambda set: set[0] == set[1] and set[0] =="C" , zip(yesterday, today))))

yesterday = "CECECECECECEECEECECCECECCECE"
today =     "ECEECCECECECECECCECECECCECEC"
            # "   **       *** ***    *    "
result = num_same_spaces(yesterday, today)
print(result)

print(len("CECECECECECEECEECECCECECCECE"))