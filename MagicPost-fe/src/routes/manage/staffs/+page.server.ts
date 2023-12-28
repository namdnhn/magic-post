import { lazyLoad } from 'src/lib/lazyLoad';
import { mergeQueries } from 'src/utils/helper';
import type { PageServerLoad } from './$types';
import axiosInstance from 'src/axios';

interface TransactionStaffs {
	transaction_staffs: {
		data: any[];
		status: number;
	};
}

interface GatheringStaffs {
	gathering_staffs: {
		data: any[];
		status: number;
	};
}

interface Staffs {
	staffs: {
		data: any[];
		status: number;
	};
}

export const load: PageServerLoad = async ({ parent, fetch, url }) => {
	await parent();

	try {
		const currentQuery = new URLSearchParams(url.search);
		const pageSize = (url.searchParams.get('pageSize') as string) ?? 10;
		const pageNumber = (url.searchParams.get('pageNumber') as string) ?? 1;
		const query = mergeQueries(
			currentQuery,
			new URLSearchParams({
				pageSize,
				pageNumber
			})
		);

		const staffs = await lazyLoad<Staffs>(axiosInstance.get(`/manage/all_staffs/`).then((res) => res.data));

		const transaction_staffs = await lazyLoad<TransactionStaffs>(
			axiosInstance.get(`/manage/transaction_staffs/`).then((res) => res.data)
		);

		const gathering_staffs = await lazyLoad<GatheringStaffs>(
			axiosInstance.get(`/manage/gathering_staffs/`).then((res) => res.data)
		);

		return {
			streamed: {
				staffs: staffs,
				transaction_staffs: transaction_staffs,
				gathering_staffs: gathering_staffs
			}
		};
	} catch (err) {
		console.log('❗Error:', err);
		return {
			err: 'Internal Server Error!'
		};
	}
};
