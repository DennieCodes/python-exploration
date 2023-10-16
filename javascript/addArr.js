/* transpose this 2d array
input: 2d array
output: 1 4 2 5 3 6



*/

function transpose(arr) {
	// return arr.map((__, col) => twoDarr.map((row) => row[col])).flat();
	// return arr[0].map((__, col) => twoDarr.map((row) => row[col])).flat();

	return arr.map((item, idx) => console.log(item));
}

const twoDarr = [
	[1, 2, 3],
	[4, 5, 6],
];

const result = transpose(twoDarr);

console.log(result);
