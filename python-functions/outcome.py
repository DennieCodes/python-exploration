'''
There's an old game played by a group of kids. One gets a chocolate gold coin, but keeps it secret. Then, all the kids in the group play rock-paper-scissors. If you're holding the gold coin and your opponent wins rock-paper-scissors, then you surreptitiously give the gold coin to them. Otherwise, you hold on to the gold coin.

As many things do, this game has taken the adult world by storm. You're going to be on the leading edge of the fad with the first tournament Web site set up to track the gold coins tournaments.

9
Gold coin
Each round of the game has 26 players, labeled "A" through "Z". You're given the starting_player who has the gold coin, and a list of matches where each entry is a string of two letters denoting the two players in the match, the first the winner and the second the lower. Complete the function outcome to return the label of the player that has the gold coin at the end of the tournament.

Constraints: 1 <= len(matches) <= 100

Example:

Your function gets the value "Z" for starting_player, which means "Z" has the gold coin. For matches, your input list looks like this:

[ "ZA", "CD", "BZ", "SE", "FA", "LB"]

First match: ZA - Z wins and keeps the coin
Second match: CD - neither has the coin
Third match: BZ - B wins the coin from Z
Fourth match: SE - neither has the coin
Fifth match: FA - neither has the coin
Sixth match: LB - L wins the coin from B
Your function should return "L" for that input.

input: the letter player who starts with the coin
       a list of matches, in each string of two the first letter is the winner
output: the letter of the player with the gold coin

pseudocode:
1. set var to track who has the coin
2. iterate over the list of matches
3. search each match for coin holder
4. if the coin holder is in the match, check if they're in the second position
5. if no coin holder or they're in first then continue
6. if coin holder is in second position then give the coin to player in first position
7. at the end return whoever has the coin

'''

def outcome(starting_player, matches):
    coin_holder = starting_player

    for match in matches:
        if coin_holder in match:
            if match[1] == coin_holder:
              coin_holder = match[0]

    return coin_holder

start1 = "A"
matches1 = ['DK', 'SO', 'EI', 'XH', 'IE', 'XI', 'VY', 'DY', 'QI']
start2 = "A"
matches2 = ['FL', 'AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'XI', 'EI']
start3 = "A"
matches3 = ['XQ', 'AB', 'RQ', 'CB', 'DC', 'LA', 'QL', 'FE', 'GF']
start4 = "A"
matches4 = ['XQ', 'BA', 'RQ', 'CB', 'DC', 'LQ', 'ED', 'FE', 'GF']

expect1 = "A"
expect2 = "A"
expect3 = "Q"
expect2 = "G"


result = outcome(start3, matches3)
print(result)
