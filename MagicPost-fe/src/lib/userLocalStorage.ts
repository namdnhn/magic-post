export function setUserStorage(data: any) {
	localStorage.setItem('user', JSON.stringify(data));
}

export function getUserStorage() {
	const user = localStorage.getItem('user');
	if (!user) {
		return null;
	}
	return JSON.parse(user);
}
