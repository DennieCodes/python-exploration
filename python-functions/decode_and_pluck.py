'''
Implement this function: decode_and_pluck

Inputs:

input_json: a JSON encoded string that, once decoded, should be a Python dictionary
field: a list of field names that we want to extract
The function should decode input_json into a dictionary and then pluck out the fields named in fields as a new dictionary to return.

Example:

decode_and_pluck('{"a": 1, "b": 2, "c": 3}', ["a", "c"])
# --> {"a": 1, c": 3}

'''

import json

def decode_and_pluck(input_json, fields):
    loaded = json.loads(input_json)
    return { key: loaded[key] for key in loaded if key in fields}
    # return { key: input_json[key] for key in input_json if key in fields}


result = decode_and_pluck(
    '{"a": 1, "b": 2, "c": 3}', ["a", "c"],
)

print(result)