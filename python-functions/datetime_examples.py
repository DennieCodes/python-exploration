from datetime import datetime, timedelta, date

datetime(1941, 5, 24,1, 30)
str(datetime(1941, 5, 24, 1, 30))

my_birthday = datetime(1974, 8, 1, 1, 30, 30)
# formatted =  my_birthday.strftime("%y-%m-%d %H:%M:%S")
# formatted = my_birthday.strftime("%A %B")
# print(my_birthday)

# Just a date
# Add code below to make the function return this specific date/time value: 1:13pm on January 28, 1998:

def a_specific_date():
    return datetime(1998, 1, 28, 13, 13)

'''
Add 30 minutes
The following function gets a datetime value as the parameter when. Please complete the function so that it returns a datetime that is thirty minutes later.

For example, if the value passed into the function is 2021-02-01 9:00am, then you should return a datetime value that represents 2021-02-01 9:30am.
'''

def add_thirty_minutes(when):
    return when + timedelta(minutes=30)

''' Strings to dates

Please complete the function that will take three strings in a list, one for the year, one for the month, and one for the day, and have it return a date that represents that day.

For example, let's say your function got the following input: ["2022", "11", "8"]. Your function should return a date object representing November 8, 2022.
'''

def make_a_date(values):
    [ year, month, day ] = values
    date_obj = datetime(int(year), int(month), int(day))
    return date_obj.date()

''' Find the difference
Complete the function to return the total number of days between two dates represented by date objects.

For example, given the first date of Jan 1, 2020, and the second date of Feb 2, 2022, then your function would return 763 which is the total number of days between those.

Your function should always return a positive integer.
'''

def date_diff_in_days(first, second):
    delta = first - second
    return abs(delta.days)

''' Between two dates

Complete the following function to return a list that contains the start date, then all of the dates up to and including end.

For example, if start is Jan 1, 2002, and end is Jan 10, 2022, then you would return a list that contains the following date values:

date(2002, 1, 1)
date(2002, 1, 2)
date(2002, 1, 3)
date(2002, 1, 4)
date(2002, 1, 5)
date(2002, 1, 6)
date(2002, 1, 7)
date(2002, 1, 8)
date(2002, 1, 9)
date(2002, 1, 10)
'''

def the_days_of_our_lives(start, end):
    days_difference = abs((start-end).days)
    incremental_days = start
    dates = []

    for day in range(days_difference+1):
        dates.append(incremental_days)
        incremental_days = incremental_days + timedelta(days=1)

    return dates

''' UNIX timestamp to 'date'
Complete the function to convert the UNIX timestamp in the parameter ts to a datetime.

For example, given the value 467056213 for ts, your function would return a datetime the represents Friday, October 19, 1984 5:50:13 PM
'''

def stamp_my_hand(ts):
    return datetime.fromtimestamp(ts)

# I'll gladly pay you Tuesday...
# Complete the function that returns a date that represents next Tuesday.

from datetime import timedelta, date

def hamburger_payment_due():
    currently = date.today()
    days_ahead = 1 - currently.weekday()

    if days_ahead <= 0:
        days_ahead += 7

    return currently + timedelta(days=days_ahead)
    # 0 = Monday, 1=Tuesday, 2=Wednesday...

# On Wednesday We Wear Pink
# Complete the function to return the number of months whose first day falls on a Wednesday from January 2000 through December 2022.


def wednesday_wilderness():
    start = datetime(2000, 1, 1)
    end = datetime(2022, 12, 31)
    # Offsets because we're looking for a range between two dates
    difference = abs(end.year+1 - start.year) * 12
    difference -= 1
    count = 0

    for month in range(difference):
        if start.weekday() == 2 and start.day == 1:
            count += 1

        if start.month == 12:
            start = start.replace(year = start.year + 1, month = 1)
        else:
            start = start.replace(month = start.month + 1)

    return count

print(wednesday_wilderness())

'''
2000-03-01
2000-11-01
2001-08-01
2002-05-01
2003-01-01
2003-10-01
2004-09-01
2004-12-01
2005-06-01
2006-02-01
2006-03-01
2006-11-01
2007-08-01
2008-10-01
2009-04-01
2009-07-01
2010-09-01
2010-12-01
2011-06-01
2012-02-01
2012-08-01
2013-05-01
2014-01-01
2014-10-01
2015-04-01
2015-07-01
2016-06-01
2017-02-01
2017-03-01
2017-11-01
2018-08-01
2019-05-01
2020-01-01
2020-04-01
2020-07-01
2021-09-01
2021-12-01
2022-06-01
'''

'''
2000-03-01
2000-11-01
2001-08-01
2002-05-01
2003-01-01
2003-10-01
2004-09-01
2004-12-01
2005-06-01
2006-02-01
2006-03-01
2006-11-01
2007-08-01
2008-10-01
2009-04-01
2009-07-01
2010-09-01
2010-12-01
2011-06-01
2012-02-01
2012-08-01
2013-05-01
2014-01-01
2014-10-01
2015-04-01
2015-07-01
2016-06-01
2017-02-01
2017-03-01
2017-11-01
2018-08-01
2019-05-01
2020-01-01
2020-04-01
2020-07-01
2021-09-01
2021-12-01
'''