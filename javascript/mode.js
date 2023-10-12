/*

The mode average is the number that occurs most often in a list of numbers. For example, the mode average in the following list is 4:

[1, 4, 10, 2, 8, 4, 6, 4]

Please complete the mode function to find the mode average of an array of numbers. The array will never be empty. There will only be one modal value.

*/

function mode(numbers) {
	let obj = {};

	for (let number of numbers) {
		obj[number] = obj[number] === undefined ? 1 : (obj[number] += 1);
	}

	let count = 0;
	let mode = 0;

	for (let key in obj) {
		if (obj[key] > count) {
			count = obj[key];
			mode = key;
		}
	}

	return parseInt(mode);
}

let data = [6, 8, 3, 7, 3];
const result = mode(data);

console.log(result);
