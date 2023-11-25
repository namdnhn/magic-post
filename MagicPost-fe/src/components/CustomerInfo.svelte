<script lang="ts">
	import { LocationDepth, type LocationSchema } from 'src/utils/interface';
	import { onMount } from 'svelte';

	export let target: 'gửi' | 'nhận';

	let location = {
			provinces: [] as LocationSchema[],
			districts: [] as LocationSchema[],
			wards: [] as LocationSchema[]
		},
		provinceCode = -1,
		districtCode = -1;
	let district: HTMLSelectElement, ward: HTMLSelectElement;

	async function getLocationData(depth: number, provinceCode?: number, districtCode?: number) {
		const response = await fetch(`/api/location-vn?depth=${depth}&province=${provinceCode}&district=${districtCode}`, {
			method: 'GET'
		});

		const data = await response.json();
		return data.data;
	}

	onMount(async () => {
		location.provinces = await getLocationData(LocationDepth.PROVINCE);
	});
</script>

<div class="mb-3">
	<label class="dui-label pb-1" for="name">
		<span class="dui-label-text required-label">Họ và tên người {target}</span>
	</label>
	<input type="text" name="name" placeholder="Họ tên người {target}" class="dui-input h-10 dui-input-bordered w-full" />
</div>

<div class="mb-3">
	<label class="dui-label pb-1" for="phone">
		<span class="dui-label-text required-label">Số điện thoại người {target}</span>
	</label>
	<input
		type="text"
		name="phone"
		placeholder="Số điện thoại người {target}"
		class="dui-input h-10 dui-input-bordered w-full"
	/>
</div>

<div class="w-full mb-3">
	<label class="dui-label pb-1" for="address">
		<span class="dui-label-text required-label">Địa chỉ người {target}</span>
	</label>
	<div class="grid grid-cols-3 gap-1 w-full mb-1">
		<select
			name="type"
			required
			class="dui-select dui-select-sm dui-select-bordered w-full h-10"
			on:change={(e) => {
				location.wards = [];
				//@ts-ignore
				provinceCode = e.target.value;
				getLocationData(LocationDepth.DISTRICT, provinceCode).then((data) => {
					location.districts = data;
					district.selectedIndex = 0;
					ward.selectedIndex = 0;
				});
			}}
		>
			<option value="" disabled selected hidden>---Tỉnh/Thành phố---</option>
			{#each location.provinces as province}
				<option value={province.code}>{province.name}</option>
			{/each}
		</select>

		<select
			name="type"
			required
			class="dui-select dui-select-sm dui-select-bordered w-full h-10"
			bind:this={district}
			disabled={location.districts.length == 0}
			on:change={(e) => {
				//@ts-ignore
				districtCode = e.target.value;
				ward.selectedIndex = 0;
				getLocationData(LocationDepth.WARDS, provinceCode, districtCode).then((data) => {
					location.wards = data;
				});
			}}
		>
			<option value="" disabled selected hidden>---Quận/Huyện---</option>
			{#each location.districts as district}
				<option value={district.code}>{district.name}</option>
			{/each}
		</select>

		<select
			name="type"
			required
			class="dui-select dui-select-sm dui-select-bordered w-full h-10"
			disabled={location.wards.length == 0}
			bind:this={ward}
		>
			<option value="" disabled selected hidden>---Phường/Xã---</option>
			{#each location.wards as ward}
				<option value={ward.code}>{ward.name}</option>
			{/each}
		</select>
	</div>
	<input type="text" placeholder="Địa chỉ cụ thể" class="dui-input h-10 dui-input-bordered w-full" />
</div>

<style>
	select:invalid {
		color: #9ca3af;
	}

	select:focus {
		color: #000;
	}
</style>
