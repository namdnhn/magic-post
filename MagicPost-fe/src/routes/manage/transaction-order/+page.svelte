<script lang="ts">
	import { TabGroup, Tab } from '@skeletonlabs/skeleton';
	import TransactionOrderTable from 'src/components/table/TransactionOrderTable.svelte';
	import type { OrderTransaction } from 'src/utils/interface';

	let tabSet: 'coming' | 'processing' | 'forward' = 'coming';


	let orderData1: OrderTransaction[] = 
		[{
			category:"Hàng hóa",
			orderId: 2089,
			mainCharge: "30.000",
			date: "18/09/2023",
			gatherPoint: "ĐTK Cầu Giấy"
	},
	{
			orderId: 2087,
			mainCharge: "31.000",
			date: "22/06/2023",
			category:"Tài liệu",
			gatherPoint: "ĐTK Đống Đa"
	}
	,
	{
			orderId: 2086,
			mainCharge: "20.000",
			date: "06/06/2023",
			category:"Tài liệu",
			gatherPoint: "ĐTK Hoàn Kiếm"
	}
	,
	{
			orderId: 2085,
			mainCharge: "30.000",
			date: "02/06/2023",
			category:"Tài liệu",
			gatherPoint: "ĐTK Long Biên"
	}
	,
	{
			orderId: 2084,
			mainCharge: "15.000",
			date: "16/05/2023",
			category:"Hàng hóa",
			gatherPoint: "ĐTK Xuân Thủy"
	}
]
let orderData2: OrderTransaction[] = 
		[{
			category:"Hàng hóa",
			orderId: 2089,
			mainCharge: "30.000",
			date: "18/09/2023",
			gatherPoint: "ĐTK Cầu Giấy"
	},
	{
			orderId: 2087,
			mainCharge: "31.000",
			date: "22/06/2023",
			category:"Tài liệu",
			gatherPoint: "ĐTK Đống Đa"
	}
	,
	{
			orderId: 2086,
			mainCharge: "20.000",
			date: "06/06/2023",
			category:"Tài liệu",
			gatherPoint: "ĐTK Hoàn Kiếm"
	}
	,
	{
			orderId: 2085,
			mainCharge: "30.000",
			date: "02/06/2023",
			category:"Tài liệu",
			gatherPoint: "ĐTK Long Biên"
	}
	,
	{
			orderId: 2084,
			mainCharge: "15.000",
			date: "16/05/2023",
			category:"Hàng hóa",
			gatherPoint: "ĐTK Xuân Thủy"
	},
	{
			orderId: 9405,
			mainCharge: "31.000",
			date: "22/06/2023",
			category:"Tài liệu",
			gatherPoint: "ĐTK Đống Đa"
	}
	,
	{
			orderId: 7198,
			mainCharge: "31.000",
			date: "06/06/2023",
			category:"Tài liệu",
			gatherPoint: "ĐTK Hoàn Kiếm"
	}
	,
	{
			orderId: 1782,
			mainCharge: "31.000",
			date: "02/06/2023",
			category:"Tài liệu",
			gatherPoint: "ĐTK Long Biên"
	}
]

</script>

<main class="h-full">
	<h3 class="h3 uppercase mb-3">Danh sách đơn giao dịch </h3>
	<div class="logo-cloud grid-cols-2 gap-12 w-full h-[12vh] [&>.logo-item]:bg-secondary-400 items-center text-center [&>.logo-item]:text-secondary-50">
		<div class="logo-item text-2xl card-hover text-center">
			<p>Số hàng gửi: 8</p>
		</div>
		<div class="logo-item text-2xl card-hover">
			<div>Số hàng nhận: 5</div>
		</div>	
	</div>
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
					<TransactionOrderTable tableData={orderData1} tooltip={"điểm tập kết"}  />
				{:else if tabSet == 'forward'}
					<TransactionOrderTable tableData={orderData2} tooltip={"khách hàng"} />
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
