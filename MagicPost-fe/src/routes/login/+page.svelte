<script>
	// @ts-nocheck
	// import '../../app.css';
	import { onMount } from 'svelte';
	import { fade } from 'svelte/transition';
	import { linear } from 'svelte/easing';
	import { goto } from '$app/navigation';

	import SignIn from './components/SignIn.svelte';
	import SignUp from './components/SignUp.svelte';
	let isLogin = true;

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

	// @ts-ignore

	onMount(async () => {
		// @ts-ignore
		await checkIsLoggedIn();
		particlesJS('particles-js', {
			particles: {
				number: {
					value: 80
				},
				size: {
					value: 2
				},
				shape: {
					type: 'circle'
				},
				opacity: {
					value: 0.7
				},
				color: {
					value: '#dedede'
				}
			},
			lines: {
				color: '#dedede',
				width: 1,
				opacity: 0.4,
				distance: 150
				//...
			},
			move: {
				speed: 3
			},
			interactivity: {
				events: {
					onhover: {
						enable: true,
						mode: 'grab'
					},
					onclick: {
						enable: true,
						mode: 'push'
					}
				}
			}
		});
	});

	function toggleMode() {
		isLogin = !isLogin;
	}
</script>

<div id="particles-js" />
<section
	class="relative bg-blueGray-50 mx-auto"
	style="
	height: 100vh
"
>
	{#if isLogin}
		<SignIn {toggleMode} />
	{:else}
		<SignUp {toggleMode} />
	{/if}
</section>

<style>
	#particles-js {
		position: absolute;
		width: 100%;
		height: 100%;
		background-image: linear-gradient(to top left, #30cfd0 0%, #330867 100%);
	}
	section {
		color: white;
		overflow: hidden;
		position: relative;
	}
</style>
