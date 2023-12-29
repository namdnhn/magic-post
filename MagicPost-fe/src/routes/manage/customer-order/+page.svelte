<script lang="ts">
	import { PlusCircle } from 'lucide-svelte';
	import { goto } from '$app/navigation';
	import type { Order } from 'src/utils/interface';

	import ListOrder from 'src/components/ListOrder.svelte';

	let orderData: Order[] = 
		[
			{
			orderId: 2089,
			mainCharge: "90.000",
			category:"Hàng hóa",
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
			orderId: 2088,
			mainCharge: "90.000",
			category:"Hàng hóa",
			orderDelivery: {
			id: 123,
			fromLocation: {
				id: "id",
				customerId: 123,
				name: "name",
				phoneNo: "0123456",
				address: "address",
			},

			toLocation: {
				id: "id",
				customerId: 123,
				name: "name",
				phoneNo: "0123456",
				address: "address",
			},
		},
		createAt: "HN",
	},
	{
			orderId: 2087,
			mainCharge: "90.000",
			category:"Tài liệu",
			orderDelivery: {
			id: 123,
			fromLocation: {
				id: "id",
				customerId: 123,
				name: "name",
				phoneNo: "0123456",
				address: "address",
			},
			toLocation: {
				id: "id",
				customerId: 123,
				name: "name",
				phoneNo: "0123456",
				address: "address",
			},
		},
		createAt: "HN",
	},
	{
			orderId: 2087,
			mainCharge: "90.000",
			category:"Tài liệu",
			orderDelivery: {
			id: 123,
			fromLocation: {
				id: "id",
				customerId: 123,
				name: "name",
				phoneNo: "0123456",
				address: "address",
			},
			toLocation: {
				id: "id",
				customerId: 123,
				name: "name",
				phoneNo: "0123456",
				address: "address",
			},
		},
		createAt: "HN",
	},
	{
			orderId: 2087,
			mainCharge: "90.000",
			category:"Tài liệu",
			orderDelivery: {
			id: 123,
			fromLocation: {
				id: "id",
				customerId: 123,
				name: "name",
				phoneNo: "0123456",
				address: "address",
			},
			toLocation: {
				id: "id",
				customerId: 123,
				name: "name",
				phoneNo: "0123456",
				address: "address",
			},
		},
		createAt: "HN",
	},
	{
			orderId: 2087,
			mainCharge: "90.000",
			category:"Tài liệu",
			orderDelivery: {
			id: 123,
			fromLocation: {
				id: "id",
				customerId: 123,
				name: "name",
				phoneNo: "0123456",
				address: "address",
			},
			toLocation: {
				id: "id",
				customerId: 123,
				name: "name",
				phoneNo: "0123456",
				address: "address",
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