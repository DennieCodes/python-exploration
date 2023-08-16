'''
Asha has been stranded on an island for many days. He's grown terribly bored with his situation. He's started to find ordinary things immensely fascinating.

Today, he's interested in the waves he sees. He notes that at certain times of the day, the water level either increases or decreases. Realizing this phenomenon is due to tides, he's now most fervent about determining the difference in water level between high tide and low tide.

He's started measuring the water level throughout the day using a high-precision measuring device (that he had when he got marooned), such that each reading is a unique integer, that is, no two readings are the same.

He knows that after measuring the absolute minimum reading at low tide, the transition to the absolute maximum reading representing the water level at high tide consists of a strictly increasing sequence of water level readings.

He's interested in the difference between the absolute maximum and absolute minimum readings: the water level difference between the low and high tides.

He knows it's possible that he made a mistake in writing down some readings. In the case where the sequence between the low tide reading and high tide reading is not strictly increasing, then he knows that he messed up and will throw away that day's measurements.

Once he gets back to the mainland, he shares all of his daily measurements with you. He asks if you can help him calculate the difference between the low tide and the high tide for one of the days.

5
The bored castaway
Given a series of measurements, where each measurement is a unique number, in chronological order over a day, complete the function tide_difference to determine what the difference is between the low tide and high tide measures.

If the values between the low tide and the high tide do not always increase, then return None.

If there's no high tide after the low tide, return None.

Example 1:

Look at these measurements where the low tide and the high tide are in bold:

3, 1, 4, 6, 7, 5

The difference is 6.

Example 2:

Look at these measurements where the low tide and the high tide are in bold and a bad reading is italicized:

3, 1, 4, 6, 5, 7, 2

This is bad data and the function should return None.

Example 3:

Look at these measurements:

5, 4, 3, 2, 1

There is no high tide reading after the low tide. This is bad data and the function should return None.

input: a list of tide heights
output: difference between low tide and high tide

note:
1. values between low tide and high tide must increase
2. high tide has to come before low tide
3. if neither of these conditions are true then return difference between low and high tide
'''

def tide_difference(measurements):
    high_tide = max(measurements)
    low_tide = min(measurements)
    high_pos = measurements.index(high_tide)
    low_pos = measurements.index(low_tide)

    for num in range(low_pos+1, high_pos+1):
        if num == 0:
            continue
        if measurements[num-1] > measurements[num]:
            # print(f"compare: {measurements[num-1]} < {measurements[num]}")
            return None


    if low_pos > high_pos: # when low tide follows high tide
        return None

    return high_tide - low_tide

dataset = [
    [8, 1, 2, 6, 4, 5, 10, 7],
    [9, 1, 2, 3, 4, 19, 20, 8],
    [1, 2, 3, 4, 5, 6, 7],
    [7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 11, 8],
    [8, 1, 2, 3, 4, 5, 10]
]

result = tide_difference(dataset[1])
print(result)