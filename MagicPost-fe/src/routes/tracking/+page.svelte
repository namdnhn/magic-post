<script lang="ts">
	import { page } from '$app/stores';
	import Tracking from 'src/components/Tracking.svelte';
	import type { PageServerData } from '../$types';
	import Loading from 'src/components/Loading.svelte';
    import { Check} from 'lucide-svelte';
	export let data: PageServerData;
    import { goto } from '$app/navigation';
	console.log('🚀 ~ file: +page.svelte:8 ~ data:', data);

    let trackingOrder: string;
</script>

<div class="flex flex-col items-center w-full md:my-10">
	<main class="flex flex-col gap-5 bg-surface-200 md:w-[60vw] p-3">

        <div class="w-full  bg-surface-200 rounded-md flex gap-5">
            <input type="text" placeholder="Mã đơn" 
            class="dui-input dui-input-bordered dui-input-lg w-full"
            bind:value={trackingOrder}
            />
            <button type="button" 
            class="btn variant-filled-secondary rounded-md w-1/5"
            on:click={() => goto(`/tracking/${trackingOrder}`)}
            >Theo dõi</button>
        </div>
	</main>
	<div class="trail-dash" />
</div>

<style>


</style>
