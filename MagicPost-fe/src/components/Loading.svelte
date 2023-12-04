<script lang="ts">
	export let message = '';
</script>

<div class="h-full w-full flex justify-center items-center gap-2">
	<span class="dui-loading dui-loading-ring dui-loading-lg" />
	<span class="text-lg">
		{message}
	</span>
</div>
