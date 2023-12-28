<script lang="ts">
	import { invalidate } from '$app/navigation';
	import { Autocomplete, popup } from '@skeletonlabs/skeleton';
	import type { AutocompleteOption, PopupSettings } from '@skeletonlabs/skeleton';
	import { X } from 'lucide-svelte';
	import { OfficeType, Roles, type OfficesInterface, type StaffsInteface } from 'src/utils/interface';
	import { onMount } from 'svelte';
	import { LocationDepth, type LocationSchema } from 'src/utils/interface';
	import { slide } from 'svelte/transition';
	import axiosInstance from 'src/axios';

	export let id: string;
	export let leaderData: StaffsInteface[] = [],
		gatherPointData: OfficesInterface[] = [];
	export let officeData: OfficesInterface | null = null;
	let name: string,
		address: string,
		phoneNo: string,
		type = OfficeType.GATHERING,
		leader = '',
		leaderLabel = '',
		linkGatherPoint = '',
		gatherPointLabel = '';
	let loading = false,
		error: string;

	function onLeaderSelect(event: CustomEvent<AutocompleteOption<string>>): void {
		leaderLabel = event.detail.label;
		leader = event.detail.value;
	}

	function onGatherPointSelect(event: CustomEvent<AutocompleteOption<string>>): void {
		gatherPointLabel = event.detail.label;
		linkGatherPoint = event.detail.value;
	}

	async function createNewOffice() {
		const requiredBody = {
			name,
			phoneNo,
			address,
			adminId: leader,
			type
		};

		const body = { ...requiredBody, gatheringPointId: linkGatherPoint };

		Object.values(requiredBody).some(async (value) => {
			if (!value) {
				error = 'Có dữ liệu bắt buộc bị để trống!';
				return;
			}

			loading = true;

			if (type == OfficeType.GATHERING) {
				const postData = {
					name: name,
					address: address,
					phone: phoneNo,
					user_email: leader,
				}
				const response = await axiosInstance.post('/manage/gathering_point_by_current_user/', postData);
				if (response.status == 200) {
					(document.getElementById(id) as any).close();
					// invalidate((url) => url.pathname.includes('/api/admin/offices'));
				}
				loading = false;
				return;
			}
			
			const postData = {
				name: name,
				province_code: provinceCode,
				district_code: districtCode,
				ward_code: ward.value,
				address: address,
				phone: phoneNo,
				user_email: leader,
				gathering_point_id: parseInt(linkGatherPoint)
			}

			const response = await axiosInstance.post('/manage/transaction_point_by_current_user/', postData);

			if (response.status == 200) {
				(document.getElementById(id) as any).close();
				// invalidate((url) => url.pathname.includes('/api/admin/offices'));
			}
			loading = false;
			return;
		});
	}

	// async function getLeaderData() {
	// 	const response = await fetch('/api/admin/staffs', {
	// 		method: 'GET'
	// 	});

	// 	const data = await response.json();
	// 	return data.data.content;
	// }

	let leaderPopupSettings: PopupSettings = {
		event: 'focus-click',
		target: 'leader-autofill',
		placement: 'top'
	};
	let leaderAutoComplete: AutocompleteOption<string>[] = [];
	let gatherPopupSettings: PopupSettings = {
		event: 'focus-click',
		target: 'gatherPoint-autofill',
		placement: 'top'
	};
	let gatherAutoComplete: AutocompleteOption<string>[] = [];

	$: {
		// (leader = ''), (leaderLabel = ''), (linkGatherPoint = ''), (gatherPointLabel = '');
		leaderAutoComplete = [];
		leaderData
			.filter((leader) => {
				return leader.role.id == (type == OfficeType.TRANSACTION ? Roles.TRANSACTION_LEADER : Roles.GATHERING_LEADER);
			})
			.map((leader) => {
				leaderAutoComplete = [
					...leaderAutoComplete,
					{
						label: `${leader.userId} - ${leader.fullName}`,
						value: `${leader.id}`,
						keywords: `${leader.email}`,
						meta: { healthy: false }
					}
				];
			});

		gatherAutoComplete = [];
		gatherPointData.map((point) => {
			gatherAutoComplete = [
				...gatherAutoComplete,
				{
					label: `${point.pointId} - ${point.name}`,
					value: `${point.id}`,
					keywords: `${point.name}, ${point.pointId}, ${point.address}`,
					meta: { healthy: false }
				}
			];
		});
	}

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
		
	});

	onMount(async () => {
		if (officeData) {
			name = officeData.name;
			address = officeData.address;
			phoneNo = officeData.phoneNo;
			leaderLabel = officeData.leader?.fullName;
			// leaderData = await getLeaderData();
			// console.log('🚀 ~ file: OfficeModal.svelte:133 ~ leaderData:', leaderData);
		}

		location.provinces = await getLocationData(LocationDepth.PROVINCE);
	});
</script>

