import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { API_URL } from '$env/static/private';

export const GET: RequestHandler = async ({ cookies, url }) => {
	try {
		const token = cookies.get('token') as string;
		const typeOffices = url.searchParams.get('type')?.toString();
		const query = new URLSearchParams({
			type: typeOffices as any
		});

		const filterQuery = new URLSearchParams();
		for (let [key, value] of query.entries()) {
			if (value != 'null') filterQuery.append(key, value);
		}

		const response = await fetch(`${API_URL}/api/v1/admin/delivery-points?${filterQuery}`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			}
		});
		const data = await response.json();
		if (response.status != 200) {
			return json({
				status: response.status,
				error: data.message
			});
		}

		return json(data);
	} catch (err) {
		console.log('❗Error:', err);
		return json({
			status: 500,
			err: 'Server error!'
		});
	}
};

export const POST: RequestHandler = async ({ request, cookies }) => {
	try {
		const token = cookies.get('token') as string;
		const response = await fetch(`${API_URL}/api/v1/admin/delivery-points`, {
			method: 'POST',
			body: JSON.stringify(await request.json()),
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			}
		});
		const data = await response.json();
		if (response.status != 201) {
			return json({
				status: response.status,
				error: data.message
			});
		}

		return json(data);
	} catch (err) {
		console.log('❗Error:', err);
		return json({
			status: 500,
			err: 'Server error!'
		});
	}
};
