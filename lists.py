my_list = ["Evander", 22, True]
print(my_list)

days_of_week = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

print(days_of_week)

print("The first day of the week is", days_of_week[0])

days_of_week[3] = "Hump day!"
print(days_of_week)

days_of_week[5] = "FriYAY!"
print(days_of_week)

favorite_foods = []
food = input("What is one of your favorite foods? ")
favorite_foods.append(food)

food = input("What is another of your favorite foods? ")
favorite_foods.append(food)

food = input("Last time, one more favorite food? ")
favorite_foods.append(food)

print("Your fav foods are", favorite_foods)

num_foods = len(favorite_foods)
print("That's", num_foods, "of your favorite foods.")