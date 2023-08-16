'''
Every evening villagers in a small village gather around a big fire and sing songs.

A visitor to the community is the traveling minstrel. Every evening, if the minstrel is present, he sings a brand new song that no villager has heard before, and no other song is sung that night. In the event that the minstrel is not present, other villagers sing without him and exchange all songs that they know.

Given the list of villagers present for some number of consecutive evenings, you should calculate the total number of villagers that know all of the songs.

For example, let's say there are 5 villagers in the village, numbered 1, 2, 3, 4, and 5. Let's say the minstrel is represented by the number 0. Here's a record of each evening:

Evening #	Attendees	Who knows all the songs	Reason
1	2, 4	2, 4	2 and 4 know all the songs
2	0, 1, 2	2	Only 2 knows all the songs sung
3	1, 3, 4	1, 2, 3, 4	1 knows the song from evening 2, and four knows the songs from evening 1, sharing them they now know all the songs
4	1, 2	1, 2, 3, 4	Nothing changes
5	0, 5		5 now knows a new song that no one else knows and doesn't know any other songs
6	3, 5	3, 5	3 and 5 share their songs and now know all of them
The result is 2, just the villagers 3 and 5 know all of the songs.

Given the number of villagers num_villagers and a list of lists attendees_lists that record the attendees each evening, where 0 is the minstrel and all other numbers are the villagers, complete the function total_song_knowers to calculate the total number of villagers that know all the songs.

output: total # of villagers who know all of the songs
'''

def total_song_knowers(num_villagers, attendees_lists):
    villagers = {}
    song_list = []
    current_song = "a"

    # create villagers based on num_villagers
    for num in range(1, num_villagers+1):
        villagers[num] = []

    for attendees in attendees_lists:
        if 0 in attendees:
            # create a new song
            current_song = chr(ord(current_song) + 1)
            # add song to list
            song_list.append(current_song)
            # pass song to other attendees
            for villager in attendees:
                if not villager == 0:
                    villagers[villager].append(current_song)
        else:
            # iterate over the current attendees and create a common song set
            common_songs = set()
            for villager in attendees:
                common_songs.update(villagers[villager])

            # iterate again over the present villagers and make sure they have the whole song set
            for villager in attendees:
                villagers[villager] = list(common_songs)

    # count the number of villagers who have same length songs as the song_list
    return len(list(filter(lambda item: len(song_list) == len(villagers[item]), villagers)))

num1 = 3
data1 = [[0, 1], [1, 2, 3], [3, 1, 0]]

num2 = 4
data2 = [[0, 2], [1, 0], [1, 0, 3, 4]]

num3 = 7
data3 = [[0, 2, 4, 3], [4, 5], [5, 6, 7], [5, 1], [1, 5, 7, 0]]

result = total_song_knowers(num1, data1)
print(result)