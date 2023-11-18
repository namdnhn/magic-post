import type { PageServerLoad } from './$types';

export const load: PageServerLoad = ({ cookies }) => {
	const accessToken = cookies.get('token');
	return {
		accessToken
	};
};
