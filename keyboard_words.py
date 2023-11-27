'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
words	Output
["Hello","Alaska","Dad","Peace"]	["Alaska","Dad"]
["omk"]	[]
["adsdf","sfd"]	["adsdf","sfd"]

input: array of strings (words)
output: array of words that can be typed on only one row of keyboard letters

you get an array of letters
you want to see for each word if every letter in it is in the same keyboard row
if so then add it to the return list
if not then continue

'''

keyboard_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

def keyboard_words(words):
    result = []
    flag = True

    for row in keyboard_rows:
      for word in words:
          for letter in word:
              if str.lower(letter) not in row:
                  flag = False

          if flag == True:
              result.append(word)
          flag = True
      flag = True

    return result


data = ["Hello", "Alaska", "Dad", "Peace"]

result = keyboard_words(data)

print(result)