<template>
 <!--=======================================================
                          CONTACT
  =========================================================-->
    <div class="contact-area mtb-192">
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <h2 class="title-2">Connect your <span>Database</span></h2>
          </div>
          <div class="col-md-12 col-lg-6">
            <div class="contact-content">
              <img width="240" height="80" src="/src/assets/img/logo.png" alt="logo" />
              <p>
                Seamlessly connect your database and start querying with natural language. Our system allows you to configure database connections quickly and easily.
              </p>
              
              <h4>Connect your favorite database</h4>
             
              <div class="contact-brand">
  <div class="brand-item" data-tech="MySQL">
    <img src="/src/assets/img/brand/1.png" alt="MySQL" />
    <span class="tooltip">MySQL</span>
  </div>
  <div class="brand-item" data-tech="RDS AWSL">
    <img src="/src/assets/img/brand/2.png" alt="RDS AWS" />
    <span class="tooltip">RDS AWS</span>
  </div>
  <div class="brand-item" data-tech="Microsoft SQL Server">
    <img src="/src/assets/img/brand/3.png" alt="Microsoft SQL Server" />
    <span class="tooltip">Microsoft SQL Server</span>
  </div>
  <div class="brand-item" data-tech="PostgreSQL">
    <img src="/src/assets/img/brand/4.png" alt="PostgreSQL" />
    <span class="tooltip">PostgreSQL</span>
  </div>
  <div class="brand-item" data-tech="SQLite">
    <img src="/src/assets/img/brand/5.png" alt="SQLite" />
    <span class="tooltip">SQLite</span>
  </div>
  <div class="brand-item" data-tech="MariaDB">
    <img src="/src/assets/img/brand/6.png" alt="MariaDB" />
    <span class="tooltip">MariaDB</span>
  </div>
</div>
<p class="text-center mt-4">And more...</p>

            </div>
          </div>
         <div class="col-md-12 col-lg-6">
  <div class="contact-form">
    <h2>Set Up Your Database Connection</h2>
    <p>
      Configure your database connection. Provide the necessary details to establish a secure connection.
    </p>
    <ConfigurationFormComponent/>
  </div>
</div>

        </div>
      </div>
    </div>
    

</template>

<script setup>
import ConfigurationFormComponent from "../components/ConfigurationFormComponent.vue";

</script>

<style scoped>
.contact-brand {
  display: grid;
  grid-template-columns: repeat(3, 1fr); 
  gap: 16px; 
  justify-content: center;
  margin-bottom: 32px; 
}

.brand-item {
  position: relative;
  display: block;
}



.brand-item:hover .tooltip {
  visibility: visible;
  opacity: 1;
}

.brand-item img {
  display: block;
  width: 100px; 
  height: auto;
}

</style>