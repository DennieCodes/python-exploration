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

def only_items_with(items, filters):
    result = []

    for dict in items:
          for item in dict:
               if item in filters:
                    result.append(dict)
                    break

    # loop over the things, get the things you want

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