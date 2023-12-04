import { lazyLoad } from '$lib/lazyLoad';
import type { PageLoad } from './$types';

interface Staffs {
	staffs: {
		data: any[];
		status: number;
	};
}

interface Offices {
	offices: {
		data: any[];
		status: number;
	};
}

export const load: PageLoad = async ({ parent, fetch, url }) => {
	await parent();

	const typeOffices = url.searchParams.get('type');

	const staffs = await lazyLoad<Staffs>(
		fetch(`/api/admin/staffs`, {
			method: 'GET'
		}).then((res) => res.json())
	);

	const offices = await lazyLoad<Offices>(
		fetch(`/api/admin/offices?type=${typeOffices}`, {
			method: 'GET'
		}).then((res) => res.json())
	);

	return {
		staffs,
		offices
	};
};
