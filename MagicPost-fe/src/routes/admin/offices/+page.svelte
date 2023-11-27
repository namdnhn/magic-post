<script lang="ts">
	import { PlusCircle } from 'lucide-svelte';
	import type { OfficeTableInterface } from 'src/utils/interface';
	import OfficesTable from 'src/components/table/OfficesTable.svelte';

	let officeType: 'giao dịch' | 'tập kết';
	let offices: OfficeTableInterface[] = [
		{
			id: '1',
			name: 'Diem tap ket so 1',
			phone: '0123456789',
			address: '144 Xuân Thủy',
			manager: 'Minh Khoi'
		},
		{
			id: '2',
			name: 'Diem tap ket so 2',
			phone: '0987654321',
			address: '144 Xuân Thủy',
			manager: 'Minh Khoi'
		}
	];
	function createStaff() {
		// (document.getElementById('admin_new_staff') as any).showModal();
	}
	offices = new Array(5).fill(offices).flat();
</script>

<main class="h-full">
	<div class="flex justify-between items-center mb-3">
		<h1 class="h3 uppercase">Danh sách điểm tập kết - điểm giao dịch</h1>
		<button class="btn variant-filled bg-ocean" on:click={createStaff}>
			<PlusCircle class="mr-1" size="20" /> Thêm mới
		</button>
	</div>
	<div class="card p-4 mb-3 grid grid-cols-3 gap-10 !bg-[#fff]">
		<div class="flex items-center">
			<span class="mr-2 min-w-max">Tìm kiếm</span>
			<input
				type="text"
				placeholder="Nhập tên, mã điểm"
				class="dui-input dui-input-bordered !h-8 w-full max-w-xs"
			/>
		</div>
		<div class="flex items-center">
			<span class="mr-2 min-w-max">Loại điểm</span>
			<select
				name="type"
				required
				class="dui-select dui-select-sm dui-select-bordered w-full !h-8"
				bind:value={officeType}
			>
				<option value="" disabled selected hidden>---Chọn loại điểm chuyển phát---</option>
				<option value="giao dịch">Điểm giao dịch</option>
				<option value="tập kết">Điểm tập kết</option>
			</select>
		</div>
	</div>
	<div class="card !rounded-b-none h-[calc(100%-7.5rem)]">
		<OfficesTable tableData={offices} {officeType} />
	</div>
</main>

<style>
</style>
