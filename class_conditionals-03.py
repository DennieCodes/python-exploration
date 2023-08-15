# 10. Write a Python program to display the astrological sign for a given date of birth.

# sample output:
# Input birthday: 18
# Input month of birth (e.g. march, july etc): january
# Your Astrological sign is : Capricorn

# Aries ♈️: March 21 - April 19
# Taurus ♉️: April 20 - May 20
# Gemini ♊️: May 21 - June 20
# Cancer ♋️: June 21 - July 22
# Leo ♌️: July 23 - August 22
# Virgo ♍️: August 23 - September 22
# Libra ♎️: September 23 - October 22
# Scorpio ♏️: October 23 - November 21
# Sagittarius ♐️: November 22 - December 21
# Capricorn ♑️: December 22 - January 19
# Aquarius ♒️: January 20 - February 18
# Pisces ♓️: February 19 - March 20

birthday = int(input("Input birthday: "))
month = input("Input month of birth: ").lower()

if month == "march":
    if birthday > 20:
        sign = "Aries ♈️"
    else:
        sign = "Pisces ♓️"
elif month == "april":
    if birthday > 20:
        sign = "Taurus ♉️"
    else:
        sign = "Aries ♈️"
elif month == "may":
    if birthday > 20:
        sign = "Gemini ♊️"
    else:
        sign = "Taurus ♉️"
elif month == "june":
    if birthday > 20:
        sign = "Cancer ♋️"
    else:
        sign = "Gemini ♊️"
elif month == "july":
    if birthday > 22:
        sign = "Leo ♌️"
    else:
        sign = "Cancer ♋️"
elif month == "august":
    if birthday > 22:
        sign = "Virgo ♍️"
    else:
        sign = "Leo ♌️"
elif month == "september":
    if birthday > 22:
        sign = "Libra ♎️"
    else:
        sign = "Virgo ♍️"
elif month == "october":
    if birthday > 22:
        sign = "Scorpio ♏️"
    else:
        sign = "Libra ♎️"
elif month == "november":
    if birthday > 21:
        sign = "Sagittarius ♐️"
    else:
        sign = "Scorpio ♏️"
elif month == "december":
    if birthday > 21:
        sign = "Capricorn ♑️"
    else:
        sign = "Sagittarius ♐️"
elif month == "january":
    if birthday > 19:
        sign = "Aquarius ♒️"
    else:
        sign = "Capricorn ♑️"
elif month == "february":
    if birthday > 18:
        sign = "Pisces ♓️"
    else:
        sign = "Aquarius ♒️"
else:
    sign = "invalid"

if sign == "invalid":
    print("You entered an invalid month")
else:
    print(f"Your Astrological sign is : {sign}")