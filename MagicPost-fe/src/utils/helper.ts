export function removeNullQueries(query: URLSearchParams) {
	const filterQuery = new URLSearchParams();
	for (let [key, value] of query.entries()) {
		if (value != 'null' && value != '') filterQuery.append(key, value);
	}

	return filterQuery;
}

export function mergeQueries(currentQuery: URLSearchParams, nextQuery: URLSearchParams) {
	if (currentQuery.get('pageNumber')) {
		currentQuery.set('pageNumber', '1');
	}
	for (let [key, val] of nextQuery.entries()) {
		currentQuery.set(key, val);
	}

	return removeNullQueries(currentQuery).toString();
}
