<template>
  
      <header>
        <div class="desktop-header">
          <div class="container-fluid">
            <div class="row align-items-center">
              <div class="col-md-2">
                <a href="/"><img width="240" height="80" src="/src/assets/img/logo.png" alt="logo" /></a>
              </div>
              <div class="col-md-8">
                <nav>
                  <ul>
                    <li><router-link class="btn btn-secondary" to="/">🤖 Chat</router-link></li>
                     <li><router-link to="/about">🤔 How it Works</router-link></li>
                   
                  </ul>
                </nav>
              </div>
              <div class="col-md-2 text-end">
                 <router-link to="/configuration" class="btn btn-secondary">
        🛠 Configuration 
    </router-link>
               
              </div>
            </div>
          </div>
        </div>
        <div class="mobile-header">
          <a href="/"><img width="240" height="80" src="/src/assets/img/logo.png" alt="logo" /></a>
          <span class="mobile-menu-open-icon">
            <svg
              width="800px"
              height="800px"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <g>
                <path
                  id="Vector"
                  d="M12 17H19M5 12H19M5 7H19"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </g>
            </svg>
          </span>
          <div class="mobile-menu">
            <strong class="mobile-menu-close-icon">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-x-circle-fill"
                viewBox="0 0 16 16"
              >
                <path
                  d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293z"
                />
              </svg>
            </strong>
            <nav>
              <ul>
                <li><router-link to="/">Chat</router-link></li>
                     <li><router-link to="/about">About</router-link></li>
              </ul>
            </nav>
             <router-link to="/configuration" class="btn btn-secondary">
        Configuration
    </router-link>
          </div>
        </div>
      </header>
    
</template>

<script setup>

</script>

<style>

</style>