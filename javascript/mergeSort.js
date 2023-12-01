/*

Today we are going to review the merge-sort. The merge sort is a little more complicated than the bubble and selection sorts from yesterday, so take your time and walk through the steps of the algorithm before you try to reimplement it in JavaScript.

1
Merge-sort in JavaScript
1 PT

Below is the Python implementation of merge-sort that you saw earlier in an exploration.

You may recall that merge sort works by splitting a list in half, sorting the two halves, and then "merging" the two halves back into one sorted list.

It is a recursive algorithm, so each time it sorts one of the halves, it actually splits that half in half and sorts and merges those halves back together. This continues until all of the sub-lists are of length 1 and trivial to merge back together.

For your reading pleasure:

"The Merge-Sort, A Tale of Two Functions (in Python)"
def merge_sort(values, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(values) - 1

    # Base case
    if left >= right:
        return

    # Recursive cases
    # Find the middle to split
    middle = (right + left) // 2

    # Sort the left half
    merge_sort(values, left, middle)

    # Sort the right half
    merge_sort(values, middle + 1, right)

    # Merge them together
    merge(values, left, middle, right)


def merge(values, left, middle, right):
    right_start = middle + 1

    # Terminal case to make sure we don't loop
    # forever
    if values[middle] <= values[right_start]:
        return

    # Merge the sub-lists by looping and comparing
    # the values at the start of each list
    while left <= middle and right_start <= right:
        # The one on the left is less than the
        # one on the right, so just keep going
        if values[left] <= values[right_start]:
            left += 1
        else:
            # In this case, the one on the right half
            # is less than one in the left half, so
            # we need to swap the values
            value = values[right_start]
            index = right_start

            # Move the all of the values to the right
            # by one
            while index != left:
                values[index] = values[index - 1]
                index -= 1

            # Put the value into the new "empty" place
            values[left] = value

            # Increment all of the indexes
            left += 1
            middle += 1
            right_start += 1
Now implement merge-sort in JavaScript

*/

const data = '';

function mergeSort(values, left = null, right = null) {
	if (left === null && right === null) {
		left = 0;
		right = values.length - 1;
	}

	if (left >= right) {
		return;
	}

	const middle = Math.floor((right + left) / 2);
	mergeSort(values, left, middle);
	mergeSort(values, middle + 1, right);
	merge(values, left, middle, right);
	return values;
}

// Merge
function merge(values, left, right, middle) {
	let right_start = middle + 1;

	if (values[middle] <= values[right_start]) return;

	while (left <= middle && right_start <= right) {
		if (values[left] <= values[right_start]) {
			left += 1;
		} else {
			let value = values[right_start];
			let index = right_start;

			while (index != left) {
				values[index] = values[index - 1];
				index -= 1;
			}

			values[left] = value;
			left += 1;
			middle += 1;
			right_start += 1;
		}
	}
}

/*

Merge values: 5,4, left: 0, right: 1, middle: 0
    1) should return [4,5]
Merge values: 1,7,4,10, left: 0, right: 3, middle: 1
    2) should return [1,4,7,10]

  mergeSort
Mergesort values: 1,2,3, left: null, right: null
    ✓ should return [1,2,3]
Mergesort values: 3,2,1, left: null, right: null
    3) should return [1,2,3]
Mergesort values: 45,13,1,5, left: null, right: null
    4) should return [1,5,13,45]

*/

const mergeData = [
	[5, 4], // Should return [4,5]
	[1, 7, 4, 10], // Should return [1,4,7,10]
];

const mergeSortdata = [
	[1, 2, 3], // [1,2,3]
	[3, 2, 1], // [1,2,3]
	[45, 13, 1, 5], // [1,5,13,45]
];

let values = mergeData[1];

const mergeResult = merge(values, 0, 1, 3);
// const mergeSortResult = mergeSort(mergeSortdata[0], null, null);

// console.log(mergeResult);
console.log(values);
