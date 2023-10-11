'''
Write a function named repeats that checks if a string repeats itself.

repeats should take one argument, s, the string to test
For this exercise, you can assume that s is a string
If the first half of s equals the second half, then return true
If s is an empty string, then return true
Otherwise, return false
'''

def repeats(s):
    if s == '':
        return True

    # return len(s)
    length = len(s)
    half = int(len(s) / 2)

    print(s[0:half])
    print(s[half:length])

    return s[0:half] == s[half:length]


result = repeats("ABBA")

print(result)
	# if (s.length == 0) return true;

	# return s.slice(0, s.length / 2) === s.slice(s.length / 2, s.length);