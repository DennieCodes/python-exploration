'''
Ken travels a lot. When he's in Nevada waiting for his airplane, he likes to play the slot machines in the airport. There are only three slot machines, and Ken is the only player.

Each slot machine takes one quarter. Ken usually has some loose change in his pocket from the toll booths that he encounters in his rental car.

His strategy is simple. He starts at the first slot machine and drops in a quarter, pulls the lever, and if any quarters come out, he collects them. Then, he moves to the second slot machine and does the same thing. Then, he moves to the third slot machine and does the same thing. Once he's done with the third slot machine, he moves back to the first slot machine. He just keeps going until he runs out of quarters.

What Ken doesn't know is that the airport has rigged the slot machines.

The first slot machine pays 20 quarters every 27th time it's played.
The second slot machine pays 50 quarters every 100th time it's played.
The third slot machine pays 7 quarters every 8th time it's played.
How many times can Ken play before he runs out of quarters?

10
Playing the slots
Given the value num_quarters, complete the function calculate_plays to return the number of times Ken plays the slot machines before running out of quarters.

Ken plays the first slot machine, then the second, then the third, then back to the first, and keeps going until he runs out of quarters.
The first slot machine pays 20 quarters every 27th time it's played.
The second slot machine pays 50 quarters every 100th time it's played.
The third slot machine pays 7 quarters every 8th time it's played.
Constraints: 1 <= num_quarters <= 1000

input: number of starting quarters
output: the number of times Ken plays the slot machines before he runs out of quarters

rules:
The first slot machine pays 20 quarters every 27th time it's played.
The second slot machine pays 50 quarters every 100th time it's played.
The third slot machine pays 7 quarters every 8th time it's played.
Constraints: 1 <= num_quarters <= 1000

pseudocode:
1. Initialize count of quarters, initialize number of plays
2. Initialize list tracking plays on each machine
3. Track which machine goes next
3. Iterate over num_quarters until it equals zero, add 1 to play_count
4. Check each machine for when it pays out
5. If a machine pays out then reset its count and increase quarters accordingly
6. continue playing until quarters run out
7. return number of plays

'''

def calculate_plays(num_quarters):
    play_count = 0
    quarters = num_quarters
    machine_play_count = [ 0, 0, 0 ]
    next_machine = 0

    inf_count = 0 # to avoid infinite loop

    while quarters > 0:
        play_count += 1
        quarters -= 1

        if next_machine == 0:
            machine_play_count[0] += 1
            if machine_play_count[0] == 27:
                quarters += 20
                machine_play_count[0] = 0
            next_machine = 1
        elif next_machine == 1:
            machine_play_count[1] += 1
            if machine_play_count[1] == 100:
                quarters += 50
                machine_play_count[1] = 0
            next_machine = 2
        elif next_machine == 2:
            machine_play_count[2] += 1
            if machine_play_count[2] == 8:
                quarters += 7
                machine_play_count[2] = 0
            next_machine = 0

        # To stop infinite loop
        if inf_count > 3300:
            break
        inf_count += 1
        # block

    return play_count

dataset = [ 1000, 100, 10, 30, 500 ]
results = [ 3211, 189, 10, 37, 1487]

for num in range(len(dataset)):
    result = calculate_plays(dataset[num])
    if result == results[num]:
        print("passed")
    else:
        print(f"Test #{num} failed, calculate_plays({dataset[num]}) did not return: {results[num]} as expected.")
        print(f"Instead: {result} was returned")
