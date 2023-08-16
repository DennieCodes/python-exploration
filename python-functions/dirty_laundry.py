'''
There are a lot of software development conferences that you can attend. Normally, when you go to one, they give you a free T-shirt!

Samir really likes going to conferences because he hates doing laundry. Samir only does his laundry when all of his t-shirts are dirty. As he goes to more and more conferences, this allows Samir to delay having to do laundry for longer periods of time.

Samir starts with a certain number of t-shirts. He wears one clean shirt every day, after which it becomes dirty. If the day begins and Samir has only dirty shirts, then he will do his laundry, which makes all of his shirts clean again. If Samir goes to a conference, then he gets one new clean shirt. Samir only gets a new shirt from the conference after putting on a clean shirt.

For example, you want to determine how many times Samir does laundry over a 10-day period given that:

Samir starts with one clean shirt

Samir attends an event on the third day and the seventh day

Day 1, Samir wakes up and wears his one clean shirt

Day 2, Samir wakes up and has no clean shirts, does laundry, and wears his one clean shirt

Day 3, Samir wakes up and has no clean shirts, does laundry, and wears his one clean shirt, and gets a new shirt

Day 4, Samir wakes up and has one clean shirt, one dirty shirt, and wears his one clean shirt

Day 5, Samir wakes up and has no clean shirts, does laundry, wears one clean shirt, and folds his other clean shirt

Day 6, Samir wakes up and has one clean shirt, one dirty shirt, and wears his one clean shirt

Day 7, Samir wakes up and has no clean shirts, does laundry, wears one clean shirt, folds his other clean shirt, and gets a new shirt

Day 8, Samir wakes up and has two clean shirts, one dirty shirt, and wears one of the clean shirts

Day 9, Samir wakes up and has one clean shirt, two dirty shirts, and wears his one clean shirt

Day 10, Samir wakes up and has no clean shirts, does laundry, wears one clean shirt, and folds the two other clean shirts

Samir does laundry 5 times.

Write a program that determines how many times Samir has to do his laundry for a given number of days.

4
Dirty laundry
Given the number of clean shirts that Samir has num_shirts, the number of days that you're interested in monitoring num_days, and a list of days on which there are events event_days, complete the function num_laundry_days to return the number of times that Samir will have to do laundry during num_days.

Samir begins this time with all clean t-shirts
Each day Samir wears a clean shirt, which becomes dirty
Each day Samir goes to a conference, he gets one new clean shirt
When Samir has no clean t-shirts, he does his laundry, which makes all his t-shirts clean again
Constraints:

1 <= num_shirts <= 100
1 <= num_days <= 1000
1 <= len(event_days) <= 100

input: number of shirts (int), number of days to monitor (int), event days (list)
output: number of times has to do laundry

note:
1. begins with all clean shirts
2. everyday a clean shirt becomes dirty
3. every day there is a conference a clean shirt is added to the pile
4. when there are no clean shirt, the laundry has to be done

pseudocode:
1. iterate number of days
2. track num of running clean shirts (start with num_shirts)
3. track num of total shirts
4. when there is an event day add another shirt

'''

def num_laundry_days(num_shirts, num_days, event_days):
    laundry = 0
    total_shirts = num_shirts
    clean_shirts = num_shirts

    for day in range(1, num_days+1):
        # print(f"start day: {day}, clean: {clean_shirts}, total: {total_shirts}, laundry: {laundry}")
        if clean_shirts == 0:
            laundry += 1
            clean_shirts = total_shirts-1
        else:
            clean_shirts -= 1

        if day in event_days:
            total_shirts += 1
            clean_shirts += 1
        # print(f"end day: {day}, clean: {clean_shirts}, total: {total_shirts}, laundry: {laundry}\n")

    return laundry

numshirt1 = 1
numdays1 = 10
eventdays1 = [10]

numshirt2 = 1
numdays2 = 10
eventdays2 = [ 2, 5, 9 ]

result = num_laundry_days(numshirt1, numdays1, eventdays1)
print(result)
