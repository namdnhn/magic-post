<script lang="ts">
	import { PencilLine, Trash2 } from 'lucide-svelte';
	import type { StaffsInteface } from 'src/utils/interface';
	export let tableData: StaffsInteface[] = [];
</script>

<div class="table-container !rounded-b-none !rounded-md h-full">
	<table class="table table-hover overflow-auto !bg-transparent !rounded-none">
		<thead class="!bg-white">
			<tr>
				<th>Mã nhân viên</th>
				<th>Họ tên</th>
				<th>Chức vụ</th>
				<th>Điểm quản lý</th>
				<th>Thao tác</th>
			</tr>
		</thead>
		<tbody>
			{#each tableData as row, i}
				<tr>
					<td>{row.id}</td>
					<td>{row.fullName}</td>
					<td>{row.role.name}</td>
					<td>{row.workAt ? row.workAt : 'Chưa có'}</td>
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
