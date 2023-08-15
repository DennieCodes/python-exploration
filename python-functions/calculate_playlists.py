'''
Raisa bought a used TiVo player from a garage sale. She gets it home and finds that, while it records and lets her play any TV show, she can't add or remove shows from the playlist.

The playlist always works with the first five episodes on the TiVo. Each episode is labeled by a letter: "A", "B", "C", "D", or "E".

The remote that Raisa has allows her to do only three things with the playlist:

Button 1 swaps the first two songs of the playlist
Pushing Button 1
Before:  "A", "B", "C", "D", "E"
After:   "B", "A", "C", "D", "E"

Button 2 moves the first song to the end of the playlist
Pushing Button 2
Before:  "A", "B", "C", "D", "E"
After:   "B", "C", "D", "E", "A"

Button 3 moves the last song of the playlist to the start of the playlist
Pushing Button 3
Before:  "A", "B", "C", "D", "E"
After:   "E", "A", "B", "C", "D"

Given a list of button numbers that Raisa pushes, what's the playlist look like after them?

1
World's worst TiVo
Given the input list of button numbers pressed button_pushes, complete the function calculate_playlist to figure out the final state of the playlist and return the episode labels in a list.

Button 1: swaps the first two songs of the playlist
Button 2: moves the first song to the end of the playlist
Button 3: moves the last song of the playlist to the start of the playlist
Constraint: 0 <= len(button_pushes) <= 100

Examples:

Pushes	Output	Reason
[]	["A", "B", "C", "D", "E"]	No button pushes
[1]	["B", "A", "C", "D", "E"]	Swap first two songs
[1, 2]	["A", "C", "D", "E", "B"]	...then move first song to end
[1, 2, 1]	["C", "A", "D", "E", "B"]	...then swap the first two songs
[1, 2, 1, 3]	["B", "C", "A", "D", "E"]	...then move last song to start

input: a list of numbers which represent button pushes
output: a list of the re-arranged episodes

'''

def calculate_playlist(button_pushes):
    eps = ["A", "B", "C", "D", "E"]
    for push in button_pushes:
        if push == 1:
            eps[0], eps[1] = eps[1], eps[0]
        elif push == 2:
            first = eps[0]
            eps = eps[1:]
            eps.append(first)
        elif push == 3:
            last = eps[4]
            eps.pop()
            eps.insert(0, last)

    return eps


data1 = [1, 2, 1, 3]

result = calculate_playlist(data1)
print(result)