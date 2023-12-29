<script lang="ts">
	import { TabGroup, Tab, TabAnchor } from '@skeletonlabs/skeleton';
	import { Mail , Landmark , Truck } from 'lucide-svelte';
	import { goto } from '$app/navigation';
	
	const services = [
		{
			name: 'Vận Chuyển',
			icon: `<i class="fa-solid fa-truck-fast"></i>`
		},
		{
			name: 'Tìm văn phòng',
			icon: `<i class="fa-solid fa-magnifying-glass-location"></i>`
		},
		{
			name: 'Theo dõi',
			icon: `<i class="fa-solid fa-map-location-dot"></i>`
		},
		{
			name: 'Phiếu đơn hàng',
			icon: `<i class="fa-solid fa-receipt"></i>`
		},
		{
			name: 'Thống kê',
			icon: `<i class="fa-solid fa-chart-line"></i>`
		},
		{
			name: 'Chăm sóc khách hàng',
			icon: `<i class="fa-solid fa-headset"></i>`
		}
	];
	let tabSet: number = 0;
	let trackingOrder: string;
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

	<div class="services m">
		<TabGroup justify="justify-center" flex="flex-1 lg:flex-none" class="h-max w-4/5 ">
			<Tab bind:group={tabSet} name="tab1" value={0} class="w-1/3 text-2xl">Theo dõi đơn hàng</Tab>
			<Tab bind:group={tabSet} name="tab2" value={1} class="w-1/3 text-2xl">Dịch vụ</Tab>
			<Tab bind:group={tabSet} name="tab3" value={2} class="w-1/3 text-2xl">Tra cứu bưu cục</Tab>
			<!-- Tab Panels --->
			<svelte:fragment slot="panel">
				{#if tabSet === 0}
					<div class="w-full p-3 bg-surface-200 rounded-md flex gap-5">
						<input type="text" placeholder="Mã đơn" 
						class="dui-input dui-input-bordered dui-input-lg w-full"
						bind:value={trackingOrder}
						/>
						<button type="button" 
						class="btn variant-filled-secondary rounded-md w-1/5"
						on:click={() => goto(`/tracking/${trackingOrder}`)}
						>Theo dõi</button>
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
				{:else if tabSet === 2}
					<div>
						
					</div>
				{/if}
			</svelte:fragment>
		</TabGroup>
	</div>

	<div class="border-t-8 border-tertiary-500 bg-tertiary-50">
		<footer class="">
			<div class="mx-auto w-full max-w-screen-xl p-4 py-6 lg:py-8">
				<div class="md:flex md:justify-between">
				  <div class="mb-6 md:mb-0">
					  <a href="/" class="flex items-center">
						  <img src="/img/logo-new.png" class="h-16" alt="MagicPost Logo" />
						  <span class="self-center text-3xl font-semibold whitespace-nowrap dark:text-white pb-5">MagicPost</span>
					  </a>
				  </div>
				  <div class="grid grid-cols-2 gap-8 sm:gap-6 sm:grid-cols-3">
					  <div>
						  <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Resources</h2>
						  <ul class="text-gray-500 dark:text-gray-400 font-medium">
							  <li class="mb-4">
								  <a href="/" class="hover:underline">MagicPost</a>
							  </li>
							  <li>
								  <a href="https://tailwindcss.com/" class="hover:underline">Tailwind CSS</a>
							  </li>
						  </ul>
					  </div>
					  <div>
						  <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Follow us</h2>
						  <ul class="text-gray-500 dark:text-gray-400 font-medium">
							  <li class="mb-4">
								  <a href="https://github.com/namdnhn/magic-post" class="hover:underline ">Github</a>
							  </li>
							  <li>
								  <a href="https://discord.com" class="hover:underline">Discord</a>
							  </li>
						  </ul>
					  </div>
					  <div>
						  <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Legal</h2>
						  <ul class="text-gray-500 dark:text-gray-400 font-medium">
							  <li class="mb-4">
								  <a href="/" class="hover:underline">Privacy Policy</a>
							  </li>
							  <li>
								  <a href="/" class="hover:underline">Terms &amp; Conditions</a>
							  </li>
						  </ul>
					  </div>
				  </div>
			  </div>
			  <hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
			  <div class="sm:flex sm:items-center sm:justify-between">
				  <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2023 <a href="/" class="hover:underline">MagicPost™</a>. All Rights Reserved.
				  </span>
				  <div class="flex mt-4 sm:justify-center sm:mt-0">
					  <a href="/" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
						  <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 8 19">
								<path fill-rule="evenodd" d="M6.135 3H8V0H6.135a4.147 4.147 0 0 0-4.142 4.142V6H0v3h2v9.938h3V9h2.021l.592-3H5V3.591A.6.6 0 0 1 5.592 3h.543Z" clip-rule="evenodd"/>
							</svg>
						  <span class="sr-only">Facebook page</span>
					  </a>
					  <a href="/" class="text-gray-500 hover:text-gray-900 dark:hover:text-white ms-5">
						  <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 21 16">
								<path d="M16.942 1.556a16.3 16.3 0 0 0-4.126-1.3 12.04 12.04 0 0 0-.529 1.1 15.175 15.175 0 0 0-4.573 0 11.585 11.585 0 0 0-.535-1.1 16.274 16.274 0 0 0-4.129 1.3A17.392 17.392 0 0 0 .182 13.218a15.785 15.785 0 0 0 4.963 2.521c.41-.564.773-1.16 1.084-1.785a10.63 10.63 0 0 1-1.706-.83c.143-.106.283-.217.418-.33a11.664 11.664 0 0 0 10.118 0c.137.113.277.224.418.33-.544.328-1.116.606-1.71.832a12.52 12.52 0 0 0 1.084 1.785 16.46 16.46 0 0 0 5.064-2.595 17.286 17.286 0 0 0-2.973-11.59ZM6.678 10.813a1.941 1.941 0 0 1-1.8-2.045 1.93 1.93 0 0 1 1.8-2.047 1.919 1.919 0 0 1 1.8 2.047 1.93 1.93 0 0 1-1.8 2.045Zm6.644 0a1.94 1.94 0 0 1-1.8-2.045 1.93 1.93 0 0 1 1.8-2.047 1.918 1.918 0 0 1 1.8 2.047 1.93 1.93 0 0 1-1.8 2.045Z"/>
							</svg>
						  <span class="sr-only">Discord community</span>
					  </a>
					  <a href="/" class="text-gray-500 hover:text-gray-900 dark:hover:text-white ms-5">
						  <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 17">
							<path fill-rule="evenodd" d="M20 1.892a8.178 8.178 0 0 1-2.355.635 4.074 4.074 0 0 0 1.8-2.235 8.344 8.344 0 0 1-2.605.98A4.13 4.13 0 0 0 13.85 0a4.068 4.068 0 0 0-4.1 4.038 4 4 0 0 0 .105.919A11.705 11.705 0 0 1 1.4.734a4.006 4.006 0 0 0 1.268 5.392 4.165 4.165 0 0 1-1.859-.5v.05A4.057 4.057 0 0 0 4.1 9.635a4.19 4.19 0 0 1-1.856.07 4.108 4.108 0 0 0 3.831 2.807A8.36 8.36 0 0 1 0 14.184 11.732 11.732 0 0 0 6.291 16 11.502 11.502 0 0 0 17.964 4.5c0-.177 0-.35-.012-.523A8.143 8.143 0 0 0 20 1.892Z" clip-rule="evenodd"/>
						</svg>
						  <span class="sr-only">Twitter page</span>
					  </a>
					  <a href="/" class="text-gray-500 hover:text-gray-900 dark:hover:text-white ms-5">
						  <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
								<path fill-rule="evenodd" d="M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z" clip-rule="evenodd"/>
						  </svg>
						  <span class="sr-only">GitHub account</span>
					  </a>
					  <a href="/" class="text-gray-500 hover:text-gray-900 dark:hover:text-white ms-5">
						  <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
							<path fill-rule="evenodd" d="M10 0a10 10 0 1 0 10 10A10.009 10.009 0 0 0 10 0Zm6.613 4.614a8.523 8.523 0 0 1 1.93 5.32 20.094 20.094 0 0 0-5.949-.274c-.059-.149-.122-.292-.184-.441a23.879 23.879 0 0 0-.566-1.239 11.41 11.41 0 0 0 4.769-3.366ZM8 1.707a8.821 8.821 0 0 1 2-.238 8.5 8.5 0 0 1 5.664 2.152 9.608 9.608 0 0 1-4.476 3.087A45.758 45.758 0 0 0 8 1.707ZM1.642 8.262a8.57 8.57 0 0 1 4.73-5.981A53.998 53.998 0 0 1 9.54 7.222a32.078 32.078 0 0 1-7.9 1.04h.002Zm2.01 7.46a8.51 8.51 0 0 1-2.2-5.707v-.262a31.64 31.64 0 0 0 8.777-1.219c.243.477.477.964.692 1.449-.114.032-.227.067-.336.1a13.569 13.569 0 0 0-6.942 5.636l.009.003ZM10 18.556a8.508 8.508 0 0 1-5.243-1.8 11.717 11.717 0 0 1 6.7-5.332.509.509 0 0 1 .055-.02 35.65 35.65 0 0 1 1.819 6.476 8.476 8.476 0 0 1-3.331.676Zm4.772-1.462A37.232 37.232 0 0 0 13.113 11a12.513 12.513 0 0 1 5.321.364 8.56 8.56 0 0 1-3.66 5.73h-.002Z" clip-rule="evenodd"/>
						</svg>
						  <span class="sr-only">Dribbble account</span>
					  </a>
				  </div>
			  </div>
			</div>
		</footer>
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
