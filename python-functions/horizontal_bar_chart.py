'''
input: sentence
output: a list made up of the letter groups from the sentence, organized by
         most frequent to least.
pseudocode
1.  iterate over the sentence and place letters into a dictionary with the
    letters being the key and the value being the occurence
2.  create a list and fill with the letters from the dictionary times the
    value
3.  sort the list, return
'''

def bylength(word1,word2):
    return len(word2)-len(word1)

def horizontal_bar_chart(sentence):
    result = []
    parse = {}

    for letter in sentence:
        parse[letter] = parse.get(letter, 0) + 1

    for key, value in parse.items():
        if not key == ' ':
          result.append(key * value)

    return list(sorted(result))

# Shahzad's solution
# def horizontal_bar_chart(sentence):
#     d = {}
#     for c in sentence:
#         if c >= "a" and c <= "z":
#             if c not in d:
#                 d[c] = ""
#             d[c] += c
#     result = []
#     for s in d.values():
#         result.append(s)
#     return list(sorted(result))

# Jessica's solution
# def horizontal_bar_chart(sentence):
#     final = {}

#     for char in sentence:
#         if char == ' ':
#             pass
#         elif char in final:
#             final[char] += f'{char}'
#         else:
#             final[char] = char

#     return sorted(final.values())

# Marcio's solution
# def horizontal_bar_chart(sentence):
#     byletter = {ii for ii in sentence}
#     out = []
#     for letter in byletter:
#         if letter == " ": continue
#         ii = letter * sentence.count(letter)
#         out.append(ii)
#     out.sort()
#     return out

print(horizontal_bar_chart("abba has a banana"))