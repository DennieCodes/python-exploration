'''
This is kind-of like the second problem, but a little different...

This function takes a list of dictionaries (items) and dictionary of filters (filters). It should return a filtered copy of items with only the items that match any of the filters.

Example:

items = [
    {"color":"blue", "size":"small"},
    {"color":"red", "size":"small"},
    {"color":"purple", "size":"medium"},
    {"color":"green", "size":"large"},
]
filters = {
    "color": "blue",
    "size": "medium"
}

result = only_items_with(items, filters)
print(result) # --> [
    {"color":"blue", "size":"small"},
    {"color":"purple", "size":"medium"},
]
'''

# def just_these_fields(items, fields):
#     result = []
#     for item in items:
#         sub_dict = {key:value for key,value in item.items() if key in fields}
#         result.append(sub_dict)

#     return result

# def only_items_with(items, filters):
#     result = []
#     for dic in items:
#         for key,val in dic.items():
#             if (key,val) in filters.items():
#                 result.append(dic)
#                 break

#     return result

def only_items_with(items, filters):
    result = []

#     for item in items:
#         for (key, value) in item.items():
#             if (key, value) in filters.items():
#                 result.append(item)

    # return result

    for item in items:
        sub_dict = {key:value for key,value in item.items() if (key, value) in filters.items()}
        if sub_dict:
            result.append(item)

        return result

items = [
    {"color":"blue", "size":"small"},
    {"color":"red", "size":"small"},
    {"color":"purple", "size":"medium"},
    {"color":"green", "size":"large"},
]
filters = {
    "color": "blue",
    "size": "medium"
}

result = only_items_with(items, filters)
print(result)
# # --> [
#     {"color":"blue", "size":"small"},
#     {"color":"purple", "size":"medium"},
# ]