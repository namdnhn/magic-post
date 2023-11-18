import { join } from 'path';
import type { Config } from 'tailwindcss';
import { skeleton } from '@skeletonlabs/tw-plugin';

export default {
	darkMode: 'class',
	content: [
		'./src/**/*.{html,js,svelte,ts}',
		join(require.resolve('@skeletonlabs/skeleton'), '../**/*.{html,js,svelte,ts}')
	],
	theme: {
		extend: {
			boxShadow: {
				'r-md': '0 35px 60px -15px rgba(0, 0, 0, 0.3)'
			}
		},
		colors:{
			"ocean": '#2460E5'
		}
	},
	plugins: [
		skeleton({
			themes: { preset: ['crimson'] }
		}),
		require('daisyui')
	],
	daisyui: {
		base: false,
		prefix: 'dui-',
		themes: ['garden']
	}
} satisfies Config;
