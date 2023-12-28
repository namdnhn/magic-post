import { lazyLoad } from '$lib/lazyLoad';
import axios from 'axios';
import type { PageLoad } from './$types';
import axiosInstance from 'src/axios';

interface Staffs {
	staffs: {
		data: any[];
		status: number;
	};
}

interface TransactionPoints {
	transactionPoints: {
		data: any[];
		status: number;
	};
}

interface GatheringPoints {
	gatheringPoints: {
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

	// const staffs = await lazyLoad<Staffs>(
	// 	fetch(`/api/admin/staffs`, {
	// 		method: 'GET'
	// 	}).then((res) => res.json())
	// );

	// const offices = await lazyLoad<Offices>(
	// 	fetch(`/api/admin/offices?type=${typeOffices}`, {
	// 		method: 'GET'
	// 	}).then((res) => res.json())
	// );

	const transactionPoints = await lazyLoad<TransactionPoints>(
		axiosInstance.get(`/manage/transaction_points`).then((res) => res.data)
	);

	const gatheringPoints = await lazyLoad<GatheringPoints>(
		axiosInstance.get(`/manage/gathering_points`).then((res) => res.data)
	);

	return {
		// staffs,
		// offices
		transactionPoints,
		gatheringPoints
	};
};
