import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // Importa el router
import 'vue-loading-overlay/dist/css/index.css';

const app = createApp(App)

// Usa el router en la aplicación Vue
app.use(router)

app.mount('#app')
