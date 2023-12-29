<script lang="ts">
	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';

	let chart;

	onMount(() => {
		const ctx = document.getElementById('myChart').getContext('2d');

		chart = new Chart(ctx, {
			type: 'bar',
			data: {
				labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
				datasets: [
                    {
                        label: 'Đơn thất bại',
						data: [0, 0, 0, 0, 0, 0, 0, 3, 5, 10, 10, 4],
						backgroundColor: 'rgba(165, 42, 42, 1)',
						borderColor: 'rgba(220, 20, 60, 1)',
						borderWidth: 1
                    },
					{
						label: 'Đơn thành công',
						data: [0, 0, 0, 0, 0, 0, 0, 15, 19, 26, 35, 37],
						backgroundColor: 'rgba(75, 192, 192, 0.2)',
						borderColor: 'rgba(75, 192, 192, 1)',
						borderWidth: 1
					}
				]
			},
			options: {
				scales: {
					y: {
						beginAtZero: true
					}
				}
			}
		});
	});
</script>

<main class="h-full">
	<div class="flex justify-between items-center mb-3">
		<h1 class="h3 uppercase">Thống kê hàng hóa</h1>
	</div>

	<div class="card ">
		<canvas id="myChart" width="400" height="150"></canvas>
	</div>
</main>
