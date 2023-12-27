<script>
	import { fade } from 'svelte/transition';
	import { linear } from 'svelte/easing';
	import { goto } from '$app/navigation';

	let inputRegisterValue = ['', '', '', '', '', '', ''];
	let isRegisterInputValid = [true, true, true, true];

	let showPassword = false;
	let showRePassword = false;
	let error_messages = '';

	let invalidRegisterMessages = [
		'Vui lòng nhập tên đầy đủ.',
		'Vui lòng nhập tài khoản email.',
		'Vui lòng nhập mật khẩu.',
		'Vui lòng nhập lại mật khẩu.',
		'Vui lòng nhập ngày tháng năm sinh',
		'Vui lòng nhập số điện thoại.',
		'Vui lòng nhập địa chỉ',
	];

	// @ts-ignore
	function checkRegisterInput(index) {
		isRegisterInputValid[index] = inputRegisterValue[index].trim() !== '';
	}

	export let toggleMode = () => {};

	let inputArrays = [
		{ attrs: { type: 'text' }, placeholder: 'Full Name' },
		{ attrs: { type: 'text' }, placeholder: 'Email' },
		{ attrs: { type: 'password' }, placeholder: 'Password' },
		{ attrs: { type: 'password' }, placeholder: 'Re-enter Password' },
		{ attrs: { type: 'date' }, placeholder: 'Date of Birth' },
		{ attrs: { type: 'text' }, placeholder: 'Phone Number' },
		{ attrs: { type: 'text' }, placeholder: 'Address' }
	];

	async function handleSignUp() {
		let check =
			isRegisterInputValid.every((value) => value === true) && inputRegisterValue.every((value) => value != '');
		if (check) {
			let formData = new FormData();
			formData.append('fullname', inputRegisterValue[0]);
			formData.append('email', inputRegisterValue[1]);
			formData.append('password', inputRegisterValue[2]);
			formData.append('re_password', inputRegisterValue[3]);
			formData.append('date_of_birth', inputRegisterValue[4]);
			formData.append('phone_number', inputRegisterValue[5]);
			formData.append('address', inputRegisterValue[6]);
			const response = await fetch('https://laweng-be.vercel.app/api/signup', {
				method: 'POST',
				body: formData
			});
			if (response.status === 200) {
				toggleMode();
			} else {
				const data = await response.json();
				error_messages = data.message;
			}
		} else {
			for (let i = 0; i < inputRegisterValue.length; i++) {
				checkRegisterInput(i);
			}
		}
	}
</script>

<div
	class="top-2/4 mt-14 md:top-1/3 lg:top-2/4 2xl:top-1/3 absolute w-full xl:w-4/12 lg:w-6/12 px-4 mx-auto pt-6"
	style="
left: 50%;
transform: translate(-50%, -50%);
"
	transition:fade={{ duration: 500, easing: linear }}
>
	<div
		class="relative flex flex-col min-w-0 break-words w-full mt-15 mb-6 shadow-md rounded-lg bg-blueGray-200 border-0"
	>
		<div class="text-center mb-5 mt-10">
			<h1 class="title text-md text-4xl font-bold tracking-widest">
				<a href="/"> MAGIC POST</a>
			</h1>
		</div>
		<div class="rounded-t mb-0 px-6 py-6" />
		<div class="flex-auto px-4 lg:px-10 py-10 pt-0">
			<div class="text-blueGray-400 text-center mb-8 font-bold">
				<medium>Sign up</medium>
			</div>
			<form>
				{#each inputArrays as inputInformation, index}
					<div class="relative w-full mb-8">
						<div class="relative">
							<input
								bind:value={inputRegisterValue[index]}
								on:blur={() => checkRegisterInput(index)}
								{...inputInformation['attrs']}
								class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
								placeholder={inputInformation['placeholder']}
							/>
							{#if inputInformation['placeholder'] == 'Password'}
								<!-- svelte-ignore a11y-click-events-have-key-events -->
								<!-- svelte-ignore a11y-no-static-element-interactions -->
								{#if !showPassword}
									<i
										class="fa-solid fa-eye absolute top-1/4 p-1 right-3 cursor-pointer"
										on:click={() => {
											inputArrays[index]['attrs']['type'] = 'text';
											showPassword = true;
										}}
									/>
								{:else}
									<i
										class="fa-solid fa-eye-slash absolute top-1/4 p-1 right-3 cursor-pointer"
										on:click={() => {
											inputArrays[index]['attrs']['type'] = 'password';
											showPassword = false;
										}}
									/>
								{/if}
							{:else if inputInformation['placeholder'] == 'Re-enter Password'}
								{#if !showRePassword}
									<!-- svelte-ignore a11y-click-events-have-key-events -->
									<!-- svelte-ignore a11y-no-static-element-interactions -->
									<i
										class="fa-solid fa-eye absolute top-1/4 p-1 right-3 cursor-pointer"
										on:click={() => {
											inputArrays[index]['attrs']['type'] = 'text';
											showRePassword = true;
										}}
									/>
								{:else}
									<!-- svelte-ignore a11y-click-events-have-key-events -->
									<!-- svelte-ignore a11y-no-static-element-interactions -->
									<i
										class="fa-solid fa-eye-slash absolute top-1/4 p-1 right-3 cursor-pointer"
										on:click={() => {
											inputArrays[index]['attrs']['type'] = 'password';
											showRePassword = false;
										}}
									/>
								{/if}
							{/if}
						</div>
						{#if !isRegisterInputValid[index]}
							<div class="error-message ml-2 absolute">{invalidRegisterMessages[index]}</div>
						{/if}
					</div>
				{/each}
				{#if error_messages != ''}
					<span class="error-message">{error_messages}</span>
				{/if}
				<div class="text-center mt-6">
					<button
						class="login bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
						type="button"
						on:click={handleSignUp}
					>
						Sign Up
					</button>
				</div>
			</form>
			<div class="mt-5">
				<i>
					Already have an account?
					<span class="cursor-pointer underline" on:click={toggleMode}> Log in heres. </span>
				</i>
			</div>
		</div>
	</div>
</div>

<style>
	button {
		background-color: #1890ff;
	}

	input {
		background-color: #2b5b88;
	}

	.title {
		background-color: #00dbde;
		background-image: linear-gradient(90deg, #00dbde 0%, #fc00ff 100%);
		-webkit-background-clip: text;
		background-clip: text;
		color: transparent;
		-webkit-text-fill-color: transparent;
	}

	.error-message {
		color: #e35659;
	}
</style>
