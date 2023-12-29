<script lang="ts">
	import { PlusCircle } from 'lucide-svelte';
	import { goto } from '$app/navigation';
	import type { Order } from 'src/utils/interface';

	import ListOrder from 'src/components/ListOrder.svelte';

	let orderData: Order[] = 
		[
			{
			orderId: 2009,
			mainCharge: "30.000",
			category:"Hàng hóa",
			date: "18/09/2023",
			orderDelivery: {
			id: 123,
			fromLocation: {
				id: "id",
				customerId: 123,
				name: "Đỗ Nhữ Hoàng Nam",
				phoneNo: "0987654321",
				address: "144 Xuân Thủy, Cầu Giấy, Hà Nội",
			},
			toLocation: {
				id: "id",
				customerId: 123,
				name: "Đặng Minh Khôi",
				phoneNo: "01234567890",
				address: "1 Đặng Tiến Đông",
			},
		},
		createAt: "HN",
	},
	{
			orderId: 2008,
			mainCharge: "31.000",
			category:"Hàng hóa",
			date: "18/09/2023",
			orderDelivery: {
			id: 123,
			fromLocation: {
				id: "id",
				customerId: 123,
				name: "Nguyễn Thị Hương",
				phoneNo: "0934567890",
				address: "Số 11/1137 đường Láng",
			},

			toLocation: {
				id: "id",
				customerId: 123,
				name: "Trần Văn Tú",
				phoneNo: "0923456789",
				address: "Số 35, Đường Trần Hưng Đạo, Quận 1, TP. Hồ Chí Minh",
			},
		},
		createAt: "HN",
	},
	{
			orderId: 2007,
			mainCharge: "30.000",
			category:"Tài liệu",
			date: "18/09/2023",
			orderDelivery: {
			id: 123,
			fromLocation: {
				id: "id",
				customerId: 123,
				name: "Lê Thị Lan Anh",
				phoneNo: "0998765432",
				address: "Số 18, Đường Nguyễn Văn Cừ, Quận Hoàn Kiếm, Hà Nội",
			},
			toLocation: {
				id: "id",
				customerId: 123,
				name: "Phạm Minh Tuấn",
				phoneNo: "0912345678",
				address: "Số 22, Đường Lê Lợi, Quận Hải Châu, Đà Nẵng",
			},
		},
		createAt: "HN",
	},
	{
			orderId: 2006,
			mainCharge: "30.000",
			category:"Tài liệu",
			date: "18/09/2023",
			orderDelivery: {
			id: 123,
			fromLocation: {
				id: "id",
				customerId: 123,
				name: "Võ Thanh Trúc",
				phoneNo: "0909876543",
				address: "Số 7, Đường Nguyễn Huệ, Quận 1, TP. Hồ Chí Minh",
			},
			toLocation: {
				id: "id",
				customerId: 123,
				name: "Trần Thanh Hằng",
				phoneNo: "0909876543",
				address: "Số 12, Đường Hai Bà Trưng, Quận Hoàn Kiếm, Hà Nội",
			},
		},
		createAt: "HN",
	},
	{
			orderId: 2005,
			mainCharge: "27.000",
			category:"Tài liệu",
			date: "18/09/2023",
			orderDelivery: {
			id: 123,
			fromLocation: {
				id: "id",
				customerId: 123,
				name: "Nguyễn Hữu Minh",
				phoneNo: "0998765432",
				address: "Số 5, Đường Điện Biên Phủ, Quận Bình Thạnh, TP. Hồ Chí Minh",
			},
			toLocation: {
				id: "id",
				customerId: 123,
				name: "Lê Văn Hoàng",
				phoneNo: "0976543210",
				address: "Số 15, Đường Lê Duẩn, Quận Thanh Khê, Đà Nẵng",
			},
		},
		createAt: "HN",
	},
	{
			orderId: 2004,
			mainCharge: "27.000",
			category:"Tài liệu",
			date: "18/09/2023",
			orderDelivery: {
			id: 123,
			fromLocation: {
				id: "id",
				customerId: 123,
				name: "Trần Thị Mai",
				phoneNo: "0923456789",
				address: "Số 9, Đường Trần Phú, Quận Hải Châu, Đà Nẵng",
			},
			toLocation: {
				id: "id",
				customerId: 123,
				name: "	Nguyễn Văn Long",
				phoneNo: "0909876543",
				address: "Số 20, Đường Nguyễn Thị Minh Khai, Quận 3, TP. Hồ Chí Minh",
			},
		},
		createAt: "HN",
	}
	
]
	
</script>

<main>
	<div class="flex justify-between">
		<h1 class="h3 uppercase">Đơn đặt hàng từ khách hàng</h1>
		<div class="flex items-end gap-3">
			<input type="text" name="sender" placeholder="Tìm mã đơn hàng" class="dui-input dui-input-bordered w-full" />
			<button
				on:click={() => goto('/manage/customer-order/add')}
		
				class="btn variant-filled bg-ocean py-2"
			>
				<PlusCircle class="mr-1" size="20" /> Thêm mới
			</button>
		</div>
	</div>
	<div class="dui-divider mt-3" />
	<div class="h-[calc(100%-7rem)] card !rounded-none overflow-auto !bg-transparent">
		{#each orderData as orderDataSample}
			<ListOrder orderData={orderDataSample} />			
		{/each}
	</div>
	
</main>

<style>    
</style>