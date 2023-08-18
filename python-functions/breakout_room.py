'''
You and your friend decide to meet up in a breakout room, but you don't want other people to know which breakout room you're going to until after you've chosen it.

To do this, you devise a way to send a secret message. You choose four unique letters, like "PLOD". Then, you construct a string that has those letters in it, in order, with other letters possible between the letters that you chose. You send the four unique letters and the secret message to your friend.

When your friend gets the four letters and the string, they throw out as many letters as they can to leave only all of the "PLOD" values that they can. Then, they count how many "PLOD" occurrences there are in the secret message. That's the number of the breakout room that the two of you should meet in.

7
Secret message
Given two strings, code and message, complete the function breakout_room that returns the count of the number of times that code occurs in message.

Constraints:

code has four unique uppercase letters
1 <= len(message) <= 100000
message has only uppercase letters
Example:

Let's say that you receive these values from your friend. You scan the string and find all of the ASDF values in it in that order.

code:    ASDF
message: SODIFJOSDIFJASOIDFASLWEARWOERIMSOEIDENRMFASD
                     AS  DFAS               D    F
Your code would return 2.

input: code (string), message (string)
output: the number of times the code is present in the message

1. iterate until the end of the message
2. going letter by letter search along the message for the code
3. when you find a letter, search the remaining string for the next letter, etc...
4. count everytime you complete the code set
5. continue to search the message
6. return the number of times code is present
'''

# def breakout_room(code, message):
#     count = 0
#     pos = 0
#     cont = True
#     last = code[len(code) - 1]
#     substring = message

#     while pos < 10 and cont == True:

#         for letter in code:
#             found = substring.find(letter)
#             print(f"substring: {substring}, l: {letter} at pos: {found}")

#             if found == -1:
#                 cont = False
#                 break

#             substring = message[found+1:]
#             print("new substring: ", substring)
#             if letter == last:
#                 count += 1

#         # stop infinite loop
#         pos += 1

#     return count


def breakout_room(code, message):
    count = 0
    flag = True
    inf_check = 0
    substring = message
    last_letter = code[len(code)-1]

    while flag == True and inf_check < 100:
        for letter in code:
            if not letter in substring: # When we no longer find code in the substring then end loop
                flag = False
                break

            new_substring_position = substring.find(letter) # Find next letter from code in substring
            substring = substring[new_substring_position+1:]

            if letter == last_letter: # When we have found the last letter then entire code has been found so add count
                count += 1

        inf_check += 1 # Infinite loop stop

    return count

code1 = "ASDF"
message1 = "SODIFJOSDIFJASOIDFASLWEARWOERIMSOEIDENRMFASD"

result = breakout_room(code1, message1)
print(result)


# code1 = "ASDF"
# # message1 = "SODIFJOSDIFJASOIDF ASLWEARWOERIMSOEID ENRMFASD"
# #                              1
# message1 = "SODIFJOSDIFJASOIDFASLWEARWOERIMSOEIDENRMFASD"


# result = breakout_room(code1, message1)
# print(result)