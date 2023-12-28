let timer: any;
const interval = 400;
export const debounce = (e: any, func: Function) => {
	clearTimeout(timer);
	timer = setTimeout(() => {
		func();
	}, interval);
};
