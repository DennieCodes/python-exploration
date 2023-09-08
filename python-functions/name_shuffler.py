def name_shuffler(str_):
    # input: a string of two words separated by a space
    # output: a string of those two words swapped

    result = str_.split(' ')
    result[0], result[1] = result[1], result[0]
    return ' '.join(result)

result = name_shuffler("John McClane")

# Submitted on Codewars
# def name_shuffler(str_):
#     return ' '.join(str_.split(' ')[::-1])


print(result)