<dialog {id} class="dui-modal">
	<div class="dui-modal-box w-[44%] max-w-3xl py-4">
		<form method="dialog">
			<button class="dui-btn dui-btn-sm dui-btn-square dui-btn-ghost absolute right-2 top-3">✕</button>
		</form>
		<h3 class="text-xl text-center mb-2">
			{officeData ? `Chỉnh sửa` : 'Thêm mới'} điểm giao dịch/tập kết
		</h3>
		<div class="dui-divider m-0 -mx-6" />
		<main class="mb-3">
			<label class="dui-label pb-1" for="name">
				<span class="dui-label-text required-label">Tên điểm</span>
			</label>
			<input
				type="text"
				bind:value={name}
				name="name"
				placeholder="Nhập tên điểm"
				class="dui-input h-10 dui-input-bordered w-full"
			/>

			<label class="dui-label pb-1" for="address">
				<span class="dui-label-text required-label">Địa chỉ</span>
			</label>
			<input
			type="text"
			bind:value={address}
			name="address"
			placeholder="Nhập địa chỉ"
			class="dui-input h-10 dui-input-bordered w-full"
		/>
			{#if type == OfficeType.TRANSACTION}
			<div class="grid grid-cols-3 gap-1 w-full mb-1 mt-3">
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
			{/if}

			<label class="dui-label pb-1" for="address">
				<span class="dui-label-text required-label">Loại văn phòng</span>
			</label>
			{#if officeData}
				<input
					type="text"
					value={officeData.type ?? ''}
					name="type"
					disabled
					class="dui-input h-10 dui-input-bordered w-full"
				/>
			{:else}
				<div class="grid grid-cols-2 gap-3">
					<label class="dui-label cursor-pointer justify-start">
						<input
							type="radio"
							on:change={() => (type = OfficeType.GATHERING)}
							name="role-radio"
							class="dui-radio dui-radio-sm checked:bg-secondary-500"
							checked
						/>
						<span class="dui-label-text ml-2">Điểm tập kết</span>
					</label>
					<label class="dui-label cursor-pointer justify-start">
						<input
							type="radio"
							on:change={() => (type = OfficeType.TRANSACTION)}
							name="role-radio"
							class="dui-radio dui-radio-sm checked:bg-secondary-500"
						/>
						<span class="dui-label-text ml-2">Điểm giao dịch</span>
					</label>
				</div>
			{/if}

			<div class="flex justify-between gap-3">
				<div class="w-full">
					<label class="dui-label pb-1" for="phone">
						<span class="dui-label-text required-label">Số điện thoại văn phòng</span>
					</label>
					<input
						type="text"
						bind:value={phoneNo}
						name="phone"
						placeholder="Nhập số điện thoại"
						class="dui-input h-10 dui-input-bordered w-full"
					/>
				</div>
				<div class="w-full">
					<label class="dui-label pb-1" for="leader">
						<span class="dui-label-text required-label">Trưởng điểm quản lý</span>
					</label>
					<input
						type="search"
						name="leader"
						placeholder="Chọn trưởng điểm"
						class="dui-input h-10 dui-input-bordered w-full"
						use:popup={leaderPopupSettings}
						bind:value={leaderLabel}
					/>
					<div data-popup="leader-autofill" class="card w-full max-w-sm max-h-60 p-4 overflow-y-auto">
						<div class="w-full flex justify-end sticky top-0">
							<button class="dui-btn dui-btn-square dui-btn-xs">
								<X size={15} />
							</button>
						</div>
						{#if leaderAutoComplete.length == 0}
							<div>Không có nhân viên nào!</div>
						{:else}
							<Autocomplete
								options={leaderAutoComplete}
								bind:input={leaderLabel}
								on:selection={onLeaderSelect}
								transitionOutParams={{ delay: 0, duration: 0 }}
								emptyState="Không có kết quả nào"
							/>
						{/if}
					</div>
				</div>
			</div>

			{#if type == OfficeType.TRANSACTION}
				<div transition:slide={{ duration: 200 }}>
					<label class="dui-label pb-1" for="name">
						<span class="dui-label-text required-label">Điểm tập kết liên kết</span>
					</label>
					<input
						type="text"
						name="name"
						placeholder="Chọn điểm tập kết"
						class="dui-input h-10 dui-input-bordered w-full"
						use:popup={gatherPopupSettings}
						bind:value={gatherPointLabel}
					/>
					<div data-popup="gatherPoint-autofill" class="card w-full max-w-sm max-h-60 p-4 overflow-y-auto">
						<div class="w-full flex justify-end sticky top-0">
							<button class="dui-btn dui-btn-square dui-btn-xs">
								<X size={15} />
							</button>
						</div>
						{#if gatherAutoComplete.length == 0}
							<div>Không còn điểm tập kết trống!</div>
						{:else}
							<Autocomplete
								options={gatherAutoComplete}
								bind:input={linkGatherPoint}
								on:selection={onGatherPointSelect}
								transitionOutParams={{ delay: 0, duration: 0 }}
							/>
						{/if}
					</div>
				</div>
			{/if}
		</main>
		<div class="dui-divider m-0 -mx-6" />
		{#if error}
			<p class="text-fail text-end font-bold mt-1">{error}</p>
		{/if}
		<div class="flex justify-end gap-3 mt-[6px]">
			<form method="dialog">
				<button class="btn variant-outline-tertiary hover:text-primary-500 hover:variant-outline-error">
					Hủy bỏ
				</button>
			</form>
			<button class="btn variant-filled bg-secondary-600" disabled={loading} on:click={createNewOffice}>
				{#if loading}
					<span class="dui-loading dui-loading-spinner dui-loading-sm" />
				{:else}
					Thêm mới
				{/if}
			</button>
		</div>
	</div>
	<form method="dialog" class="dui-modal-backdrop">
		<button>close</button>
	</form>
</dialog>
