import axios from 'axios';

const axiosInstance = axios.create({
	baseURL: 'http://localhost:8000/api/v1', // replace with your API base URL
	timeout: 10000,
	headers: { 'Content-Type': 'application/json' }
});

export default axiosInstance;