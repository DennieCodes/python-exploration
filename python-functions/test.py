# def count_matches(items, param2=None):
#     matches = []
#     for item in items:
#         if(item.get("color") == param2):
#             matches.append(item)
#             print(matches)
#     return len(matches)

# input = [
#     {"background": "green",  "size": 5,  "color": "blue"},
#     {"background": "yellow", "size": 5,  "color": "green"},
#     {"background": "blue",   "size": 25, "color": "green"},
#     {"background": "yellow", "size": 5,  "weight": "light"},
# ]

# result = count_matches(input)
# print(result)

# def calculate_prefix_sums(nums, index):
#     prefix_sum = 0
#     while index >= 0:
#         i = 0
#         while i <= index:
#             prefix_sum += nums[i]
#             i += 1
#         index -= 1
#         return prefix_sum

# result = calculate_prefix_sums([1, 2, 3, 4], 2)

# def pairwise_sums(values):
#     sums = []
#     loop_limit = len(values) - 1
#     for index in range(loop_limit):
#         next_index = index + 1
#         sum = values[index] + values[next_index]
#         sums.append(sum)
#     return sums

# print(pairwise_sums([1]))

# print(list(enumerate(['A', 'B', 'C'])))

class Mammal:
    def __init__(self, temperature, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.temperature = temperature

class Flyer:
    altitude = 0

    def flap(self):
        self.altitude += 10

    def dive(self):
        self.altitude -= 10

class Bat(Mammal, Flyer):
    pass

# bat = Bat({ "temperature": 90})
bat = Bat(90)
print(bat.temperature)