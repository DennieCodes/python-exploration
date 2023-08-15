'''
Many sportsball competitions have a "half-time", that is, the halfway point in the game. If a game is 20 minutes long, then the first half of the game is 10 minutes and the second half is 10 minutes.

Your friend Lulu has some old records of scores for different games. They ask you if you can write a program that, given the length of a game in minutes, determines how many times both teams had scored by half-time from two lists of times, one for each team. The lists of score times are when each team scored a point, but the time is in seconds.

For example, Lulu has this information for you:

Length of game: 48 minutes = 2880 seconds
Half-time: 24 minutes = 1440 seconds

Team 1: 10, 1400, 1500
Team 2: 7, 2000

Output: 3 points scored
        Team 1 scored two points in the first
          1440 seconds.
        Team 2 scored one point in the first
          1440 seconds.
1
Obligatory sportsball question
Given the game_length in minutes and two lists team_1_score_times and team_2_score_times, complete the function half_time_scores to determine the combined total number of times both teams scored in the first half.

The following function declaration is in a different format. When function names and parameter lists get really long, we will often put each parameter on its own line so that we can see the entire list without having to scroll right.
'''

def half_time_scores(
    game_length,  # in minutes
    team_1_score_times,  # each value is seconds
    team_2_score_times   # each value is seconds
):
    game_seconds = game_length * 60
    team1_scores = len(list(filter(lambda item: item <= game_seconds/2, team_1_score_times)))
    team2_scores = len(list(filter(lambda item: item <= game_seconds/2, team_2_score_times)))
    return team1_scores + team2_scores

team1 = [ 10, 1400, 1500 ]
team2 = [ 7, 2000 ]

result = half_time_scores(48, team1, team2)
print(result)