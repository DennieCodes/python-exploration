def find_multiples(integer, limit):
  # input: integer that you will make multiples of itself
  #        limit is limit of integer max
  # output: a list of the multiples of integer up to limit
  # range(int(limit / integer))
  return [integer * count for count in range(1, int(limit/integer)+1)]
  # return result

# SUBMITTED ON Codewars
#
# def find_multiples(integer, limit):
#     return list(range(integer, limit+1, integer))

result = find_multiples(2, 6)
print(result)