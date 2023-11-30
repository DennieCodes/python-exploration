/*
Below is an implementation for bubble-sort in Python.

Recall that it "bubbles" the next largest value to the end of the list on each iteration of the outer loop.

def bubble_sort(items):
    length = len(items)
    for i in range(0, length-1):
        for j in range(0, length-(i+1)):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items
Now implement bubble-sort in JavaScript:

*/

function bubbleSort(items) {
	const arr_length = items.length;

	for (let i = 0; i < arr_length; i++) {
		for (let j = 0; j <= arr_length - (i + 1); j++) {
			if (items[j] > items[j + 1]) {
				[items[j], items[j + 1]] = [items[j + 1], items[j]];
			}
		}
	}

	return items;
}
items = [45, 13, 1, 5];
result = bubbleSort(items);
console.log(result);
