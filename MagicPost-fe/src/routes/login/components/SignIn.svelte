<script>
	import { fade } from 'svelte/transition';
	import { linear } from 'svelte/easing';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	// @ts-ignore
	let access_token = '';
	let error_messages = ''
	let isRemember = false;

	async function checkIsLoggedIn() {
		if (sessionStorage.getItem('access_token')) {
			const response = await fetch('https://laweng-be.vercel.app/api/check_login', {
				method: 'GET',
				credentials: 'include',
				headers: {
					Authorization: `Bearer ${sessionStorage.getItem('access_token')}`
				}
			});
			const information = await response.json();
			if (response.status == 200 && information.isLogin) {
				goto('/');
			}
		}
	}

	// @ts-ignore
	let isLoginInputValid = [true, true];
	let inputLoginValue = [
		'', //username
		'' //password
	];
	// @ts-ignore
	let showPassword = false;

	// @ts-ignore
	let invalidLoginMessages = [
		'You need to enter your username.',
		'The password cannot be less than 7 characters.'
	];
    
	// @ts-ignore
	// @ts-ignore
	function checkLoginInput(index) {
		// @ts-ignore
        error_messages = ''
		isLoginInputValid[index] = inputLoginValue[index].trim() !== '';
	}

	// @ts-ignore
	// @ts-ignore
	export let toggleMode = () => {};

	// @ts-ignore
	let inputArrays = [
		{ attrs: { type: 'text' }, placeholder: 'Username' },
		{ attrs: { type: 'password' }, placeholder: 'Password' }
	];

	// @ts-ignore
	async function handleSignInWithGoogle() {
		// @ts-ignore
		// @ts-ignore
		const popup = await window.open(
			'https://laweng-be.vercel.app/api/login_with_google',
			'_blank',
			'width=600,height=800'
		); // Mở popup hoặc tab mới

		if (popup) {
			var timer = setInterval(async function () {
				if (popup.closed) {
					clearInterval(timer);
					await checkIsLoggedIn();
				}
			}, 1000);
		}

		window.addEventListener('message', (event) => handleMessageFromBackend(event));
		window.removeEventListener('message', (event) => handleMessageFromBackend(event));
	}


	// @ts-ignore
	function handleMessageFromBackend(event ) {
		if (event.origin !== 'https://laweng-be.vercel.app') {
					return; // Bỏ qua các sự kiện từ nguồn không an toàn
				}

				// Nhận dữ liệu từ cửa sổ con
		const data = event.data;

		sessionStorage.setItem('access_token', data.access_token);
	}

    async function handleSignInWithFacebook() {
		// @ts-ignore
		// @ts-ignore
		const popup = await window.open(
			'https://laweng-be.vercel.app/api/login_with_facebook',
			'_blank',
			'width=600,height=800'
		); // Mở popup hoặc tab mới
		if (popup) {
			var timer = setInterval(async function () {
				if (popup.closed) {
					clearInterval(timer);
					await checkIsLoggedIn();
				}
			}, 1000);
		}
		// Lắng nghe sự kiện message
		window.addEventListener('message', (event) => handleMessageFromBackend(event));
		window.removeEventListener('message', (event) => handleMessageFromBackend(event));
	}


	async function handleSignIn() {
		let check = isLoginInputValid.every((value) => value === true) && inputLoginValue.every((value) => value != '');
		if (check) {
			let formData = new FormData();
			formData.append('username', inputLoginValue[0]);
			formData.append('password', inputLoginValue[1]);
			const res = await fetch(`https://laweng-be.vercel.app/api/login`, {
				method: 'POST',
				body: formData,
				credentials: 'include'
			});
			if (res.status == 200) {
				const data = await res.json();
				access_token = data['access_token'];
				sessionStorage.setItem('access_token', access_token);
				goto('/');
			} else {
				const data = await res.json();
				error_messages = data.message
			}
		} else {
            for(let i = 0; i < inputLoginValue.length; i++) {
				checkLoginInput(i)
			}
        }
	}
</script>

