months_in_year = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

for month_name in months_in_year:
    print(month_name)

for month_name in months_in_year:
    if len(month_name) > 8:
        print(month_name)

infinite_list = [1]
for item in infinite_list:
    print(item, len(infinite_list))
    infinite_list.append(item + 1)