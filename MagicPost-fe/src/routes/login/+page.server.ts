import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ cookies, parent }) => {
	await parent();
	const accessToken = cookies.get('token')?.toString();
	if (!accessToken) {
		return {};
	}

	throw redirect(301, '/');
};
