# 1. Write a program to check whether a number entered is three digit number or not.

user_number = int(input("Please, enter a number: "))

if len(str(user_number)) == 3:
    print("The number is three digits")
else:
    print("The number is not three digits")

# 2. Write a program to find the lowest number out of two numbers inputed by a user.

user_first_number = int(input("Enter the first number: "))
user_second_number = int(input("Enter the second number: "))

if user_first_number < user_second_number:
    print(f"{user_first_number} is smaller than {user_second_number}")
elif user_second_number < user_first_number:
    print(f"{user_second_number} is smaller than {user_first_number}")
else:
    print("Something went wrong")

# 3. Write a program to check whether a number (inputed by the user) is divisible by both 2 and 3.

user_input = int(input("Enter a number (To check if it is divisible by both 2 and 3): "))

if user_input % 2 == 0 and user_input % 3 == 0:
    print(f"{user_input} is both divisible by 2 and 3")
else:
    print(f"{user_input} is not divisible by 2 and 3")

# 4. Accept as input three sides of a triangle and check whether it is an equilateral, isosceles, or scalene triangle

# an equilaterial is a triangle with three equal sides
# an isosceles is a triangle with two equal sides
# a scaelene triangle has 3 different sides

print("Enter each side of a triangle for analysis")

side_one = int(input("What is side 1? "))
side_two = int(input("What is side 2? "))
side_three = int(input("What is side 3? "))

if side_one == side_two and side_two == side_three:
    print(f"{side_one}, {side_two}, and {side_three} makes an equilateral triangle")
elif side_one != side_two and side_two != side_three and side_one != side_three:
    print(f"{side_one}, {side_two}, and {side_three} makes a scalene triangle")
else:
    print(f"{side_one}, {side_two}, and {side_three} makes an isosceles triangle")

# 5. Accept three numbers from the user and display the second largest number

num_one = int(input("Enter the first number: "))
num_two = int(input("Enter the second number: "))
num_three = int(input("Enter the third number: "))

if num_one > num_two and num_one < num_three:
    print(f"{num_one} is the second largest number.")
elif num_two > num_one and num_two < num_three:
    print(f"{num_two} is the second largest number.")
else:
    print(f"{num_three} is the second largest number.")

# 6. Write a program to convert temperatures to and from Celsius and Fahrenheit - take user input - "Input the temperature you like to convert? (e.g, 45F, 102C, etc..")

# sample output will look like
# Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : 104f
# The temperature in Celsius is 40 degrees.

user_input = input("Input the temperature you like to convert? (e.g, 45F, 102C, etc..): ")
temp = float(user_input[0:len(user_input)-1])
scale = user_input[len(user_input)-1].lower()

if scale == "f":
    new_temp = (temp - 32) / 1.8
    print(f"The temperature in Celsius is {new_temp}C")
elif scale == "c":
    new_temp = (temp * 1.8) + 32
    print(f"The temperature in Fahrenheit is {new_temp}F")
else:
    print("You have to put either a C or F after your temperature number")

# 7. Write a Python program to calculate a dog's age in dog years.
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

# sample output:
# Input a dog's age in human years: 12
# The dog's age in dog's years is 61

dog_age = int(input("Input a dog's age in human years: "))

if dog_age <= 2:
    relative_age = int(dog_age * 10.5)
else:
    relative_age = int((dog_age - 2) * 4 + 21)

print(f"The dog's age in dog years is {relative_age}.")

# 8. Write a Python program to check whether an alphabet is a vowel or consonant.

letter = input("Please, type a character to evaluate: ")

if letter == 'a' or letter == 'e' or letter == "i" or letter == 'o' or letter == 'u':
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is a consonant.")

# 9.Write a Python program to convert a month name to a number of days.

# sample output:
# List of months: January, February, March, April, May, June, July, August, September, October, November, December
# Input the name of Month: April
# No. of days: 30 days

# To check if a year is a leap year, divide the year by 4. If it is fully divisible by 4, it is a leap year.

# February - 28 days in a common year and 29 days in leap years

# June - 30 days
# April - 30 days
# September - 30 days
# November - 30 days

# January - 31 days
# March - 31 days
# May - 31 days
# July - 31 days
# August - 31 days
# October - 31 days
# December - 31 days

month = input("Input the name of Month: ").lower()

if month == "february":
    days = 28
elif month == "june" or month == "april" or month == "september" or month == "november":
    days = 30
elif month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
    days = 31
else:
    days = 0

# conditional for February
if days == 0:
    print("Please, enter a valid month")
elif month == "february":
    print(f"No. of days: {days} days.  Note February has 29 days on a leap year.")
else:
    print(f"No. of days: {days} days")
