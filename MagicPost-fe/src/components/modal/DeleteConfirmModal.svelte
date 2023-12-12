<script lang="ts">
	export let id: string, message: string, confirmAction: () => {};
	let loading = false;
</script>

<dialog {id} class="dui-modal">
	<div class="dui-modal-box w-max max-w-lg py-4 overflow-hidden">
		<form method="dialog">
			<button class="dui-btn dui-btn-sm dui-btn-square dui-btn-ghost absolute right-2 top-3">✕</button>
		</form>
		<h3 class="text-xl text-center mb-2">Xác nhận xóa</h3>
		<div class="dui-divider m-0 -mx-6" />

		<p class="text-lg text-center mt-4">{@html message}</p>
		<p class="text-lg text-center mb-4">Sau khi xóa bạn sẽ không thể hoàn tác</p>

		<div class="dui-divider m-0 -mx-6" />
		<div class="flex justify-end gap-3 mt-[6px]">
			<form method="dialog">
				<button class="btn variant-outline-tertiary hover:text-primary-500 hover:variant-outline-error"> Hủy </button>
			</form>
			<button
				class="btn variant-filled bg-secondary-600"
				on:click={() => {
					loading = true;
					confirmAction();
				}}
			>
				{#if loading}
					<span class="dui-loading dui-loading-spinner dui-loading-sm" />
				{:else}
					Xóa
				{/if}
			</button>
		</div>
	</div>
	<form method="dialog" class="dui-modal-backdrop">
		<button>close</button>
	</form>
</dialog>