# Problem 1
# Write a for loop so that every item in the list is printed

animals = ["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]

# for animal in animals:
#     print(animal)

# Problem 2
# Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Sam"

names = ["Sam", "Lisa", "Micha", "Fatima", "Wyatt", "Emma", "Sage"]

# for name in names:
#     print(f"Hello!, {name}")

# Problem 3
# Write a for loop that iterates through a string and prints every letter.

str = "Antarctica"

# for letter in str:
#     print(letter)

# Problem 4
# Using a for loop and .append() method append each item with a Dr. prefix to the lst.

lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2=[]

for name in lst1:
    lst2.append("Dr. " + name)

print(lst2)