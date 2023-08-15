'''
You'd like to register an account for a new app that you've downloaded. You've already entered your email address and Social Security number, but it seems that the requirements for choosing a password are quite strict.

In order to "completely protect" your account from being hacked into, the password must be:

a string between 8 and 12 characters long (inclusive)
every character is either:
a lowercase letter (a … z)
an uppercase letter (A … Z)
a digit (0 … 9)
In addition to those rules, the password must contain:

at least two lowercase letters
at least three uppercase
at least two digits
You've got a potential password in mind. Rather than entering the password into the app and getting some nasty notification that it doesn't meet the requirements, you'd like to determine for yourself whether or not your password would validly satisfy all of the rules.

4
Strong password
Given an input string password, complete the function valid_password to return the string good if it's a valid password, or to return the string bad if it's an invalid password.

The criteria for the password are:

It must be have 8, 9, 10, 11, or 12 characters
It must have at least two lowercase letters (a … z)
It must have at least three uppercase letters (A … Z)
It must have at least two digits (0 … 9)
'''

def valid_password(password):
    convert = list(password)
    lower_count = len(list(filter(lambda item: item == item.lower() and item.isalpha(), convert)))
    upper_count = len(list(filter(lambda item: item == item.upper() and item.isalpha(), convert)))
    digit_count = len(list(filter(lambda item: item.isdigit(), convert)))

    if len(convert) < 8 or len(convert) > 12:
        return "bad"
    if lower_count < 2:
        return "bad"
    if upper_count < 3:
        return "bad"
    if digit_count < 2:
        return "bad"

    return "good"

pw1 = "F3i89SzI"
pw2 = "A231CcBbaD"
pw3 = "ne8ieZp3lp"
pw4 = "l8eipZnE3p"
pw5 = "EO8OBZ3z"

result = valid_password(pw3)
print(result)