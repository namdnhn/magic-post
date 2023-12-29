<script lang="ts">
	import { ArrowRightFromLine, ClipboardCheck, Eye, PencilLine, Trash2 } from 'lucide-svelte';
	import EmptyData from '../EmptyData.svelte';
	import OfficeModal from '../modal/OfficeModal.svelte';
	import DeleteConfirmModal from '../modal/DeleteConfirmModal.svelte';
	import type { Order, GatherOrderInteface } from 'src/utils/interface';

	export let tableData: Order[] = [];

	let checkedOrders: Set<any>;

	let checkAll: boolean = false,
		checks: boolean[] = [];
	let loading = false,
		error: string;

	function selectAllRow() {
		if (checkAll) {
			checks = new Array(tableData.length).fill(true);
			checkedOrders = new Set(tableData.map((td) => td.orderId));
		} else {
			checks = new Array(tableData.length).fill(false);
			checkedOrders = new Set();
		}
	}

	function onSelectOrder(i: number, row: Order) {
		if (checks[i] == true) checkedOrders.add(row.orderId);
		else checkedOrders.delete(row.orderId);
		checkedOrders = checkedOrders;
		if (checks.every((v) => v == true) && checks.length == tableData.length) checkAll = true;
		if (checks[i] == false && checkAll == true) checkAll = false;
	}
</script>

<div class="table-container !rounded-b-none !rounded-md h-full">
	<table class="table table-hover overflow-auto !bg-transparent !rounded-none" class:h-full={tableData.length == 0}>
		<thead class="!bg-white relative z-10">
			<tr>
				<th>
					<div class="flex items-center gap-2">
						<input
							class="dui-checkbox dui-checkbox-secondary dui-checkbox-sm rounded-sm border-[#000]"
							type="checkbox"
							bind:checked={checkAll}
							on:change={selectAllRow}
						/>
						STT
					</div>
				</th>
				<th>Mã đơn hàng</th>
				<th>Loại hàng</th>
				<th>Cước phí</th>
				<th>Ngày tạo</th>
				<th>Điểm tập kết </th>
				<th>Thao tác</th>	
			</tr>
		</thead>
		{#if tableData.length == 0}
			<tbody class="h-full relative">
				<EmptyData css="absolute top-1/4" message="Không có dữ liệu!" />
			</tbody>
		{:else}
			<tbody>
				{#each tableData as row, i}
					<tr class:row-selected={checks[i] == true}>
						<td class="flex items-center gap-2">
							<input
								class="dui-checkbox dui-checkbox-secondary dui-checkbox-sm rounded-sm border-[#000]"
								type="checkbox"
								bind:checked={checks[i]}
								on:change={() => onSelectOrder(i, row)}
							/>
							{i + 1}
						</td>
						<td>{row.orderId}</td>
						<td>Loại hàng</td>
						<td>999</td>
						<td>date</td>
						<td>Xuân Thủy</td>
							<td class="flex items-center gap-3">	
								<div class="dui-tooltip dui-tooltip-bottom" data-tip="Chuyển">
									<button
									type="button"
									class="btn-icon variant-filled h-8 w-8"
									data-tip="Xóa"
								>
									<ArrowRightFromLine size="16" />
								</button>
								</div>
							</td>
					</tr>
				{/each}
			</tbody>
		{/if}
		<tfoot />
	</table>
</div>

<style>
	thead th {
		position: sticky;
		top: 0;
		background-color: #fff;
		text-transform: none;
	}

	.table tbody td {
		padding-left: 1rem;
		vertical-align: middle;
	}

	.btn-icon {
		background-color: #4784af;
	}
</style>
