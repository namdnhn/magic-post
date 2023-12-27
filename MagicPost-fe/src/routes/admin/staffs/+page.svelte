<script lang="ts">
	import { PlusCircle } from 'lucide-svelte';
	import StaffsTable from 'src/components/table/StaffsTable.svelte';
	import StaffsModel from 'src/components/modal/StaffsModal.svelte';
	import type { StaffsInteface } from 'src/utils/interface';
	import { onMount } from 'svelte';
	import axiosInstance from 'src/axios';

	let staffs: StaffsInteface[] = [];
	function createStaff() {
		(document.getElementById('admin_new_staff') as any).showModal();
	}

	onMount(async() => {
		const res1 = await axiosInstance.get('/manage/gathering_leaders');
		console.log(res1.data);
		staffs = res1.data;
		const res2 = await axiosInstance.get('/manage/transaction_leaders');
		console.log(res2.data);
		staffs = staffs.concat(res2.data)
	})
</script>

<main class="h-full">
	<div class="flex justify-between items-center mb-3">
		<h1 class="h3 uppercase">Danh sách tài khoản trưởng điểm</h1>
		<button class="btn variant-filled bg-ocean" on:click={createStaff}>
			<PlusCircle class="mr-1" size="20" /> Thêm mới
		</button>
		<StaffsModel id="admin_new_staff" />
	</div>
	<div class="card p-4 mb-3 !bg-[#fff]">
		<span class="mr-2">Tìm kiếm</span>
		<input
			type="text"
			placeholder="Nhập tên, mã nhân viên..."
			class="dui-input dui-input-bordered w-full max-w-xs !h-8"
		/>
	</div>
	<div class="card !rounded-b-none h-[calc(100%-7.5rem)]">
		<StaffsTable tableData={staffs} />
	</div>
</main>
