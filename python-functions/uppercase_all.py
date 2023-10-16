
def uppercase_all(strings):
  result = [item.upper() for item in strings];

  return result

result = uppercase_all([
    "arrays in JavaScript, lists in Python",
    "objects in JavaScript, dictionaries in Python"
])

print(result)