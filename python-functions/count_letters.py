def count_letters(string):
  count = 0
  idx = 0

  for i in range(0, len(string), 2):
    if i < idx and idx != 0:
      continue

    if string[i] == "H":
      if "A" in string[i:]:
        idxA = string.index("A")
        if "C" in string[idxA:]:
          idxC = string.index("C")
          if "K" in string[idxC:]:
            count += 1
            idx = string.index("K")

  return count
#     list = []

#     for i in range(0, len(string), 2):
#         if (i != len(string)-1):
#             list.append(string[i] + string[i+1])

#     print(list)
#     return list.count("HA")

data = [
"HXAXHX",
"HHHHHAAAAA",
"HXAXHXA",
"FFF"
]


result = count_letters(data[1])
print(result)