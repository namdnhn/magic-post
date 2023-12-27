<script lang="ts">
	import { PencilLine, Trash2 } from 'lucide-svelte';
	import type { OfficesInterface } from 'src/utils/interface';
	import EmptyData from '../EmptyData.svelte';
	import OfficeModal from '../modal/OfficeModal.svelte';
	import DeleteConfirmModal from '../modal/DeleteConfirmModal.svelte';
	import { invalidate } from '$app/navigation';

	export let tableData: OfficesInterface[] = [];
	export let officeType: 'giao dịch' | 'tập kết' | 'toàn bộ';

	async function showEditOfficeModal(modalId: string, officeId: string) {
		(document.getElementById(modalId) as any).showModal();
	}

	function showDeleteOfficeModal(modalId: string) {
		(document.getElementById(modalId) as any).showModal();
	}

	async function deleteOffice(deleteId: string) {
		const response = await fetch(`/api/admin/offices/${deleteId}`, {
			method: 'DELETE'
		});

		if (response.status == 200) {
			invalidate((url) => url.pathname.includes('/api/admin/offices'));
		}
	}
</script>

<div class="table-container !rounded-b-none !rounded-md h-full">
	<table class="table table-hover overflow-auto !bg-transparent !rounded-none" class:h-full={tableData.length == 0}>
		<thead class="!bg-[#fff]">
			<tr>
				<th>STT</th>
				<th>Mã điểm</th>
				<th>Tên điểm {officeType != 'toàn bộ' ? officeType : ''}</th>
				<th>SĐT liên lạc</th>
				<th>Trưởng điểm</th>
				<th>Địa chỉ</th>
				{#if officeType == 'giao dịch'}
					<th>Điểm tập kết liên kết</th>
				{/if}
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
					<tr>
						<td>{i + 1}</td>
						<td>{row.pointId}</td>
						<td>{row.name}</td>
						<td>{row.phoneNo}</td>
						<td>{row.leader ? row.leader.fullName : 'Không có'}</td>
						<td>{row.address}</td>
						{#if officeType == 'giao dịch'}
							<td>{row.gatheringPoint?.name}</td>
						{/if}
						<td class="flex items-center gap-3">
							<button
								type="button"
								class="btn-icon variant-filled h-8 w-8"
								on:click={() => showEditOfficeModal('edit-office' + row.pointId, row.id)}
							>
								<PencilLine size="16" />
							</button>
							<OfficeModal id={'edit-office' + row.pointId} officeData={row} />
							<button
								type="button"
								class="btn-icon variant-filled h-8 w-8"
								on:click={() => showDeleteOfficeModal('delete-office' + row.pointId)}
							>
								<Trash2 size="16" />
							</button>
							<DeleteConfirmModal
								id={'delete-office' + row.pointId}
								message={`Xác nhận xóa <b>${row.name}</b>?`}
								confirmAction={() => deleteOffice(row.id)}
							/>
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
