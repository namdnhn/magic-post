<script lang="ts">
    let tableData: any = [
        {id: "123", phone: "1800 1008", name: "Nguyễn Văn A", quantity: "1" , price: "100000"},
        {id: "456", phone: "1800 1008", name: "Nguyễn Văn A", quantity: "3" , price: "300000"},
        {id: "789", phone: "1800 1008", name: "Nguyễn Văn A", quantity: "2" , price: "400000"},
    ]
    function totalQuantity() {
        let total = 0;
        tableData.forEach((element: any) => {
            total += parseInt(element.quantity)
        });
        return total;
    }
    function totalPrice() {
        let total = 0;
        tableData.forEach((element: any) => {
            total += parseInt(element.price)
        });
        return total;
    }
</script>

<div class="bg-[#fff] p-4 my-4" style="width: 1000px">
	<div class="flex items-center justify-around">
		<span>
			<img src="/img/logo-new.png" alt="logo" class="h-16" />
		</span>
		<p class="uppercase text-lg">Biên bản bàn giao vận đơn (ID: 1007139). Ngày 22/12/2023</p>
	</div>
	<div class="flex mt-4">
		<p class="ml-2 w-[60%]"><strong>Điểm chuyển phát hiện tại: </strong>Kho 1 - Khôi</p>
        <p><strong>Ngày giờ in: </strong>29/12/2023 12:34</p>
	</div>
    <div class="flex">
		<p class="ml-2 w-[60%]"><strong>Ghi chú: </strong>note...</p>
        <p><strong>Điểm chuyển phát tiếp theo: </strong>Kho 2 - Nam</p>
	</div>
	<table class="receipt-table w-full mt-2">
		<thead>
			<tr>
				<th><strong>STT</strong></th>
				<th><strong>Mã đơn hàng</strong></th>
				<th><strong>Người nhận</strong></th>
				<th><strong>SL SP</strong></th>
				<th><strong>Tổng thu</strong></th>
			</tr>
		</thead>
		<tbody>
            {#each tableData as tableRow, index}
                <tr>
                    <td class="text-center">{index + 1}</td>
                    <td>{tableRow.id}</td>
                    <td>{tableRow.phone} {tableRow.name}</td>
                    <td class="text-center">{tableRow.quantity}</td>
                    <td class="text-end">{tableRow.price}</td>
                </tr>
            {/each}
			<tr class="">
				<td class="text-center" colspan="3" ><strong>Tổng</strong></td>
				<td class="text-center"><strong>{totalQuantity()}</strong></td>
				<td class="text-end"><strong>{totalPrice()}</strong></td>
			</tr>
		</tbody>
	</table>
	<div class="w-full flex mt-4 h-40">
		<div class="box-sender w-[50%] text-center">
			<p class="mt-2">Người gửi</p>
			<p>(Ký và ghi rõ họ tên)</p>
		</div>
		<div class="box-receiver w-[50%] text-center">
			<p class="mt-2">Người nhận</p>
			<p>(Ký và ghi rõ họ tên)</p>
		</div>
	</div>
</div>

<style>
	.receipt-table, th, td {
		border: 1px solid black;
		border-collapse: collapse;
	}
	.receipt-table td, .receipt-table th {
		padding: 4px;
	}
	.box-sender {
		border: 1px solid black;
		border-right: none;
	}
	.box-receiver {
		border: 1px solid black;
	}
</style>