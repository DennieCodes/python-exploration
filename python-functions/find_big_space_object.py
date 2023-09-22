'''
The input is a list of dictionaries where each dictionary represents an object in space that has a probability of smashing into earth. You're going help sort out the more dangerous objects for further analysis. Follow this pseudo-code:

big_objects = new list
for each of the input space objects
    if the object's estimated diameter is less than 1, skip it
    create a new dictionary with these fields (and values) from the space-object:
        * `estimated_diameter`
        * `impact_probability`
    encoded_object = json encode the dictionary
    add encoded_object to the big_objects list
return the big_objects list
'''

import json
def find_big_space_objects(space_objects):
  big_objects = []

  for item in space_objects:
    if item["estimated_diameter"] > 1:
      object = { "estimated_diameter" : item["estimated_diameter"], "impact_probability": item["impact_probability"] }

      encoded = json.dumps(object)
      big_objects.append(encoded)

  return big_objects



data = [{'estimated_diameter': 1.5, 'impact_probability': 0.0001, 'mass': 300}, {'estimated_diameter': 0.5, 'impact_probability': 0.0101, 'mass': 30}, {'estimated_diameter': 10.5, 'impact_probability': 0.1001, 'mass': 30000}]

result = find_big_space_objects(data)

print(result)
