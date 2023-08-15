def add(*numbers):
    total = 0
    for num in range(len(numbers)):
        total += numbers[num]
    return total

total = add(1, 2, 3, 4)
# print(total)  # We expect 10

def double_splat(**mystery):
    print(mystery)

double_splat()
double_splat(name="Noor")
double_splat(first_name="Baz", last_name="Sayid")

def scammer(number):
    converted = str(number)
    if converted[0] == 2 or converted[0] == 4:
        if converted[4] == 2 or converted[4] == 4:
            if converted[6] == converted[7]:
                if converted[9] == 0:
                    return 'ignore'
    return 'accept'