<script lang="ts">
	import { TabGroup, Tab } from '@skeletonlabs/skeleton';
	import GatherOrdersTable from 'src/components/table/GatherOrdersTable.svelte';
	import type { Order } from 'src/utils/interface';

	let tabSet: 'coming' | 'processing' | 'forward' = 'coming';
	let tab3: boolean = false;

	let orderData: Order[] = 
		[{
			orderId: 123,
			mainCharge: 123,
			orderDelivery: {
			id: 123,
			fromLocation: {
				id: "id",
				customerId: 123,
				name: "name",
				phoneNo: "0123456",
				address: "address",
				// transactionPoint: OfficesInterface,
			},
			// currentLocation: OfficesInterface,
			toLocation: {
				id: "id",
				customerId: 123,
				name: "name",
				phoneNo: "0123456",
				address: "address",
				// transactionPoint: OfficesInterface,
			},
			// status: OrderStatus,
		},
		createAt: "HN",
	},
	{
			orderId: 123,
			mainCharge: 123,
			orderDelivery: {
			id: 123,
			fromLocation: {
				id: "id",
				customerId: 123,
				name: "name",
				phoneNo: "0123456",
				address: "address",
				// transactionPoint: OfficesInterface,
			},
			// currentLocation: OfficesInterface,
			toLocation: {
				id: "id",
				customerId: 123,
				name: "name",
				phoneNo: "0123456",
				address: "address",
				// transactionPoint: OfficesInterface,
			},
			// status: OrderStatus,
		},
		createAt: "HN",
	}
]

	function handleTabChange(tabName: string) {
		if (tabName === 'tab3') {
		tab3 = true;
		} else {
		tab3 = false;
		}
	}
</script>

<main class="h-full">
	<h3 class="h3 uppercase mb-3">Danh sách đơn tập kết </h3>

	<TabGroup rounded="rounded-tl-md rounded-tr-md" class="h-[calc(100%-6rem)]" on:change={() => handleTabChange('tab1')}>
		<Tab bind:group={tabSet} name="tab1" value="coming" class="w-1/3">
			<span class:text-surface-400={tabSet != 'coming'}>Đơn đến</span>
		</Tab>
		<Tab bind:group={tabSet} name="tab2" value="processing" class="w-1/3" on:change={() => handleTabChange('tab2')}>
			<span class:text-surface-400={tabSet != 'processing'}>Đơn ở kho</span>
		</Tab>
		<Tab bind:group={tabSet} name="tab3" value="forward" class="w-1/3" on:change={() => handleTabChange('tab3')}>
			<span class:text-surface-400={tabSet != 'forward'}>Đơn đi</span>
		</Tab>
		<!-- Tab Panels --->
		<svelte:fragment slot="panel">
			<div class="card !rounded-b-none h-full">
				{#if tabSet == 'coming'}
					<GatherOrdersTable tableData={orderData} tab3={tab3} />
				{:else if tabSet == 'processing'}
				<GatherOrdersTable tableData={orderData} tab3={tab3} />
				{:else if tabSet == 'forward'}
				<GatherOrdersTable tableData={orderData} tab3={tab3} />

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
