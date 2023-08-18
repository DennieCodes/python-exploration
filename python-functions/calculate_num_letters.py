'''
Your auntie gives you a puzzle for your birthday. It's a box with one button and a screen. Intrigued by it, you press the button and see an "X" appear on the screen. You press the button, again, and the "X" is replaced by "O". You press it, again, and the "O" is replaced by "OX". You keep pressing it and get "OXO", "OXOOX".

After playing around with it for a while, you realize that every time you press the button, it changes all of the "X" letters to "O" letters, and changes all of the "O" letters to the letters "OX".

Here's that sequence again:

Start:
Press: X
Press: O      (The X becomes an O)
Press: OX     (The O becomes OX)
Press: OXO    (Of OX, the first O becomes OX and the X
               becomes an O)
Press: OXOOX  (Of OXO,
                the first O becomes OX,
                the X becomes O, and
                the second O becomes OX)
The sequence has you intrigued. You decide to write a program to figure out how many "X" and "O" letters there are on the screen after you push it a certain number of times.

8
Flip-flop
Given the number of times to push the button num_pushes, complete the function calculate_num_letters so that it returns both the number of Xs and Os. The placeholder function shows you how that works.

Constraints: 1 <= num_pushes <= 20

input: num of times to push the box (int <= 20)
output: the number of x's and o'x (tuple)

rules with each push:
1. X's become O's
2. O's become OX

pseudocode:
1. iterate the function according to input value
2. initialize a count of 0
3. initialize a string = "" to track current string
4. iterate over each letter in the string
5. start appending results to a new string
6. when done count the x's and o's and return values in a tuple

'''

def calculate_num_letters(num_pushes):
    display_string = ["X"]

    for num in range(1, num_pushes): # start at one with default X
        working_string = []
        for char in display_string:
            if char == "X":
                working_string.append("O")
            else:
                working_string.append("O")
                working_string.append("X")
            pass
        display_string = working_string

    exes = ''.join(display_string).count("X")
    os = ''.join(display_string).count("O")

    return (exes, os)

result = calculate_num_letters(5)
print(result)

print(['X', 'O'][::])