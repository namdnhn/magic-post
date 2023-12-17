<script lang="ts">
	import { PencilLine, Trash2 } from 'lucide-svelte';
	import type { StaffsInteface } from 'src/utils/interface';
	import EmptyData from '../EmptyData.svelte';
	import StaffsModal from '../modal/StaffsModal.svelte';
	import DeleteConfirmModal from '../modal/DeleteConfirmModal.svelte';
	import { invalidate } from '$app/navigation';

	export let tableData: StaffsInteface[] = [];

	function openEditStaffModal(id: string) {
		(document.getElementById(id) as any).showModal();
	}

	function openDeleteStaffModal(id: string) {
		(document.getElementById(id) as any).showModal();
	}

	async function deleteStaff(deleteId: string) {
		const response = await fetch(`/api/admin/staffs/${deleteId}`, {
			method: 'DELETE'
		});

		if (response.status == 200) {
			invalidate((url) => url.pathname.includes('/api/admin/staffs'));
		}
	}
</script>

<div class="table-container !rounded-b-none !rounded-md h-full">
	<table class="table table-hover overflow-auto !bg-transparent !rounded-none" class:h-full={tableData.length == 0}>
		<thead class="!bg-white">
			<tr>
				<th>STT</th>
				<th>Mã nhân viên</th>
				<th>Họ tên</th>
				<th>Chức vụ</th>
				<th>Điểm quản lý</th>
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
						<td>{row.userId}</td>
						<td>{row.fullName}</td>
						<td>{row.role.name}</td>
						<td>{row.workAt ? row.workAt.name : 'Chưa có'}</td>
						<td class="flex items-center gap-3">
							<div class="dui-tooltip dui-tooltip-bottom " data-tip="Chỉnh sửa">
								<button
									type="button"
									class="btn-icon variant-filled-secondary h-8 w-8"
									on:click={() => openEditStaffModal('edit-staff-' + row.userId)}
								>
									<PencilLine size="16" />
								</button>
								<StaffsModal id={'edit-staff-' + row.userId} staff={row} />
							</div>

							<div class="dui-tooltip dui-tooltip-bottom " data-tip="Xóa">
								<button
								type="button"
								class="btn-icon variant-filled-error h-8 w-8"
								on:click={() => {
									openDeleteStaffModal('delete-staff-' + row.userId);
								}}
							>
								<Trash2 size="16" />
							</button>
							<DeleteConfirmModal
								id={'delete-staff-' + row.userId}
								message={`Xóa <b>${row.fullName}</b>?`}
								confirmAction={() => deleteStaff(row.id)}
							/>
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

</style>
