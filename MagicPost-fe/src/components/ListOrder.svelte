<script lang="ts">
	import { Eye, PackagePlus, PencilLine } from 'lucide-svelte';
	import { Catergority } from 'src/utils/interface';
	import type { Order } from 'src/utils/interface';

	export let orderData: Order;

	let checked = false;
</script>

<div class="card w-full mb-1 !rounded-sm" class:!bg-secondary-100={checked}>
	<div class="p-4 pb-3 grid grid-cols-2 gap-2">
		<div class="flex items-start gap-1">
			<input
				class="dui-checkbox dui-checkbox-secondary dui-checkbox-sm rounded-sm border-[#000]"
				type="checkbox"
				bind:checked
				on:change
			/>
			<b>Mã đơn: &nbsp;</b>
			<span class="text-surface-500 font-bold">
				{orderData.orderId}
			</span>
		</div>
		<div class="flex justify-end gap-3">
			<div class="dui-tooltip dui-tooltip-bottom bg-" data-tip="Xem chi tiết">
				<button type="button" class="btn-icon variant-filled-secondary h-8 w-8">
					<Eye size="16" />
				</button>
			</div>
			<button type="button" class="btn-icon variant-filled-error h-8 w-8">
				<PencilLine size="16" />
			</button>
		</div>

		<div class="flex gap-1" style="border-right: 1px solid #a3a3a3;">
			<b>Trạng thái:</b>
			<span class="flex  gap-1 text-greenNew">Mới </span>
		</div>

		<div class="grid grid-cols-2">
			<span>
				<b>Loại:</b>
				{orderData.category}
			</span>
			<div>
				<b>Cước phí: </b>
				{orderData.mainCharge} ₫
			</div>
		</div>

		<div style="border-right: 1px solid #a3a3a3;">
			<b>Người gửi:</b>
			<p> {orderData.orderDelivery.fromLocation.name}</p>
			<p>{orderData.orderDelivery.fromLocation.address}</p>
		</div>
		<div>
			<b>Người nhận:</b>
			<p>{orderData.orderDelivery.toLocation.name}</p>
			<p>{orderData.orderDelivery.toLocation.address}</p>
		</div>
	</div>
	<div class="trail-dash" />
</div>

<style>
	.card:hover .trail-dash {
		visibility: visible;
	}
	.trail-dash {
		visibility: hidden;
		height: 0.1875rem;
		width: 100%;

	}
</style>
