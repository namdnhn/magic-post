<script lang="ts">
	import { BaggageClaim, Blocks, Check, ClipboardList, MapPin, Plane, Truck } from 'lucide-svelte';
</script>

<ul>
	<!-- Đã giao -->
	<li>
		<!-- Dòng chính (icon) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center">
					<div class="tracking-icon tracking-icon-success">
						<Check class="w-5 h-5" />
					</div>
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5 mt-1">15:20 30-05-2023</div>
			</div>
			<div class="mt-1">
				<div class="tracking-text-success"><strong>Đã giao</strong></div>
				<div class="tracking-text-success">Đơn hàng đã được giao thành công</div>
				<a class="tracking-link-image" >Xem hình ảnh giao hàng</a>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center min-w-[2rem]">
					<div class="tracking-hr grow" />
					<div class="tracking-dot rounded-full w-3 h-3" />
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5">15:20 30-05-2023</div>
			</div>
			<div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center min-w-[2rem]">
					<div class="tracking-hr grow" />
					<div class="tracking-dot rounded-full w-3 h-3" />
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5">15:20 30-05-2023</div>
			</div>
			<div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
	</li>

	<!-- Đang giao hàng -->
	<li>
		<!-- Dòng chính (icon) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center">
					<div class="tracking-icon">
						<Truck class="w-5 h-5" />
					</div>
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5 mt-1">15:20 30-05-2023</div>
			</div>
			<div class="mt-1">
				<div><strong>Đang giao hàng</strong></div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center min-w-[2rem]">
					<div class="tracking-hr grow" />
					<div class="tracking-dot rounded-full w-3 h-3" />
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5">15:20 30-05-2023</div>
			</div>
			<div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center min-w-[2rem]">
					<div class="tracking-hr grow" />
					<div class="tracking-dot rounded-full w-3 h-3" />
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5">15:20 30-05-2023</div>
			</div>
			<div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
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
				<div class="mx-5 mt-1">15:20 30-05-2023</div>
			</div>
			<div class="mt-1">
				<div><strong>Đã đến Việt Nam</strong></div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center min-w-[2rem]">
					<div class="tracking-hr grow" />
					<div class="tracking-dot rounded-full w-3 h-3" />
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5">15:20 30-05-2023</div>
			</div>
			<div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center min-w-[2rem]">
					<div class="tracking-hr grow" />
					<div class="tracking-dot rounded-full w-3 h-3" />
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5">15:20 30-05-2023</div>
			</div>
			<div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
	</li>

	<!-- Vận chuyển đến Việt Nam -->
	<li>
		<!-- Dòng chính (icon) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center">
					<div class="tracking-icon">
						<Plane class="w-5 h-5" />
					</div>
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5 mt-1">15:20 30-05-2023</div>
			</div>
			<div class="mt-1">
				<div><strong>Vận chuyển đến Việt Nam</strong></div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center min-w-[2rem]">
					<div class="tracking-hr grow" />
					<div class="tracking-dot rounded-full w-3 h-3" />
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5">15:20 30-05-2023</div>
			</div>
			<div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center min-w-[2rem]">
					<div class="tracking-hr grow" />
					<div class="tracking-dot rounded-full w-3 h-3" />
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5">15:20 30-05-2023</div>
			</div>
			<div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
	</li>

	<!-- Đang xử lý đơn hàng nước ngoài -->
	<li>
		<!-- Dòng chính (icon) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center">
					<div class="tracking-icon">
						<BaggageClaim class="w-5 h-5" />
					</div>
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5 mt-1">15:20 30-05-2023</div>
			</div>
			<div class="mt-1">
				<div><strong>Đang xử lý đơn hàng nước ngoài</strong></div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center min-w-[2rem]">
					<div class="tracking-hr grow" />
					<div class="tracking-dot rounded-full w-3 h-3" />
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5">15:20 30-05-2023</div>
			</div>
			<div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center min-w-[2rem]">
					<div class="tracking-hr grow" />
					<div class="tracking-dot rounded-full w-3 h-3" />
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5">15:20 30-05-2023</div>
			</div>
			<div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
	</li>

	<!-- Đang được chuẩn bị -->
	<li>
		<!-- Dòng chính (icon) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center">
					<div class="tracking-icon">
						<Blocks class="w-5 h-5" />
					</div>
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5 mt-1">15:20 30-05-2023</div>
			</div>
			<div class="mt-1">
				<div><strong>Đang được chuẩn bị</strong></div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center min-w-[2rem]">
					<div class="tracking-hr grow" />
					<div class="tracking-dot rounded-full w-3 h-3" />
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5">15:20 30-05-2023</div>
			</div>
			<div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
		<!-- Dòng phụ (chấm tròn) -->
		<div class="flex">
			<div class="flex">
				<div class="flex flex-col items-center min-w-[2rem]">
					<div class="tracking-hr grow" />
					<div class="tracking-dot rounded-full w-3 h-3" />
					<div class="tracking-hr grow" />
				</div>
				<div class="mx-5">15:20 30-05-2023</div>
			</div>
			<div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
			</div>
		</div>
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
				<div class="mx-5 mt-1">15:20 30-05-2023</div>
			</div>
			<div class="mt-1">
				<div><strong>Đặt hàng thành công</strong></div>
				<div class="tracking-text-pending">Đơn hàng đã được giao thành công</div>
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
	.tracking-text-success {
		color: #26ab9a;
	}
	.tracking-link-image {
		color: rgb(59, 130, 246);
	}
	.tracking-text-pending {
		color: gray;
	}
</style>