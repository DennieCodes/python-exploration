from functools import reduce
'''
The function dict_to_list takes a dictionary as its input and transforms the dictionary into a list by adding its keys and values to the list.

Example:

dict_to_list({"a": 1, "b": 2})
# --> ["a", 1, "b", 2]
'''

def dict_to_list(the_dict):
    result = []
    for item in the_dict:
        result.append(item)
        result.append(the_dict[item])
    return result
    # return [item, the_dict[item] for item in the_dict]
    # return list(reduce(lambda acc, item: acc + item + the_dict[item], the_dict, ""))

result = dict_to_list({"a": 1, "b": 2})

print(result)