<div
	class="top-2/4 md:top-1/3 lg:top-2/4 2xl:top-1/3 absolute w-full xl:w-4/12 lg:w-6/12 px-4 mx-auto pt-6"
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
				<a href="/"> MAGIC POST </a>
			</h1>
		</div>
		<div class="rounded-t mb-0 px-6 py-6">
			<div class="text-center mb-3">
				<h3 class="text-blueGray-500 text-sm font-bold">Sign in with</h3>
			</div>
			<div class="btn-wrapper text-center">
				<button
					class="bg-white font-semibold active:bg-blueGray-50 text-blueGray-700 px-4 py-2 rounded outline-none focus:outline-none mr-2 mb-1 uppercase shadow hover:shadow-md inline-flex items-center font-semibold text-xs ease-linear transition-all duration-150"
					type="button"
                    on:click={handleSignInWithFacebook}
				>
					<i class="facebook fa-brands fa-facebook-f w-5 mr-1 align-middle" />FACEBOOK</button
				>
				<button
					class="bg-white font-semibold active:bg-blueGray-50 text-blueGray-700 px-4 py-2 rounded outline-none focus:outline-none mr-1 mb-1 uppercase shadow hover:shadow-md inline-flex items-center font-semibold text-xs ease-linear transition-all duration-150"
					type="button"
					on:click={handleSignInWithGoogle}
				>
					<i class="google custom-icon fa-brands fa-google w-5 mr-1 align-middle" />Google
				</button>
			</div>
			<hr class="mt-6 border-b-1 border-blueGray-300" />
		</div>
		<div class="flex-auto px-4 lg:px-10 py-10 pt-0">
			<div class="text-blueGray-400 text-center mb-8 font-bold">
				<medium>Or sign in with credentials</medium>
			</div>
			<form>
				{#each inputArrays as inputInformation, index}
					<div class="relative w-full mb-8">
						<div class="relative">
							<input
								bind:value={inputLoginValue[index]}
								on:blur={() => checkLoginInput(index)}
								{...inputInformation['attrs']}
								class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
								placeholder={inputInformation['placeholder']}
							/>
							{#if inputInformation['placeholder'] == 'Password'}
								<!-- svelte-ignore a11y-click-events-have-key-events -->
								<!-- svelte-ignore a11y-no-static-element-interactions -->
								{#if !showPassword}
									<i
										class="fa-solid fa-eye p-1 absolute top-1/4 right-3 cursor-pointer"
										on:click={() => {
											inputArrays[index]['attrs']['type'] = 'text';
											showPassword = true;
										}}
									/>
								{:else}
									<i
										class="fa-solid fa-eye-slash p-1 absolute top-1/4 right-3 cursor-pointer"
										on:click={() => {
											inputArrays[index]['attrs']['type'] = 'password';
											showPassword = false;
										}}
									/>
								{/if}
							{/if}
						</div>

						{#if !isLoginInputValid[index]}
							<div class="error-message ml-2 absolute">{invalidLoginMessages[index]}</div>
						{/if}
					</div>
				{/each}
                {#if error_messages != ''}
                    <span class="error-message">{error_messages}</span>
                {/if}
				<div>
					<label class="inline-flex items-center cursor-pointer"
						><input
							id="customCheckLogin"
							type="checkbox"
							class="form-checkbox border-0 rounded text-blueGray-700 ml-1 w-5 h-5 ease-linear transition-all duration-150"
							bind:checked={isRemember}
						/>
							<span class="ml-2 text-sm font-semibold text-blueGray-600">
								Remember me
							</span>
						</label
					>
				</div>
				<div class="text-center mt-6">
					<button
						class="login bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
						type="button"
						on:click={handleSignIn}
					>
						Sign In
					</button>
				</div>
			</form>
			<div class="mt-5">
				<i>
					Don't have an account?
					<span class="cursor-pointer underline" on:click={toggleMode}> Sign up now! </span>
				</i>
			</div>
		</div>
	</div>
</div>

<style>
	i.facebook {
		color: #0268e2;
	}

	i.google {
		background: conic-gradient(
				from -45deg,
				#ea4335 110deg,
				#4285f4 90deg 180deg,
				#34a853 180deg 270deg,
				#fbbc05 270deg
			)
			73% 55%/150% 150% no-repeat;
		-webkit-background-clip: text;
		background-clip: text;
		color: transparent;
		-webkit-text-fill-color: transparent;
	}

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
