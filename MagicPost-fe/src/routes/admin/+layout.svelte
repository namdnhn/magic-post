<script lang="ts">
	import { AppRail, AppRailTile, AppRailAnchor, TreeView, TreeViewItem } from '@skeletonlabs/skeleton';
	import { page } from '$app/stores';
	import { AlignJustify, AreaChart, Users ,Store  } from 'lucide-svelte';

	let expand: boolean = true;
</script>

<div class="wrapper"> 
	<AppRail width="w-64" margin=""  aspectRatio="aspect-[4/1]" class="shadow-lg">
		<AppRailTile bind:group={expand} name="tile-1" active="" value={0} hover="hover:bg-secondary-500">
			<span class="flex justify-center text-base gap-3">
				<AlignJustify /> Menu Quản Lý
			</span>
		</AppRailTile>

		<!-- --- -->
		<AppRailAnchor href="/admin" hover="hover:bg-secondary-500/90" active="bg-secondary-500" selected={$page.url.pathname === '/admin'}>
			<span class="pl-5 text-base flex gap-3">
				<AreaChart /> Thống Kê
			</span>
		</AppRailAnchor>
		<AppRailAnchor href="/admin/staffs" hover="hover:bg-secondary-500/90" active="bg-secondary-500" selected={$page.url.pathname === '/admin/staffs'}>
			<span class="pl-5 text-base flex gap-3">
				<Users  /> Nhân Viên
			</span>
		</AppRailAnchor>
		<AppRailAnchor href="/admin/offices" hover="hover:bg-secondary-500/90" active="bg-secondary-500" selected={$page.url.pathname === '/admin/offices'}>
			<span class="pl-5 text-base flex gap-3">
				<Store  />Điểm Giao Dịch & Tập Kết
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
