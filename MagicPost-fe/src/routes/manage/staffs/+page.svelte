<script lang="ts">
	import { PlusCircle } from "lucide-svelte";
    import Loading from 'src/components/Loading.svelte';
	import StaffsTable from "src/components/table/StaffsTable.svelte";
	import { Roles, type StaffsInteface } from "src/utils/interface";
    import StaffsModal from 'src/components/modal/StaffsModal.svelte';
    import type { PageData } from './$types';
	import { onMount } from "svelte";

    const tableData: StaffsInteface[] = [
        {
            id: "",
            userId: "26",
            address: "",
            email: "",
            fullName: "Nguyễn Cao Đức",
            phoneNo: "",
            dateOfBirth: "",
            role: {
                id: Roles.GATHERS_STAFF,
                name: "Nhân viên điểm giao dịch",
            },
            workAt: {
                id: "",
                pointId: "",
                name: "ĐGD Xuân Thủy",
            },
        },
        {
            id: "",
            userId: "27",
            address: "",
            email: "",
            fullName: "Dương Hoàng Hải",
            phoneNo: "",
            dateOfBirth: "",
            role: {
                id: Roles.GATHERS_STAFF,
                name: "Nhân viên điểm giao dịch",
            },
            workAt: {
                id: "",
                pointId: "",
                name: "ĐGD Xuân Thủy",
            },
        },
    ]
    export let data: PageData;

    onMount(() => {
        console.log(data.streamed?.staffs);
    })
	function showStaffModal() {
		(document.getElementById('manager_new_staff') as any).showModal();
	}
</script>

<main class="h-full">
	<div class="flex justify-between items-center mb-3">
		<h1 class="h3 uppercase">Danh sách tài khoản nhân viên</h1>
		<button class="btn variant-filled bg-ocean" on:click={showStaffModal}>
			<PlusCircle class="mr-1" size="20" /> Thêm mới
		</button>
		<StaffsModal id="manager_new_staff" title="nhân viên" />
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
		{#await data.streamed?.staffs}
			<Loading message="Đang lấy dữ liệu mới nhất" />
		{:then staffs}
			<StaffsTable tableData={tableData}  />
		{:catch err}
			<p>Error : {err}</p>
		{/await}
	</div>
</main>