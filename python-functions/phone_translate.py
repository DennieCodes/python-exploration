'''
Before smart phones, when you wanted to text someone, you had to press the same number over and over again to get a letter from the keypad.

letter dialing

You can see the number 2 has three letters associated with it: A, B, and C. Originally, you would press the 2 button once to get the letter A, push the 2 button twice to get the letter B, and push the 2 button three times to get the letter C.

At some point, someone tried to make it easier by including a dictionary in the phone. You could just type the numbers once, and the phone would try to guess the word for you.

For example, let's say the phone's dictionary contained the words "ARROW", "BOTOX", "DOMES", and "FOODS". If you typed the numbers 26869, then the phone would come up with the word BOTOX for you. If you typed the numbers 27769, then the phone would come up with the word ARROW for you. If you typed the numbers 36637, it would come up with both the words "DOMES" and "FOODS".

Given that mapping of numbers to letters and a list of valid words, it's up to you to figure out which of those words could be created from the digits someone types into the phone.

2
OG texting
Given list of valid words and a number digits, complete the function translate to return the total number of the words in words that can be created using the digits from digits.

input: a list of words, an integer
output: total number of words that can be created from the list based on the numbers provided

each number on the phone besides 0 and 1, can be used to produce 3 letters from the alphabet

1. create a dictionary of numbers with their corresponding letters
2. create a list of possible character combinations of the provided numbers
2a. create a counter integer
3. iterate over each word in the list
3a. make a local copy of possible char combinations
4. iterate over each letter in the word
5. check if the letter is in the list of possible character combinations
6. if so then remove it from the list of combinations and continue onto next letter until end.
   if it reaches the end then this word can be made from the numbers provided, increment counter
7. if not then continue onto next word
8. return counter

'''

def get_num(letter):
    if letter in "ABC":
        return 2
    elif letter in "DEF":
        return 3
    elif letter in "GHI":
        return 4
    elif letter in "JKL":
        return 5
    elif letter in "MNO":
        return 6
    elif letter in "PQRS":
        return 7
    elif letter in "TUV":
        return 8
    elif letter in "WXYZ":
        return 9

def translate(words, digits):
    counter = 0
    for word in words:
        compare = ""
        for letter in word:
            compare += str(get_num(letter))
        if int(compare) == digits:
            counter += 1
    return counter

words1 = ['TOMO', 'MONO', 'DAK']
digits1 = 6666
possible = [ "MNO", "MNO", "MNO", "MNO" ]

words2 = ['DOM', 'FON', 'TOM']
digits2 = 366

words3 = ['JA', 'LA']
digits3 = 52

result = translate(words1, digits1)
print(result)