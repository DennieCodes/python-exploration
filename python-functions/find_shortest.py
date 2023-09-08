def find_shortest(list):
  list.sort(key=lambda x: len(x))
  return list[0]

# my_list.sort(key=lambda x: len(x))


result = find_shortest([[1, 2, 3], [3, 2], [1, 2, 11, 200]])

print(result)