<script lang="ts">
	import { TabGroup, Tab } from '@skeletonlabs/skeleton';
	import GatherOrdersTable from 'src/components/table/GatherOrdersTable.svelte';

	let tabSet: 'coming' | 'processing' | 'forward' = 'coming';
</script>

<main class="h-full">
	<h3 class="h3 uppercase mb-3">Danh sách đơn tập kêt - Điểm giao dịch XYZ</h3>

	<TabGroup rounded="rounded-tl-md rounded-tr-md" class="h-[calc(100%-6rem)]">
		<Tab bind:group={tabSet} name="tab1" value="coming" class="w-1/3">
			<span class:text-surface-400={tabSet != 'coming'}>Đơn đến</span>
		</Tab>
		<Tab bind:group={tabSet} name="tab2" value="processing" class="w-1/3">
			<span class:text-surface-400={tabSet != 'processing'}>Đơn đang xử lý</span>
		</Tab>
		<Tab bind:group={tabSet} name="tab3" value="forward" class="w-1/3">
			<span class:text-surface-400={tabSet != 'forward'}>Đơn đi</span>
		</Tab>
		<!-- Tab Panels --->
		<svelte:fragment slot="panel">
			<div class="card !rounded-b-none h-full">
				{#if tabSet == 'coming'}
					<GatherOrdersTable tableData={[]} />
				{:else if tabSet == 'processing'}
					(tab panel 2 contents)
				{:else if tabSet == 'forward'}
					(tab panel 3 contents)
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
