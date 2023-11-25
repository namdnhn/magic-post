<script lang="ts">
	export let content: string, quantity: number, value: number;
</script>

<div class="grid grid-cols-3 gap-2 mb-2">
	<input
		type="text"
		placeholder="Nhập nội dung"
		class="dui-input h-10 dui-input-bordered w-full"
		bind:value={content}
	/>
	<input
		type="number"
		placeholder="Nhập số lượng"
		class="dui-input h-10 dui-input-bordered w-full"
		bind:value={quantity}
	/>
	<input type="" placeholder="Nhập trị giá" class="dui-input h-10 dui-input-bordered w-full" bind:value />
</div>
