<script lang="ts">
	export let message = '',
		css = '';
</script>

<div class="w-full flex flex-col justify-center items-center {css}">
	<img src="/img/empty-data.png" alt="empty data" class="h-40 w-auto" />
	<span class="text-2xl text-[#8A96A3]">{message}</span>
</div>