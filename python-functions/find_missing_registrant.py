'''
Every year, your city hosts a marathon. What's really interesting about it is that everyone who participates in the race finishes it, except one.

Given a list of names of registrants, and the names of the people who finish the race, find the one missing name.

2
Missing marathoner
Given a list registrants that contains the unique names of everyone who runs the race, and a list finishers that contains the names of all of the registrants who completed the race, complete the function find_missing_registrant to return the name of the one person who registered for the race and did not complete it.

Constraints: len(finishers) = len(registrants) - 1
'''

def find_missing_registrant(registrants, finishers):
    for runner in registrants:
        if not runner in finishers:
            return runner