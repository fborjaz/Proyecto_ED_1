import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      // Agrega alias para los módulos de Swiper
      swiper: 'swiper/react',
    },
  },
});
