'''

mplement the function shorter_than_5(strings), which returns a list that contains all of the strings from the strings input that have a length less than 5.

'''

def shorter_than_5(strings):
    results = []

    results = list(filter(lambda item: len(item), strings))

    return results

our_list = [ 1,2,3,4,5,6 ]

result = list(filter(lambda x: x % 2 == 0, our_list))

# print(result)

new_dict = dict.fromkeys(our_list, "")

new_dict.update({"a": 10})

# print(new_dict)

print(new_dict.popitem())