/*
Write a function named repeats that checks if a string repeats itself.

repeats should take one argument, s, the string to test
For this exercise, you can assume that s is a string
If the first half of s equals the second half, then return true
If s is an empty string, then return true
Otherwise, return false
*/

function repeats(s) {
	if (s.length == 0) return true;

	return s.slice(0, s.length / 2) === s.slice(s.length / 2, s.length);
}
