<script lang="ts">
	import { TabGroup, Tab } from '@skeletonlabs/skeleton';
	import GatherOrdersTable from 'src/components/table/GatherOrdersTable.svelte';
	import type { Order } from 'src/utils/interface';

	let tabSet: 'coming' | 'processing' | 'forward' = 'coming';
	let tab3: boolean = false;

	let orderData1: Order[] = 
		[{
			category:"Hàng hóa",
			orderId: 2089,
			mainCharge: "90.000",
			date: "18/09/2023",
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
			mainCharge: "100.000",
			date: "22/06/2023",
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
	,
	{
			orderId: 2086,
			mainCharge: "100.000",
			date: "06/06/2023",
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
	,
	{
			orderId: 2085,
			mainCharge: "100.000",
			date: "02/06/2023",
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
	,
	{
			orderId: 2084,
			mainCharge: "100.000",
			date: "16/05/2023",
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
let orderData2: Order[] = 
		[{
			category:"Hàng hóa",
			orderId: 2089,
			mainCharge: "90.000",
			date: "18/09/2023",
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
			category:"Hàng hóa",
			orderId: 7198,
			mainCharge: "80.000",
			date: "05/08/2023",
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
			orderId: 1782,
			mainCharge: "90.000",
			category:"Tài liệu",
			date: "01/07/2023",
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
	}	,
	{
			orderId: 3716,
			mainCharge: "100.000",
			date: "02/06/2023",
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
	,
	{
			orderId: 6250,
			mainCharge: "100.000",
			date: "16/05/2023",
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
	,
			{
			category:"Hàng hóa",
			orderId: 7198,
			mainCharge: "80.000",
			date: "05/08/2023",
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
			orderId: 1782,
			mainCharge: "90.000",
			category:"Tài liệu",
			date: "09/04/2023",
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
	,
	{
			orderId: 1782,
			mainCharge: "90.000",
			category:"Tài liệu",
			date: "19/03/2023",
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
	,
	{
			orderId: 1782,
			mainCharge: "90.000",
			category:"Tài liệu",
			date: "07/01/2023",
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
let orderData3: Order[] = 
		[{
			category:"Hàng hóa",
			orderId: 2089,
			mainCharge: "90.000",
			date: "18/09/2023",
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
			category:"Hàng hóa",
			orderId: 689,
			mainCharge: "150.000",
			date: "18/09/2023",
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
			orderId: 397,
			mainCharge: "200.000",
			category:"Hàng hóa",
			date: "11/10/2023",
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
	let len1 : number;
	$: len1 = orderData1.length;

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
	<div class="logo-cloud grid-cols-2 gap-12 w-full h-[12vh] [&>.logo-item]:bg-secondary-400 items-center text-center [&>.logo-item]:text-secondary-50">
		<div class="logo-item text-2xl card-hover text-center">
			<p>Số đơn đến: 5</p>
		</div>
		<div class="logo-item text-2xl card-hover">
			<div>Số đơn đi: 3</div>
		</div>
		<!-- <div class="logo-item text-2xl card-hover ">
			<div>oke</div>
		</div> 	 -->
	</div>
	<!-- <div class="dui-divider m-0" /> -->
    <div class="card py-3 px-4 mb-3">
		<span class="mr-2">Tìm kiếm</span>
		<input type="text" placeholder="Nhập tên, mã đơn hàng..." class="dui-input dui-input-bordered w-full max-w-xs" />
	</div>


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
					<GatherOrdersTable tableData={orderData1} tab3={tab3} />
				{:else if tabSet == 'processing'}
				<GatherOrdersTable tableData={orderData2} tab3={tab3}/>
				{:else if tabSet == 'forward'}
				<GatherOrdersTable tableData={orderData3} tab3={tab3} />

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
