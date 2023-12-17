<script lang="ts">
	import { PlusCircle } from "lucide-svelte";
	import StaffsTable from "src/components/table/StaffsTable.svelte";
	import { Roles, type StaffsInteface } from "src/utils/interface";

    const tableData: StaffsInteface[] = [
        {
            id: "",
            userId: "12345",
            address: "",
            email: "",
            fullName: "Nguyen Van A",
            phoneNo: "",
            dateOfBirth: "",
            role: {
                id: Roles.GATHERS_STAFF,
                name: "Nhân viên điểm tập kết",
            },
            workAt: {
                id: "",
                pointId: "",
                name: "Điểm tập kết 1",
            },
        },
        {
            id: "",
            userId: "23456",
            address: "",
            email: "",
            fullName: "Nguyen Van B",
            phoneNo: "",
            dateOfBirth: "",
            role: {
                id: Roles.TRANSACTION_STAFF,
                name: "Nhân viên điểm giao dịch",
            },
            workAt: {
                id: "",
                pointId: "",
                name: "Điểm giao dịch 1",
            },
        },
    ]
</script>

<main class="h-full">
	<div class="flex justify-between items-center mb-3">
		<h1 class="h3 uppercase">Danh sách tài khoản nhân viên</h1>
		<button class="btn variant-filled bg-ocean">
			<PlusCircle class="mr-1" size="20" /> Thêm mới
		</button>
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
		<!-- {#await data.staffs.promise}
			<Loading message="Đang lấy dữ liệu mới nhất" />
		{:then staffs}
			<StaffsTable tableData={staffs.data.content} />
		{:catch err}
			<p>Error :(</p>
		{/await} -->
        <StaffsTable tableData={tableData} />
	</div>
</main>