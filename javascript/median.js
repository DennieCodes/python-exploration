/*

The median average is the value that occurs in the middle of a sorted list of numbers. For example, given this list:

[1, 10, 2, 8, 4]

its median average is 4 because, once its sorted, 4 is the middle value.

If you have an even number of items in the list, you find the middle two, then take the mean average of those. For example, if you have this list:

[1, 10, 2, 8, 4, 6]

its median average is 5, which is the mean average of 4 and 6.

Please complete the median function below to calculate the median average of an array of numbers. The list will never be empty.


input: list
output: median value if odd # of items, average of middle 2 if even

note: list is never empty
*/

function median(numbers) {
	numbers.sort((a, b) => a - b);

	let num_length = numbers.length;

	if (num_length % 2 !== 0) {
		let middle = Math.floor(num_length / 2);
		return numbers[middle];
	} else {
		console.log(numbers);
		let midLeft = numbers[num_length / 2 - 1];
		let midRight = numbers[num_length / 2];
		return (midLeft + midRight) / 2;
	}
}

const result = median([1, 10, 2, 8, 4, 6]);
console.log(result);
