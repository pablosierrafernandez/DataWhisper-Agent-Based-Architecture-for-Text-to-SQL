<template>
  <form @submit.prevent="submitForm">
    <div class="form-group">
      <!-- Fila 1 -->
      <div class="input-row">
        <div class="input-group">
          <label for="hostname">Hostname*</label>
          <input
            id="hostname"
            type="text"
            v-model="formData.hostname"
            placeholder="Hostname*"
            required
          />
        </div>
        <div class="input-group">
          <label for="database">Database*</label>
          <input
            id="database"
            type="text"
            v-model="formData.database"
            placeholder="Database*"
            required
          />
        </div>
      </div>

      <!-- Fila 2 -->
      <div class="input-row">
        <div class="input-group">
          <label for="username">Username*</label>
          <input
            id="username"
            type="text"
            v-model="formData.username"
            placeholder="Username*"
            required
          />
        </div>
        <div class="input-group">
          <label for="password">Password*</label>
          <input
            id="password"
            type="password"
            v-model="formData.password"
            placeholder="Password*"
            required
          />
        </div>
      </div>

      <!-- Fila 3 -->
      <div class="input-row">
        <div class="input-group">
          <label for="port">Port*</label>
          <input
            id="port"
            type="number"
            v-model="formData.port"
            placeholder="Port*"
            required
          />
        </div>
        <div class="input-group">
          <label for="openai_api_key">OpenAI API Key*</label>
          <input
            id="openai_api_key"
            type="text"
            v-model="formData.openai_api_key"
            placeholder="OpenAI API Key*"
            required
          />
        </div>
      </div>

      <!-- Fila 4 -->
      <div class="input-row">
        <div class="input-group">
          <label for="huggingface_api_key">HuggingFace API Key</label>
          <input
            id="huggingface_api_key"
            type="text"
            v-model="formData.huggingface_api_key"
            placeholder="HuggingFace API Key"
            required
          />
        </div>
        <div class="input-group">
          <label for="model_name">SQL Coder 🤖 <small>ℹ Empty (GPT 3.5)  -  Or url from HuggingFace</small></label> 
          <input
            id="model_name"
            type="text"
            v-model="formData.model_name"
            placeholder="defog/sqlcoder-7b-2"
           
          />
        </div>
         <div class="input-group">
          <label for="num_insights">Number of Insights (0 to 5)</label>
          <input
            id="num_insights"
            type="number"
            v-model="formData.num_insights"
            placeholder="Number of Insights"
            min="0" 
            max="5"   
            required
          />
        </div>
      </div>

      <!-- Fila 5 -->
      <div class="input-row tooltip-container">
        <div class="input-group">
          <label for="option">Option <small>ℹ Disabled (GPT)  -  Active (FAISS)</small>
           
          </label>
          <div class="custom-form-check form-check">
            <input
              class="custom-form-check-input form-check-input"
              type="checkbox"
              v-model="formData.opcion"
              id="option"
            />
          </div>
        </div>
      </div>
    </div>

   
    
    <div v-if="showSuccessMessage" class="alert alert-success" role="alert">
      Configuration saved successfully!
    </div>
    
    <button class="btn btn-primary" type="submit">Submit</button>
  </form>
</template>
<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

// Define the form data object
const formData = ref({
  hostname: '',
  database: '',
  username: '',
  password: '',
  port: null,
  openai_api_key: '',
  huggingface_api_key: '',
  opcion: false,
  num_insights: '',
  model_name:'',
});

