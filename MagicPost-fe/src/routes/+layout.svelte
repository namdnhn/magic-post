<script lang="ts">
	import '../app.css';
	import { TabGroup, AppBar, TabAnchor } from '@skeletonlabs/skeleton';
	import { Newspaper, Truck, User2, MapPin, FileText, LogOut, UserCircle } from 'lucide-svelte';
	import type { PageData } from './$types';
	import { computePosition, autoUpdate, offset, shift, flip, arrow } from '@floating-ui/dom';
	import { Roles } from 'src/utils/interface';
	import { storePopup } from '@skeletonlabs/skeleton';
	import { initLazy } from '$lib/lazyLoad';

	initLazy();
	storePopup.set({ computePosition, autoUpdate, offset, shift, flip, arrow });
</script>

<header>
	<AppBar class="w-full p-3 pl-6 h-16 justify-center !bg-tertiary-200">
		<svelte:fragment slot="lead" />
		<TabAnchor href="/">
			<span class="brand">
				<img src="/img/logo-new.png" alt="logo" class="h-16 overflow-hidden" />
			</span>
		</TabAnchor>
		<svelte:fragment slot="trail">
			<TabGroup
				justify="justify-end"
				active="variant-filled-primary"
				hover="hover:variant-ghost-secondary"
				flex="flex-1 lg:flex-none"
				rounded="rounded-full"
				border="border-inherit"
				class="w-full"
			>
				<TabAnchor href="/" class="ml-3">
					<span class="link-nav flex"> Dịch vụ &nbsp;<Truck /> </span>
				</TabAnchor>
				<TabAnchor href="/" class="ml-3">
					<span class="link-nav flex"> Tin tức &nbsp;<Newspaper size={20} /> </span>
				</TabAnchor>
				<TabAnchor href="/tracking" class="ml-3">
					<span class="link-nav flex"> Theo dõi &nbsp;<MapPin size={20} /></span>
				</TabAnchor>
				<TabAnchor href="/login" class="ml-3">
					<span class="link-nav flex"> Đăng nhập &nbsp;<User2 size={20} /></span>
				</TabAnchor>
			</TabGroup>
		</svelte:fragment>
	</AppBar>
</header>

<div>
	<slot />
</div>

<style>
	.brand {
		font-size: 32px;
	}
	.link-nav {
		font-size: 16px;
	}
</style>
