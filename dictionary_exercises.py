# Problem 1
# Assign the following dictionary to a variable.

continents = {
  "Asia":["China", "Mongolia", "India"],
  "South America": ["Brazil", "Argentina", "Chile"],
  "North America": ["United States", "Canada", "Mexico"], "Antarctica": [],
  "Africa": ["South Africa", "Algeria", "Kenya", "Ethiopia", "Egypt"],
  "Europe": ["France", "Germany", "England", "Spain", "Greece", "Italy"],
  "Australia": ["New Zealand", "Australia", "Fiji"]
}

# Task: Use the dictionary to print the value of "Asia"
# print(continents.get("Asia"))

# Task: use the dictionary to print the third item in the value of "Australia"
# print(continents["Australia"][2])

# Task: print a list of all the keys, in alphabetical order
sorted_keys = []
for continent in continents:
    sorted_keys.append(continent)

sorted_keys.sort()
# print(sorted_keys)

# Problem 2
# Assign the following dictionary to a variable:

user = { "first_name": "Wally",
  "last_name": "McCrea",
  "years_experience": 4,
  "role": "graphic designer"
}
# Use the dictionary keys and string interpolation to print out this string:

# "The candidate, Wally McCrea has
# 4 years of experience as a graphic designer."

# print(f"The candidate, {user['first_name']} {user['last_name']} has {user['years_experience']} years as a {user['role']}")

# Problem 3
# Consider the following dictionary:

my_dict = {'a': 1, 'b': 2, 'c': 3}
# Task: Loop through the dictionary and create a new one where the values are the squares of the current values. Print the new dictionary.
# Expected output:
# {'a': 1, 'b': 4, 'c': 9}

new_dict = {}
for key in my_dict:
    new_dict[key] = my_dict[key]**2

# print(new_dict)

# Task: Write some code that prints a dictionary where the keys are the squares of the values and the values are the keys.
# Expected output:

# my_dict = {1: 'a', 4: 'b', 9: 'c'}

new_dict = {}
for key in my_dict:
    new_dict[my_dict[key]**2] = key

print(new_dict)