// Additional state to handle form submission
const termsAccepted = ref(false);
const showSuccessMessage = ref(false); // State for the success message
// Function to fetch existing configuration
const fetchConfiguration = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/chat/configuration/');
    if (response.data) {
      formData.value = {
        hostname: response.data.hostname || '',
        database: response.data.database || '',
        username: response.data.username || '',
        password: response.data.password || '',
        port: response.data.port || '',
        openai_api_key: response.data.openai_api_key || '',
        // Si huggingface_api_key es null o vacío, lo asignamos como una cadena vacía
        huggingface_api_key: response.data.huggingface_api_key || '', 
        model_name: response.data.model_name || '',
        opcion: response.data.opcion !== undefined ? response.data.opcion : false,
        num_insights: response.data.num_insights ,
      };+
      console.log(response.data.num_insights)
      console.log(response.data.opcion)
    }
  } catch (error) {
    console.error('Error fetching configuration:', error.response.data);
  }
};

// Fetch configuration when component is mounted
onMounted(() => {
  fetchConfiguration();
});

// Function to submit the form
const submitForm = async () => {
  try {
    const response = await axios.put('http://127.0.0.1:8000/chat/configuration/', formData.value);
    console.log('Configuration saved:', response.data);
    showSuccessMessage.value = true; // Show success message
    setTimeout(() => {
      showSuccessMessage.value = false; // Hide success message after 3 seconds
    }, 3000);
  } catch (error) {
    console.error('Error saving configuration:', error.response.data);
  }
};
</script>

<style scoped>

  .form-group {
    margin-bottom: 1.5rem;
  }

  .input-group {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .form-label {
    font-weight: bold;
    margin-bottom: 0.5rem;
  }

  .tooltip {
    display: inline-block;
    margin-left: 8px;
    position: relative;
    cursor: pointer;
  }

  .tooltip::after {
    content: attr(role);
    visibility: hidden;
    width: 200px;
    background-color: #333;
    color: #fff;
    text-align: center;
    border-radius: 5px;
    padding: 5px;
    position: absolute;
    left: 50%;
    bottom: 125%;
    margin-left: -100px;
    opacity: 0;
    transition: opacity 0.3s;
    font-size: 14px;
    z-index: 1;
  }

  .tooltip:hover::after {
    visibility: visible;
    opacity: 1;
  }

  .form-check-label a {
    color: #007bff;
    text-decoration: none;
  }

  .form-check-label a:hover {
    text-decoration: underline;
  }

.alert-success {
  margin-top: 15px;
  font-size: 16px;
  text-align: center;
}
.custom-form-check {
  display: flex;
  align-items: center;
  margin-top: 15px;
}

.custom-form-check-input {
  width: 20px;
  height: 20px;
  background-color: #f1f1f1;
  border-radius: 4px;
  border: 1px solid #ddd;
  transition: all 0.3s ease;
  cursor: pointer;
}

.custom-form-check-input:checked {
  background-color: #007bff;
  border-color: #007bff;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

.custom-form-check-input:focus {
  outline: none;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

.custom-form-check-label {
  margin-left: 10px;
  font-size: 16px;
  color: #333;
  cursor: pointer;
  transition: color 0.3s ease;
}

.custom-form-check-label:hover {
  color: #007bff;
}
.input-group {
  margin-bottom: 1rem;
}

.info-icon {
  position: relative;
  display: inline-block;
  cursor: pointer;
  margin-left: 0.5rem;
}

.info-icon i {
  color: #007bff;
}

.tooltip-container .tooltip {
  visibility: hidden;
 
  background-color: #333; 
  color: #fff; 
  text-align: center;
  border-radius: 5px; 
  padding: 5px 10px;
  position: absolute;
  z-index: 1;
  bottom: 125%; 
  left: 50%;
  margin-left: -75px; 
  opacity: 0;
  transition: opacity 0.3s;
  font-size: 14px;
  white-space: nowrap; 
}

.info-icon:hover .tooltip {
  visibility: visible;
  opacity: 1;
}

.form-check-input {
  margin-right: 0.5rem;
}

.custom-form-check-input {
  margin-right: 0.5rem;
}
.small, small {
    font-size: 0.575em;
    background: #4f007c;
    padding: 6px;
    border-radius: 10px;
}
</style>
