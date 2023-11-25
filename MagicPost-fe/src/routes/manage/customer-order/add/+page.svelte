<script lang="ts">
	import { ArrowLeft, Eye, FilePlus2, PlusCircle } from 'lucide-svelte';
	import CustomerInfo from 'src/components/CustomerInfo.svelte';
	import OrderContent from 'src/components/OrderContent.svelte';

	let packageType: 'document' | 'package';
	let orderContents: any[] = [{ id: crypto.randomUUID(), content: '', quantity: undefined, value: undefined }];
	function addOrderContent() {
		const id = crypto.randomUUID();
		orderContents = [...orderContents, { id, content: '', quantity: undefined, value: undefined }];
	}

	$: console.log(packageType);
</script>

<main>
	<div class="flex justify-between">
		<div class="flex gap-5 items-center">
			<a href="/manage/customer-order" class="btn-icon btn-icon-sm variant-filled">
				<ArrowLeft size="18" />
			</a>
			<p class="title uppercase font-vn">Tạo đơn đặt hàng mới</p>
		</div>
		<div>
			<button type="button" class="btn variant-filled" disabled>
				<Eye size="20" class="mr-2" />Xem trước đơn hàng
			</button>
			<button type="button" class="btn variant-filled bg-[#2460E5]">
				<FilePlus2 size="20" class="mr-2" />Lưu và in đơn hàng
			</button>
		</div>
	</div>
	<div class="main-info">
		<div class="card rounded-lg p-4">
			<p class="text-xl font-bold">Thông tin người gửi</p>
			<hr class="my-2" />
			<CustomerInfo target="gửi" />
		</div>
		<div class="card rounded-lg p-4">
			<p class="text-xl font-bold">Thông tin người nhận</p>
			<hr class="my-2" />
			<CustomerInfo target="nhận" />
		</div>
	</div>

	<div class="card rounded-lg p-4 mt-5">
		<p class="text-xl font-bold">Thông tin đơn hàng</p>
		<hr class="my-2" />

		<div class="mb-2">
			<label class="dui-label pb-1" for="type">
				<span class="dui-label-text">Loại hàng gửi</span>
			</label>
			<select
				name="type"
				required
				class="dui-select dui-select-sm dui-select-bordered w-full h-10"
				bind:value={packageType}
			>
				<option value="" disabled selected hidden>---Chọn loại hàng gửi---</option>
				<option value="document">Tài liệu</option>
				<option value="package">Hàng hóa</option>
			</select>
		</div>
		<div class="mb-2">
			<label class="dui-label pb-1" for="name">
				<span class="dui-label-text">Khối lượng thực tế (kg)</span>
			</label>
			<input type="text" name="name" placeholder="Nhập khối lượng" class="dui-input h-10 dui-input-bordered w-full" />
		</div>

		{#if packageType == 'package'}
			<label class="dui-label pb-1" for="name">
				<span class="dui-label-text">Nội dung giá trị bưu gửi</span>
			</label>
			{#each orderContents as content, i (content.id)}
				<OrderContent bind:content={content.content} bind:quantity={content.quantity} bind:value={content.value} />
			{/each}

			<div class="dui-tooltip dui-tooltip-bottom" data-tip="Thêm nội dung">
				<button type="button" class="btn-icon w-max" on:click={addOrderContent}>
					<PlusCircle class="text-primary-500" size="28" />
				</button>
			</div>
		{/if}
	</div>
</main>

<style>
	main {
		padding-bottom: 60px;
	}

	.title {
		font-size: 22px;
		font-weight: 800;
		line-height: 28px;
	}

	.main-info {
		display: grid;
		grid-template-columns: auto auto;
		gap: 15px;
		margin-top: 16px;
	}

	select:invalid {
		color: #9ca3af;
	}

	select:focus {
		color: #000;
	}
</style>
