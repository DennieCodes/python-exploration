import calendar
import my_calendar
from dir_module import sub_module

year_str = input("What year were you born in? ")
year = int(year_str)

month_str = input("What month were you born in? ")
month = int(month_str)

day_str = input("What day were you born on? ")
day = int(day_str)

if calendar.isleap(year):
    print("That was a leap year!")
else:
    print("That was a normal year.")

if my_calendar.is_leap_day(year, month, day):
    print("You're a leap baby!")
else:
    print("You were born on a normal day.")

name = input("What is your name? ")

greeting = sub_module.create_greeting(name)

print(greeting)