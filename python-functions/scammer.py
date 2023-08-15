def scammer(number):
    converted = str(number)
    if converted[0] == '2' or converted[0] == '4':
        if converted[4] == '2' or converted[4] == '4':
            if converted[6] == converted[7]:
                if converted[9] == '0':
                    return 'ignore'
    return 'accept'

numbers = [ 2636218960, 2486288870, 2431298847, 2261442280, 2855422296, 2820422360, 4397249000, 4799239920, 4749209976, 4245456710, 4875486680, 4690406672]

for number in numbers:
    print(scammer(number))