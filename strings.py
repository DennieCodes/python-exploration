message = "This is a string in a Python file."
some_number = 1928

print("The message is", message)
print("The number is", some_number)

number_three = 3
string_three = "3"
print(number_three)
print(string_three)

converted_three = int(string_three)
print(converted_three == number_three)

response = input("How many walls are in your room?")
print("You typed:", response)
print("The value is a,", type(response))

num_walls = int(response)
print("My room has", num_walls + 1, "walls")

symbol = "*" # new line
title = "Dr."
name = "Syed"
combined = (symbol *2 ) + title + " " + name
print(combined)