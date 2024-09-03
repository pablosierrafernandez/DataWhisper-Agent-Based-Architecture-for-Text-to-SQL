<template>
   <div class="hero-area">
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <h1 class="title">
              Transform Your SQL Queries <br />
              <span>with Natural Language!</span>
            </h1>
            <p class="mx-850 text-center">
              Effortlessly convert your SQL queries into natural language with our AI-powered chat assistant. Interact with intelligent agents to get accurate and comprehensive responses based on your data.
            </p>
            <div class="hero-btn">
               <a class='btn btn-primary' href='/configuration'>Configure</a>
              <a class='btn btn-tertiary' href='/about'>How it Works?</a>
             
            </div>
           <ChatComponent/>
          </div>
        </div>
      </div>
    </div>
</template>



<script setup>
import ChatComponent from "/src/components/ChatComponent.vue";
</script>

<style>

</style>