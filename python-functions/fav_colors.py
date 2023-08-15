def get_num_colors():
    num_colors_str = input("How many fav colors do you have? ")
    num_colors = int(num_colors_str)
    return num_colors

def get_color(color_number):
    num = str(color_number + 1)
    prompt = "What is your #" + num + " fav color? "
    color = input(prompt)
    return color

print("Hi, I'd like to ask you about yoru fav colors.")
num_colors = get_num_colors()

print("Thanks! I will now ask you for each of those.")
favorite_colors = []

for color_number in range(num_colors):
    color = get_color(color_number)

    favorite_colors.append(color)

sorted_colors = sorted(favorite_colors)

print("Thank you! I have your fav colors as:")

for color in sorted_colors:
    print(" ", color)