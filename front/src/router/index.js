import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/ChatPage.vue'
import AboutPage from '../views/AboutPage.vue'
import ConfigurationPage from '../views/ConfigurationPage.vue'


const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/about', name: 'About', component: AboutPage },
  { path: '/configuration', name: 'Configuration', component: ConfigurationPage },
 
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
