function selectionSort(items) {
	const length = items.length;

	for (let i = 0; i < length - 1; i++) {
		let min_idx = i;
		let min_value = items[i];

		for (let j = i + 1; j < length; j++) {
			if (items[j] < min_value) {
				min_idx = j;
				min_value = items[j];
			}
		}
		if (min_idx > i) {
			[items[i], items[min_idx]] = [items[min_idx], items[i]];
		}
	}

	return items;
}

items = [22, 13, 4, 9];
const result = selectionSort(items);
console.log(result);
