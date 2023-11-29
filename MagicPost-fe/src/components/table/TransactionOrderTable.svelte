<script lang="ts">
	import { PencilLine, Trash2 } from 'lucide-svelte';
	import type { TableTransactionOrderInteface } from 'src/utils/interface';

	export let tableData: TableTransactionOrderInteface[] = [];
</script>

<div class="table-container !rounded-none h-full">
	<table class="table table-hover overflow-auto !bg-transparent !rounded-none">
		<thead class="!bg-white">
			<tr>
				<th>STT</th>
				<th>Mã đơn hàng</th>
				<th>Điểm giao dịch</th>
				<th>Mã đơn giao dịch</th>
				<th>Thao tác</th>
			</tr>
		</thead>
		<tbody>
			{#each tableData as row, i}
				<tr>
					<td>{i + 1}</td>
					<td>{row.orderId}</td>
					<td>{row.address}</td>
					<td>{row.transactionId}</td>
					<td class="flex items-center gap-3">
						<button type="button" class="btn-icon variant-filled h-8 w-8"><PencilLine size="16" /></button>
						<button type="button" class="btn-icon variant-filled h-8 w-8"><Trash2 size="16" /></button>
					</td>
				</tr>
			{/each}
		</tbody>
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
</style>
