<script lang="ts">
	import { AppRail, AppRailTile, AppRailAnchor, TreeView, TreeViewItem } from '@skeletonlabs/skeleton';
	import { page } from '$app/stores';
	import { AlignJustify, AreaChart, Users ,Store  } from 'lucide-svelte';

	let expand: boolean = true;
</script>

<div class="wrapper"> 
	<AppRail width={expand ? "w-64" : 'w-20'} margin=""  aspectRatio="aspect-[4/1]" class="shadow-lg">
		<AppRailTile on:click={() => (expand = !expand)}  bind:group={expand} name="tile-1" active="" value={0} hover="hover:bg-secondary-500">
			<span class="flex pl-7 text-base gap-3" class:py-4={!expand} class:py-8={expand}>
				<AlignJustify /> <span class:hidden={!expand}>Menu quản lý</span>
			</span>
		</AppRailTile>

		<!-- --- -->
		<AppRailAnchor href="/admin/statistic" hover="hover:bg-secondary-500/90" active="bg-secondary-500" selected={$page.url.pathname === '/admin'}>
			<span class="pl-7 text-base flex gap-3" class:py-4={!expand}>
				<AreaChart /> <span class:hidden={!expand}>Thống kê</span>
			</span>
		</AppRailAnchor>
		<AppRailAnchor href="/admin/staffs" hover="hover:bg-secondary-500/90" active="bg-secondary-500" selected={$page.url.pathname === '/admin/staffs'}>
			<span class="pl-7 text-base flex gap-3" class:py-4={!expand}>
				<Users /> <span class:hidden={!expand}>Nhân viên</span>
			</span>
		</AppRailAnchor>
		<AppRailAnchor href="/admin/offices" hover="hover:bg-secondary-500/90" active="bg-secondary-500" selected={$page.url.pathname === '/admin/offices'}>
			<span class="pl-7 text-base flex gap-3" class:py-4={!expand}>
				<Store /> <span class:hidden={!expand}>Điểm chuyển phát</span>
			</span>
		</AppRailAnchor>
	</AppRail>

	<div class="p-6 flex-1 overflow-auto">
		<slot />
	</div>
</div>

<style>
	.wrapper {
		width: 100%;
		height: calc(100vh - 4rem);
		display: flex;
		flex: 1;
	}
</style>
