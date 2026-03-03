import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
    base: './',
    server: {
        host: true
    },
    build: {
        rollupOptions: {
            input: {
                main: resolve('index.html'),
                salary: resolve('tool-salary-calculator.html'),
                artha: resolve('tool-artha-wealth.html'),
                homeloan: resolve('tool-home-loan-calculator.html'),
            },
        },
    },
});
