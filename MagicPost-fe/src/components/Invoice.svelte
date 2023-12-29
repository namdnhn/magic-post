<script lang="ts"></script>

<div class="mt-5 mb-5 flex flex-col items-center" style="background-color: white; width: 1100px">
	<div class="mt-2 mb-2 w-full flex justify-around items-center">
		<span class="">
			<img src="/img/logo-new.png" alt="logo" class="h-20" />
		</span>
		<span>
			<img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=Example" alt="QR code" class="h-20" />
		</span>
	</div>
	<div class="invoice-table w-[90%] flex flex-col">
		<div class="flex">
			<div class="invoice-cell w-[50%]">
				<p><strong>1. Họ tên địa chỉ người gửi:</strong></p>
				<p>Đỗ Nhữ Hoàng Nam</p>
				<p>144 Xuân Thủy, Cầu Giấy, Hà Nội</p>
				<div class="h-[1rem]" />
				<p><strong>Điện thoại:</strong> 0987654321</p>
				<div class="flex">
					<div class="w-[50%]"><strong>Mã khách hàng:</strong></div>
					<div class="w-[50%]"><strong>Mã bưu chính:</strong> 10179</div>
				</div>
			</div>
			<div class="invoice-cell w-[50%]">
				<p><strong>2. Họ tên địa chỉ người nhận:</strong></p>
				<p>Đặng Minh Khôi</p>
				<p>1 Đặng Tiến Đông</p>
				<div class="h-[1rem]" />
				<p><strong>Mã ĐH:</strong></p>
				<div class="flex">
					<div class="w-[50%]"><strong>Điện thoại:</strong> 0123456789</div>
					<div class="w-[50%]"><strong>Mã bưu chính:</strong> 01089</div>
				</div>
			</div>
		</div>
		<div class="flex grow">
			<div class="w-[50%] flex flex-col">
				<div class="invoice-cell">
					<p><strong>3. Loại hàng gửi:</strong></p>
					<div class="flex">
						<div class="flex w-[50%] justify-center">
							<input type="checkbox" name="doc" id="document" />
							<label class="ml-0.5" for="document">Tài liệu</label>
						</div>
						<div class="flex w-[50%] justify-center">
							<input type="checkbox" name="goods" id="goods" checked  />
							<label class="ml-0.5" for="goods">Hàng hóa</label>
						</div>
					</div>
					<p><strong>4. Nội dung trị giá bưu gửi:</strong></p>
					<table class="w-[calc(100%+4px)] text-center relative left-[-4px]">
						<thead>
							<tr>
								<td class="td-border-left-none"><strong>Nội dung</strong></td>
								<td><strong>Số lượng</strong></td>
								<td><strong>Trị giá</strong></td>
								<td class="td-border-right-none"><strong>Giấy tờ đính kèm</strong></td>
							</tr>
						</thead>
						<tbody>
							<tr>
								<td class="td-border-left-none">Tổng</td>
								<td>30</td>
								<td />
								<td class="td-border-right-none" />
							</tr>
						</tbody>
					</table>
				</div>
				<div class="invoice-cell">
					<p><strong>5. Dịch vụ đặc biệt/Cộng thêm:</strong></p>
					<div class="dotted-horizontal-rule mr-[4px] h-[1.2rem]" />
					<div class="dotted-horizontal-rule mr-[4px] h-[1.2rem] mt-[4px] mb-[8px]" />
					<p>Mã hợp đồng EMSC/PPA</p>
				</div>
				<div class="invoice-cell">
					<p><strong>6. Chỉ dẫn của người gửi khi không phát được bưu gửi:</strong></p>
					<div class="flex justify-between mx-2 my-1">
						<div class="flex">
							<input type="checkbox" name="chn" id="chn" />
							<label class="text-xs ml-0.5" for="chn">Chuyển hoàn ngay</label>
						</div>
						<div class="flex">
							<input type="checkbox" name="gdcng" id="gdcng" />
							<label class="text-xs ml-0.5" for="gdcng">Gọi điện cho người gửi/BC gửi</label>
						</div>
						<div class="flex">
							<input type="checkbox" name="cancel" id="cancel" />
							<label class="text-xs ml-0.5" for="cancel">Hủy</label>
						</div>
					</div>
					<div class="flex justify-between mx-2 mb-2">
						<div class="flex">
							<input type="checkbox" name="chtn" id="chtn" />
							<label class="text-xs ml-0.5" for="chtn">Chuyển hoàn trước ngày</label>
						</div>
						<div class="flex">
							<input type="checkbox" name="chkhtglt" id="chkhtglt" />
							<label class="text-xs ml-0.5" for="chkhtglt">Chuyển hoàn khi hết thời gian lưu trữ</label>
						</div>
					</div>
				</div>
				<div class="invoice-cell flex flex-col grow">
					<p><strong>7. Cam kết của người gửi:</strong></p>
					<p class="text-sm">
						Tôi chấp nhận các điều khoản tại mặt sau phiếu gửi và cam đoan bưu gửi này không chứa những mặt hàng nguy
						hiểm, cấm gửi. Trường hợp không phát được hãy thực hiện chỉ dẫn tại mục 6, tôi sẽ trả cước chuyển hoàn.
					</p>
					<div class="flex grow justify-between mt-1">
						<div class="w-[50%] flex flex-col justify-between">
							<p><strong>8. Ngày giờ gửi:</strong></p>
					        <div class="h-[1rem]" />
							<p class="mb-2">07h52/18/10/2023</p>
						</div>
						<div class="w-[50%]">
							<p><strong>Chữ ký người gửi</strong></p>
						</div>
					</div>
				</div>
				
			</div>
			<div class="w-[50%] flex flex-col">
				<div class="flex">
					<div class="w-[60%]">
						<div class="invoice-cell">
							<p><strong>9. Cước:</strong></p>
							<div class="flex justify-between">
								<span>a. Cước chính:</span>
								<span class="mr-[4px]">9.500</span>
							</div>
							<div class="flex justify-between">
								<span>b. Phụ phí:</span>
								<span class="mr-[4px]">1.900</span>
							</div>
							<div class="flex justify-between">
								<span>c. Cước GTGT:</span>
								<span class="mr-[4px]">0</span>
							</div>
							<div class="flex justify-between">
								<span>d. Tổng cước (gồm VAT):</span>
								<span class="mr-[4px]">12.312</span>
							</div>
							<div class="flex justify-between">
								<span>e. Thu khác:</span>
								<span class="mr-[4px]">0</span>
							</div>
							<div class="flex justify-between">
								<span><strong>f. Tổng thu:</strong></span>
								<span class="mr-[4px]"><strong>12.312</strong></span>
							</div>
						</div>
						<div class="invoice-cell">
							<p><strong>11. Thu của người nhận:</strong></p>
							<div class="flex justify-between">
								<span>COD:</span>
								<span class="mr-[4px]">0</span>
							</div>
							<div class="flex justify-between">
								<span>Thu khác:</span>
								<span class="mr-[4px]">0</span>
							</div>
							<div class="flex justify-between">
								<span>Tổng thu:</span>
								<span class="mr-[4px]">0</span>
							</div>
						</div>
					</div>
					<div class="w-[40%] grow flex flex-col">
						<div class="invoice-cell">
							<p><strong>10. Khối lượng (kg):</strong></p>
							<div class="flex justify-between">
								<span>Khối lượng thực tế:</span>
								<span class="mr-[4px]">30</span>
							</div>
							<div class="flex justify-between">
								<span>Khối lượng quy đổi:</span>
								<span class="mr-[4px]">0</span>
							</div>
						</div>
						<div class="invoice-cell grow">
							<p><strong>12. Chú dẫn nghiệp vụ:</strong></p>
							<p>1</p>
						</div>
					</div>
				</div>
				<div class="flex grow">
					<div class="invoice-cell w-[60%] flex flex-col items-center">
						<p><strong>13. Bưu cục chấp nhận</strong></p>
						<p>Chữ ký GDV nhận</p>
						<img class="rounded-full my-2" src="https://placehold.co/100" alt="QR code" />
						<p>GDV:</p>
					</div>
					<div class="invoice-cell w-[40%] grow">
						<p><strong>14. Ngày giờ nhận .....h...../...../...../20.....</strong></p>
						<p class="text-sm text-center">Người nhận/ Người được ủy quyền nhận</p>
						<p class="text-sm text-center">(Ký, ghi rõ họ tên)</p>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="mt-1 mb-5">
		<p><strong>Hotline: 1900 5454 33 - Website: www.ems.com.vn - Email: cskh@ems.com.vn</strong></p>
	</div>
</div>

<style>
	.invoice-cell {
		border: 1px solid black;
		padding-left: 4px;
	}
	.invoice-table {
		border: 1px solid black;
	}
	td {
		border: 1px solid black;
	}
	thead {
		background-color: #eeeeee;
	}
	.td-border-left-none {
		border-left: none;
	}
	.td-border-right-none {
		border-right: none;
	}
	.dotted-horizontal-rule {
		border-bottom: 3px dotted black;
	}
</style>
