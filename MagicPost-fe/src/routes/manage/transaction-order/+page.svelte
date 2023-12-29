<script lang="ts">
	import { TabGroup, Tab } from '@skeletonlabs/skeleton';
	import TransactionOrderTable from 'src/components/table/TransactionOrderTable.svelte';
	import type { Order } from 'src/utils/interface';

	let tabSet: 'coming' | 'processing' | 'forward' = 'coming';
	let tab3: boolean = false;

	let orderData: Order[] = 
		[{
			category:"Hàng hóa",
			orderId: 123,
			mainCharge: "123",
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
			orderId: 123,
			mainCharge: "123",
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
	}
]

</script>

<main class="h-full">
	<h3 class="h3 uppercase mb-3">Danh sách đơn giao dịch </h3>
    <div class="card py-3 px-4 mb-3">
		<span class="mr-2">Tìm kiếm</span>
		<input type="text" placeholder="Nhập tên, mã đơn hàng..." class="dui-input dui-input-bordered w-full max-w-xs" />
	</div>

	<TabGroup rounded="rounded-tl-md rounded-tr-md" class="h-[calc(100%-6rem)]" >
		<Tab bind:group={tabSet} name="tab1" value="coming" class="w-1/2">
			<span class:text-surface-400={tabSet != 'coming'}>Đơn đến</span>
		</Tab>
		<Tab bind:group={tabSet} name="tab3" value="forward" class="w-1/2" >
			<span class:text-surface-400={tabSet != 'forward'}>Đơn đi</span>
		</Tab>
		<!-- Tab Panels --->
		<svelte:fragment slot="panel">
			<div class="card !rounded-b-none h-full">
				{#if tabSet == 'coming'}
					<TransactionOrderTable tableData={orderData}  />
				{:else if tabSet == 'forward'}
					<TransactionOrderTable tableData={orderData}  />
				{/if}
			</div>
		</svelte:fragment>
	</TabGroup>
</main>

<style>
	:global(.tab-panel) {
		height: 100%;
	}
</style>
