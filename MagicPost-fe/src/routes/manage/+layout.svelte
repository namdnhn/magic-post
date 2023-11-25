<script lang="ts">
	import { AppRail, AppRailTile, AppRailAnchor, TreeView, TreeViewItem } from '@skeletonlabs/skeleton';
	import { page } from '$app/stores';
	import { AlignJustify,MenuSquare, Users, Package, Boxes, Dot, ScrollText, Navigation } from 'lucide-svelte';

	let expand: boolean = true;
	let isOpenTransport = ['/manage/delivery', '/manage/transport'].includes($page.url.pathname);
	let isOpenCustomerOrder = ['/manage/customer-order', '/manage/customer-order/add'].includes($page.url.pathname);
	let open: any;
</script>

<div class="wrapper"> 
	<AppRail width="w-56"  aspectRatio="aspect-[4/1]" class="shadow-lg">
		<AppRailTile bind:group={expand} name="tile-1" active="" value={0} hover="hover:bg-secondary-500">
			<span class="flex justify-center text-base gap-3">
				<AlignJustify /> Menu quản lý
			</span>
		</AppRailTile>

		<!-- --- -->
		<AppRailAnchor href="/manage/staffs" hover="hover:bg-secondary-500/90" active="bg-secondary-500" selected={$page.url.pathname === '/manage/staffs'}>
			<span class="pl-5 text-base flex gap-3">
				<Users /> Nhân viên
			</span>
		</AppRailAnchor>
		<AppRailAnchor href="/manage/customer-order" hover="hover:bg-secondary-500/90" active="bg-secondary-500" selected={isOpenCustomerOrder}>
			<span class="pl-5 text-base flex gap-3">
				<Package />Đơn đặt hàng
			</span>
		</AppRailAnchor>
		<AppRailAnchor href="/manage/transaction-order" hover="hover:bg-secondary-500/90" active="bg-secondary-500" selected={$page.url.pathname === '/manage/transaction-order'}>
			<span class="pl-5 text-base flex gap-3">
				<ScrollText />Đơn giao dịch
			</span>
		</AppRailAnchor>
		<AppRailAnchor href="/manage/gathering-order" hover="hover:bg-secondary-500/90" active="bg-secondary-500" selected={$page.url.pathname === '/manage/gathering-order'}>
			<span class="pl-5 text-base flex gap-3">
				<Boxes />Đơn tập kết
			</span>
		</AppRailAnchor>
		<TreeView
			rounded="rounded-none"
			open={isOpenTransport}
			indent=""
			regionSummary="flex-row-reverse gap-4"
			hover="hover:bg-secondary-500/90"
		>
			<TreeViewItem bind:open spacing="" >
				<span class="text-base font-bold flex gap-4">
					<Navigation />
					Đơn vận chuyển
				</span>
				<svelte:fragment slot="children">
					<AppRailAnchor href="/manage/delivery" active="bg-secondary-500"  selected={$page.url.pathname === '/manage/delivery'}>
						<TreeViewItem hover="" class="text-base" regionSummary="">
							<svelte:fragment slot="lead"><Dot /></svelte:fragment>
							<p class="-m-3">Tới khách hàng</p>
						</TreeViewItem>
					</AppRailAnchor>
					<AppRailAnchor href="/manage/transport" active="bg-secondary-500" selected={$page.url.pathname === '/manage/transport'}>
						<TreeViewItem hover="" class="text-base" regionSummary="">
							<svelte:fragment slot="lead"><Dot /></svelte:fragment>
							<p class="-m-3">Tới điểm tập kết</p>
						</TreeViewItem>
					</AppRailAnchor>
				</svelte:fragment>
			</TreeViewItem>
		</TreeView>
	</AppRail>

	<div class="p-6 flex-1 overflow-auto">
		<slot />
	</div>
</div>

<style>

</style>
