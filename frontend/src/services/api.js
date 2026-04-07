import axios from 'axios';

const MAX_RETRIES = 2;
const INITIAL_DELAY_MS = 3000;

function isRetryable(error) {
    if (error.code === 'ECONNABORTED') return true;
    if (error.code === 'ERR_NETWORK') return true;
    if (!error.response) return true;
    const status = error.response.status;
    return status === 502 || status === 503 || status === 504;
}

const api = axios.create({
    baseURL: process.env.REACT_APP_FASTAPI_URL || 'http://127.0.0.1:8000',
    headers: { 'Content-Type': 'application/json' },
    timeout: 120000,
});

api.interceptors.request.use(
    (config) => {
        if (config.__retryCount === undefined) config.__retryCount = 0;
        return config;
    },
    (error) => Promise.reject(error)
);

api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const config = error.config;

        if (config && isRetryable(error) && config.__retryCount < MAX_RETRIES) {
            config.__retryCount += 1;
            const delay = INITIAL_DELAY_MS * config.__retryCount;
            console.warn(
                `[API Retry ${config.__retryCount}/${MAX_RETRIES}] ` +
                `Retrying ${config.url} in ${delay}ms…`
            );
            await new Promise((res) => setTimeout(res, delay));
            return api(config);
        }

        const status = error.response?.status;
        const detail = error.response?.data?.detail;

        const messages = {
            400: detail || 'Invalid input. Please check your farm details.',
            404: 'Requested resource not found.',
            422: 'Validation error. Some fields are missing or incorrect.',
            500: 'Server error. The model or backend is unavailable.',
            502: 'Server is waking up. Please try again in a minute.',
            503: 'Server is temporarily unavailable. Please try again shortly.',
        };

        let message;
        if (error.code === 'ECONNABORTED') {
            message = 'The server took too long to respond. It may be waking up — please try again.';
        } else {
            message = messages[status]
                ?? detail
                ?? error.message
                ?? 'An unexpected error occurred.';
        }

        error.userMessage = message;
        console.error(`[API Error ${status || error.code}]`, message);
        return Promise.reject(error);
    }
);

export const generateFarmPlan = async (data) => {
    const response = await api.post('/generate-farm-plan', data);
    return response.data;
};

export const predictCrop = (data) =>
    api.post('/predict-crop', data).then(r => r.data);

export const predictYield = (data) =>
    api.post('/predict-yield', data).then(r => r.data);

export const optimizeAllocation = (data) =>
    api.post('/optimize-allocation', data).then(r => r.data);

export default api;
