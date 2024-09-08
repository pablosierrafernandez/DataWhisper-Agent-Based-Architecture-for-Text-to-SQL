<template>
  <div class="hero-chat mx-1000">
    <div class="hero-chat-list" ref="chatList">
      <!-- Mensajes del chat -->
      <div v-for="message in messages" :key="message.id" class="hero-chat-item">
        <img :src="message.sender === 'You' ? '/src/assets/img/user.svg' : '/src/assets/img/user-assistify.png'" alt="user" />
        <div class="hero-chat-item-content">
          <h3>{{ message.sender }} <span>{{ formatTimestamp(message.timestamp) }}</span></h3>

          <!-- Mostrar tabla si el contenido es JSON, sino mostrar texto -->
          <div v-if="isJsonString(message.content)">
            <table>
              <thead>
                <tr>
                  <th v-for="(key, index) in getTableHeaders(message.content)" :key="index">{{ key }}</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(row, rowIndex) in getDisplayedRows(message.content)" :key="rowIndex">
                  <td v-for="(value, key) in row" :key="key">{{ value }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p v-else>{{ message.content }}</p>
        <!-- Mostrar SQL si está disponible -->
<div v-if="message.sql" class="sql-info">
   <pre>{{ message.sql }}</pre>
</div>
          <!-- Mostrar coste si está disponible -->
          <div v-if="message.cost" class="cost-info">
            <strong>Cost:</strong> {{ message.cost }}
          </div>

          <!-- Mostrar insights si existen -->
          <div v-if="message.insights && message.insights.length > 0" class="insights">
            <h4>Recommendations:</h4>
            <ul>
              <li v-for="(insight, index) in message.insights" :key="index">
                <button @click="submitInsight(insight.description)">
                  {{ insight.description }}
                </button>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Skeleton Loader Manual -->
      <div v-if="isLoading" class="hero-chat-item">
        <img src="/src/assets/img/user-assistify.png" alt="user" />
        <div class="hero-chat-item-content">
          <h3>DataWhisper <span>Typing...</span></h3>
          <div class="skeleton-loader">
            <div class="skeleton-line"></div>
            <div class="skeleton-line"></div>
            <div class="skeleton-line short"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="hero-chat-input">
      <input type="text" v-model="userInput" placeholder="Type your message" @keyup.enter="submitMessage" :disabled="isLoading" />
<button @click="submitMessage" :disabled="isLoading">
  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
    <path d="M3 20V14L11 12L3 10V4L22 12L3 20Z" fill="url(#paint0_linear)" />
    <defs>
      <linearGradient id="paint0_linear" x1="3" y1="4" x2="24.0458" y2="20.434" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#f2a3b8" /> <!-- Rosa Suave -->
        <stop offset="50%" stop-color="#9fc2e9" /> <!-- Azul Claro Pastel -->
        <stop offset="100%" stop-color="#b9f3e5" /> <!-- Verde Aqua -->
      </linearGradient>
    </defs>
  </svg>
</button>


      <!-- Botón para borrar historial -->
      <button @click="clearHistory" class="clear-history-btn">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
          <path d="M3 6L5 6L21 6V8L19 8L19 19C19 20.1046 18.1046 21 17 21L7 21C5.89543 21 5 20.1046 5 19L5 8L3 8V6ZM7 8L7 19H17L17 8L7 8Z" fill="url(#paint0_linear_83_965)"/>
          <path d="M7 3V4H17V3H15V2H9V3H7Z" fill="url(#paint0_linear_83_965)"/>
          <defs>
            <linearGradient id="paint0_linear_83_965" x1="3" y1="2" x2="22" y2="23" gradientUnits="userSpaceOnUse">
              <stop stop-color="#A570FF"/>
              <stop offset="0.5" stop-color="#FF6EB2"/>
              <stop offset="1" stop-color="#FFAD66"/>
            </linearGradient>
          </defs>
        </svg>
      </button>
    </div>
  </div>
</template>



<script setup>
import { ref, watch, onMounted } from 'vue';
import axios from 'axios';

const userInput = ref('');
const messages = ref([]);
const isLoading = ref(false);
const rowsPerPage = 20;

// Función para cargar los mensajes desde localStorage
const loadMessages = () => {
  const savedMessages = localStorage.getItem('chatMessages');
  if (savedMessages) {
    messages.value = JSON.parse(savedMessages);
  }
};

const saveMessages = () => {
  localStorage.setItem('chatMessages', JSON.stringify(messages.value));
};

watch(messages, (newMessages) => {
  saveMessages();
}, { deep: true });

// Función para borrar el historial de chat
const clearHistory = async () => {
  try {
    await axios.delete('http://127.0.0.1:8000/chat/clear-messages/');
    messages.value = [];
    localStorage.removeItem('chatMessages');
  } catch (error) {
    console.error('Error clearing chat history:', error);
  }
};

// Función para verificar si una cadena es JSON
const isJsonString = (str) => {
  try {
    const jsonString = str.replace(/'/g, '"').replace(/\bNone\b/g, 'null');
    return Array.isArray(JSON.parse(jsonString));
  } catch (e) {
    return false;
  }
};

// Función para parsear JSON
const parseJson = (str) => {
  let jsonString = str.replace(/'/g, '"').replace(/\bNone\b/g, 'null');
  try {
    return JSON.parse(jsonString);
  } catch (error) {
    console.error('Error parsing JSON:', error.message);
    return [];
  }
};

// Función para obtener encabezados de la tabla
const getTableHeaders = (content) => {
  const jsonArray = parseJson(content);
  const headers = {};
  jsonArray.forEach(obj => {
    Object.keys(obj).forEach(key => {
      headers[key] = true;
    });
  });
  return Object.keys(headers);
};

// Función para obtener filas mostradas
const getDisplayedRows = (content) => {
  const jsonArray = parseJson(content);
  const start = 0;
  const end = Math.min(rowsPerPage, jsonArray.length);
  return jsonArray.slice(start, end);
};

// Función para verificar si hay más filas
const hasMoreRows = (content) => {
  const jsonArray = parseJson(content);
  return jsonArray.length > rowsPerPage;
};

// Función para cargar más filas
const loadMoreRows = (content) => {
  const jsonArray = parseJson(content);
  const start = displayedRows.value.length;
  const end = Math.min(start + rowsPerPage, jsonArray.length);
  displayedRows.value = jsonArray.slice(start, end);
};


// Enviar mensaje del usuario
const submitMessage = async () => {
  if (userInput.value.trim() === '') return;

  const userMessage = {
    id: Date.now() + Math.random().toString(36).substring(2, 9),
    sender: 'You',
    content: userInput.value,
    timestamp: new Date().toISOString(),
    isTyping: false
  };

  messages.value = [...messages.value, userMessage];
  saveMessages(); // Guarda los mensajes después de añadir el mensaje del usuario

  const prompt = userInput.value;
  userInput.value = '';

  isLoading.value = true;

  try {
    const response = await axios.post('http://127.0.0.1:8000/chat/run-script/', { prompt });
    console.log(response)
    const aiMessage = {
      id: response.data.id || Date.now() + Math.random().toString(36).substring(2, 9),
      sender: 'DataWhisper',
      content: response.data.content,
      timestamp: response.data.timestamp || new Date().toISOString(),
      isTyping: false,
      insights: response.data.insights || '',
      cost: response.data.cost || 'N/A',  // Añade el coste aquí
      sql: response.data.sql || 'N/A'
    };

    messages.value = [...messages.value, aiMessage];
    saveMessages(); // Guarda los mensajes después de recibir la respuesta del asistente
  } catch (error) {
    console.error('Error fetching AI response:', error);

    const errorMessage = {
      id: Date.now() + Math.random().toString(36).substring(2, 9),
      sender: 'System',
      content: 'Error en la conexión. No se pudo obtener una respuesta.',
      timestamp: new Date().toISOString(),
      isTyping: false
    };
    messages.value = [...messages.value, errorMessage];
    saveMessages(); // Guarda los mensajes después de recibir el error
  } finally {
    isLoading.value = false; // Asegúrate de que isLoading se establezca a false
    setTimeout(() => {
      const chatList = document.querySelector('.hero-chat-list');
      chatList.scrollTop = chatList.scrollHeight;
    }, 100);
  }
};

// Enviar un insight como consulta
const submitInsight = (description) => {
  userInput.value = description;
  submitMessage();
};

// Formatear timestamp
const formatTimestamp = (timestamp) => {
  if (!timestamp) return '';
  const date = new Date(timestamp);
  return isNaN(date.getTime()) ? 'Invalid Date' : date.toLocaleString();
};

onMounted(() => {
  loadMessages();
});

</script>

<style>

.hero-chat-item-content.system {
  background-color: #ff6e6e33; 
  color: #ff6e6e; 
  border: 1px solid #ff6e6e; 
}


.hero-chat-item-content.system h3 {
  color: #ff6e6e; 
}

.hero-chat-item-content.system p {
  color: #ff6e6e; 
}


.hero-chat-list {
  max-height: 400px;
  overflow-y: auto;
  padding: 10px;
  border-radius: 8px;
  margin-bottom: 10px;
}

.hero-chat-item-content {
  padding: 10px 15px;
  border-radius: 10px;
  max-width: 100%;
  color: #ffffff; 
}

.hero-chat-item-content h3 {
  margin: 0;
  font-size: 14px;
  font-weight: bold;
  color: #a570ff; 
}

.hero-chat-item-content h3 span {
  font-size: 12px;
  color: #bbbbbb; 
}

.hero-chat-item-content table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

.hero-chat-item-content th,
.hero-chat-item-content td {
  border: 1px solid #555;
  padding: 8px;
  text-align: left;
}

.hero-chat-item-content th {
  background-color: #3a3a3a;
  color: #ffffff;
}

.hero-chat-item-content p {
  margin: 10px 0;
  line-height: 1.6;
}


.insights {
  margin-top: 10px;
  
  padding: 10px;
 
}

.insights h4 {
  margin: 0 0 10px 0;
  font-size: 14px;
  color: #ffad66;
}

.insights ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.insights li {
  margin-bottom: 10px;
}

.insights button {
  background-color: #a470ff1a;
  color: #ffffff;
  border: 1px solid #fff;
  padding: 8px 12px;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.insights button:hover {
  background-color: #ff6eb223;
}


.skeleton-loader {
  margin-top: 10px;
}

.skeleton-line {
  background-color: #2b2b2b;
  height: 12px;
  margin: 8px 0;
  border-radius: 4px;
  animation: loading 1.2s infinite ease-in-out;
}

.skeleton-line.short {
  width: 60%;
}

@keyframes loading {
  0% {
    background-color: #333;
  }
  50% {
    background-color: #444;
  }
  100% {
    background-color: #333;
  }
}

.hero-chat-input svg path {
  fill: url(#paint0_linear); 
  
}

.hero-chat-input button {
  background: none;
  
}



.clear-history-btn {
  background-color: transparent;
  border: none;
  margin-left: 10px;
  cursor: pointer;
  display: flex;
  align-items: center;
}

.clear-history-btn svg path {
  stroke: #f2a3b8;
}

.clear-history-btn:hover svg path {
  stroke: #9fc2e9;
}
.cost-info {
  margin-top: 10px;
  font-size: 14px;
  color: #b9f3e5;
}
.sql-info {
  margin-top: 10px;
  
  
  border-radius: 8px;
  color: #9fc2e9; 
  font-family: 'Courier New', Courier, monospace;
  font-size: 14px;
  
  white-space: pre-wrap; 
  word-wrap: break-word; 
}



.sql-info pre {
  margin: 10px 0 0 0;
  color: #e6e6e6; 
  background-color: #2a2a2a; 
  padding: 10px;
  border-radius: 6px;
  overflow-x: auto;
}

</style>
