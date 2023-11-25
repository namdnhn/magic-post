import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { LocationDepth } from 'src/utils/interface';
import location from 'src/data/location-vn.json';

export const GET: RequestHandler = async ({ url }) => {
	try {
		let data: any;
		const depth: LocationDepth = Number(url.searchParams.get('depth'));

		switch (depth) {
			case LocationDepth.PROVINCE: {
				data = location.map((l) => {
					return { name: l.name, code: l.code };
				});
				break;
			}
			case LocationDepth.DISTRICT: {
				const province: any = findProvince(url, location);
				data = province.districts.map((l: any) => {
					return { name: l.name, code: l.code };
				});
				break;
			}
			case LocationDepth.WARDS: {
				const districtCode = Number(url.searchParams.get('district'));
				const provinceCode = findProvince(url, location);
				const district = provinceCode.districts.find((d: any) => d.code == districtCode);
				data = district.wards.map((l: any) => {
					return { name: l.name, code: l.code };
				});
				break;
			}
			default:
				break;
		}

		if (!data) {
			return json({
				status: 400,
				err: 'Get location failed!'
			});
		}
		return json({
			status: 201,
			data
		});
	} catch (err) {
		console.log('❗Error:', err);
		return json({
			status: 500,
			err: 'Server error!'
		});
	}
};

function findProvince(url: any, location: any[]) {
	const provinceCode = Number(url.searchParams.get('province'));
	const province = location.find((l: any) => l.code == provinceCode);
	return province;
}
