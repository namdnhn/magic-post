import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { token } from 'src/utils/stores';

export const load: PageServerLoad = async ({ cookies, fetch }) => {
	const accessToken = cookies.get('token') as string;

	if (!accessToken) {
		return {};
	}
	token.set(accessToken);

	const role = JSON.parse(atob(accessToken.split('.')[1]));

	try{
		
		return {
			accessToken,
			role
		};
	} catch(err){
		return {}
	}
};
