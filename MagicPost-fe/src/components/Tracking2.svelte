<script lang="ts">
	import { BaggageClaim, Blocks, XCircle, Check, ClipboardList, MapPin, Plane, Truck } from 'lucide-svelte';
</script>

<ul>
	<!-- Đã giao -->
	<li>
		<!-- Dòng chính (icon) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center">
					<div class="tracking-icon tracking-icon-fail">
						<XCircle class="w-5 h-5" />
					</div>
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5 mt-1">10:15 26-12-2023</div>
			</div>
			<div class="mt-1">
				<div class="tracking-text-fail"><strong>Thất bại</strong></div>
				<div class="tracking-text-fail">Lý do: Khách từ chối nhận hàng</div>
			</div>
		</div>

	</li>

	<!-- Đang giao hàng -->
	<li>
		<!-- Dòng chính (icon) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center">
					<div class="tracking-icon ">
						<Truck class="w-5 h-5" />
					</div>
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5 mt-1">07:06 26-12-2023</div>
			</div>
			<div class="mt-1">
				<div><strong>Đang giao hàng</strong></div>
				<div class="tracking-text-pending">Đang giao hàng cho khách hàng</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		
		<!-- Dòng phụ (chấm tròn) -->
		
	</li>

	<!-- Đã đến Việt Nam -->
	<li>
		<!-- Dòng chính (icon) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center">
					<div class="tracking-icon">
						<MapPin class="w-5 h-5" />
					</div>
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5 mt-1">21:09 25-12-2023</div>
			</div>
			<div class="mt-1">
				<div><strong>Đã đến ĐGD Lương Thế Vinh</strong></div>
				<div class="tracking-text-pending">Đơn hàng đã đến nơi</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		
		<!-- Dòng phụ (chấm tròn) -->
		
	</li>

	<!-- Vận chuyển đến Việt Nam -->
	<li>
		<!-- Dòng chính (icon) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center">
					<div class="tracking-icon">
						<MapPin class="w-5 h-5" />
					</div>
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5 mt-1">20:24 24-12-2023</div>
			</div>
			<div class="mt-1">
				<div><strong>Đã đến ĐTK Thanh Xuân Bắc</strong></div>
				<div class="tracking-text-pending">Đơn hàng đã đến nơi</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		
		<!-- Dòng phụ (chấm tròn) -->
		
	</li>

	<!-- Đang xử lý đơn hàng nước ngoài -->
	<li>
		<!-- Dòng chính (icon) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center">
					<div class="tracking-icon">
						<MapPin class="w-5 h-5" />
					</div>
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5 mt-1">12:03 24-12-2023</div>
			</div>
			<div class="mt-1">
				<div><strong>Đã đến ĐTK Thanh Oai 1</strong></div>
				<div class="tracking-text-pending">Đơn hàng đã đến nơi</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		
		<!-- Dòng phụ (chấm tròn) -->
		
	</li>

	<!-- Đang được chuẩn bị -->
	<li>
		<!-- Dòng chính (icon) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center">
					<div class="tracking-icon">
						<MapPin class="w-5 h-5" />
					</div>
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5 mt-1">16:36 23-12-2023</div>
			</div>
			<div class="mt-1">
				<div><strong>Đã đến ĐGD Tả Thanh Oai</strong></div>
				<div class="tracking-text-pending">Đơn hàng đã đến nơi</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		
		<!-- Dòng phụ (chấm tròn) -->
		
	</li>

	<!-- Đặt hàng thành công -->
	<li>
		<!-- Dòng chính (icon) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center">
					<div class="tracking-icon">
						<ClipboardList class="w-5 h-5" />
					</div>
				</div>
				<div class="mx-5 mt-1">16:36 23-12-2023</div>
			</div>
			<div class="mt-1">
				<div><strong>Nhận thành công</strong></div>
				<div class="tracking-text-pending">Đơn hàng đã được nhận tại ĐGD Tả Thanh Oai</div>
			</div>
		</div>
	</li>
</ul>

<style>
	.tracking-hr {
		background-color: gray;
		width: 1px;
	}
	.tracking-icon {
		border: 1px solid gray;
		color: gray;
		border-radius: 9999px;
		display: flex;
		justify-content: center;
		align-items: center;
		min-width: 2rem;
		min-height: 2rem;
	}
	.tracking-dot {
		background-color: gray;
	}
	.tracking-icon-success {
		background-color: #26ab9a;
		border: none;
		color: white;
	}
    .tracking-icon-fail {
		background-color: red;
		border: none;
		color: white;
	}
	.tracking-text-success {
		color: #26ab9a;
	}
    .tracking-text-fail {
        color: red;
    }
	.tracking-link-image {
		color: rgb(59, 130, 246);
	}
	.tracking-text-pending {
		color: gray;
	}
</style>