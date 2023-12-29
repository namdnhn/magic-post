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

	export let data: PageData;
	$: data.role ;

	let manageRoute: string;
	$: manageRoute = data.role == Roles.ADMIN ? '/admin' : '/manage';
	$: manageRoute = Roles.ADMIN ;

	let roleName: string;
	$: if(manageRoute == Roles.ADMIN ){
		roleName = "Admin"
	}
	else{
		roleName = "Nguyen Van A"
	}
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
			{#if !data.accessToken}
				<TabAnchor href={manageRoute} class="ml-3">
					<span class="link-nav flex"> Quản lý &nbsp;<FileText size={20} /></span>
				</TabAnchor>
				<TabAnchor href="/" class="ml-3 !p-0">
					<div class="dui-dropdown dui-dropdown-hover dui-dropdown-bottom dui-dropdown-end">
						<div tabindex="0" role="button">
							<span class="link-nav flex py-2 px-4"> {roleName} &nbsp;<User2 size={20} /></span>
						</div>

					</div>
				</TabAnchor>
				<TabAnchor href="/logout" data-sveltekit-reload class="ml-3">
					<span class="link-nav flex"> Đăng xuất &nbsp;<LogOut size={20} />  </span>
				</TabAnchor>
			{:else}
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
			{/if}
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
