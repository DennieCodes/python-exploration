import calendar

def is_leap_day(year, month, day):
    if calendar.isleap(year) and month == 2 and day == 29:
        return True
    else:
        return False