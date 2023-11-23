<script lang="ts">
	import { TabGroup, Tab, TabAnchor } from '@skeletonlabs/skeleton';
	import { Mail , Landmark , Truck } from 'lucide-svelte';

	const services = [
		{
			name: 'Transport',
			icon: `<i class="fa-solid fa-truck-fast"></i>`
		},
		{
			name: 'Find sites',
			icon: `<i class="fa-solid fa-magnifying-glass-location"></i>`
		},
		{
			name: 'Tracking',
			icon: `<i class="fa-solid fa-map-location-dot"></i>`
		},
		{
			name: 'Invoices',
			icon: `<i class="fa-solid fa-receipt"></i>`
		},
		{
			name: 'Statistics',
			icon: `<i class="fa-solid fa-chart-line"></i>`
		},
		{
			name: 'Customer Services',
			icon: `<i class="fa-solid fa-headset"></i>`
		}
	];
	let tabSet: number = 0;

</script>

<main>
	<div class="home">
		<div class="slogan ">
			<h1 class="h1 text-center mb-8 text-secondary-400">
				 Tổ chức uy tín hàng đầu Việt Nam
			</h1>
			<h1 class="justify-between text-center mb-8 ">
				<Mail class="inline" size={80} />
				<Landmark class="inline ml-40" size={80} />
				<Truck class="inline ml-40" size={90} />
			</h1>

			<h1 class="h1 text-center mb-8 text-secondary-400">
				Gửi hàng đi mọi nơi với MagicPost
			</h1>
			
		</div>
		<div class="relative top-0 left-0">
			<div class="bg-color" />
			<img src="/img/Transportation.jpg" alt="bg" class="bg-pic" />
		</div>
	</div>

	<div class="services">
		<TabGroup justify="justify-center" flex="flex-1 lg:flex-none" class="h-max w-4/5 ">
			<Tab bind:group={tabSet} name="tab1" value={0} class="w-1/2 text-2xl">Theo dõi đơn hàng</Tab>
			<Tab bind:group={tabSet} name="tab2" value={1} class="w-1/2 text-2xl">Dịch vụ</Tab>
			<!-- Tab Panels --->
			<svelte:fragment slot="panel">
				{#if tabSet === 0}
					<div class="w-full p-3 bg-surface-200 rounded-md flex gap-5">
						<input type="text" placeholder="Mã đơn" class="dui-input dui-input-bordered dui-input-lg w-full"/>
						<button type="button" class="btn variant-filled-secondary rounded-md w-1/5">Theo dõi</button>
					</div>
				{:else if tabSet === 1}
					<div class="logo-cloud grid-cols-3 gap-2 w-full h-[60vh] [&>.logo-item]:bg-secondary-400">
						{#each services as service}
							<div class="logo-item text-2xl card-hover">
								<div>{@html service.icon}</div>
								<p>{service.name}</p>
							</div>
						{/each}
					</div>
				{/if}
			</svelte:fragment>
		</TabGroup>
	</div>
</main>

<style>
	main {
		overflow-x: hidden;
	}
	.home {
		padding-top: 20px;
		height: calc(80vh - 5rem);
		display: grid;
		grid-template-columns: 1.3fr 1fr;
		overflow: hidden;
	}

	.slogan {
		color: rgba(var(--color-surface-600) / 1);
		font-weight: 900;
		padding: 9rem 0 0 1.5rem;
	}


	.bg-pic {
		position: absolute;
		top: 15%;
		left: 30px;
		border-radius: 12px 0 0 12px;
	}

	.services {
		height: 100vh;
		display: flex;
		justify-content: center;
		padding-top: 100px;
		background-color: rgba(var(--color-surface-50) / 1) !important;
	}
</style>
