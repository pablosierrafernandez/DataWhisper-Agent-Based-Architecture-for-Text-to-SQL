<template>
  <footer>
    <div class="container">
      <div class="row gy-4">
        <div class="col-md-6">
          <img width="240" height="80" src="/src/assets/img/logo.png" alt="logo" />
          <p>
            Simplify your SQL queries with our AI-driven chat. Transform complex queries into natural language effortlessly.
          </p>
        </div>
        <div class="col-md-6">
          <div class="row gy-4">
            <div class="col-md-6">
              <div class="footer-item">
                <h2>Explore</h2>
                <ul>
                  <li><a href="/">Home</a></li>
                  <li><a href="/about">About Us</a></li>
                  <li><a href="/configuration">Configuration</a></li>
                </ul>
              </div>
            </div>
            <div class="col-md-6">
              <div class="footer-item">
                <h2>Connect</h2>
                <ul>
                  <li><a target="_blank" href="https://www.linkedin.com/in/pablo-sierra-fernandez/">LinkedIn</a></li>
                  <li><a  target="_blank" href="https://github.com/pablosierrafernandez">Github</a></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-copyright">
      <div class="container">
        <div class="row gy-2">
          <div class="col-md-12 text-center">
            <p>© 2023 Assistify. All rights reserved.</p>
          </div>
         
        </div>
      </div>
    </div>
  </footer>
</template>

<style>
  footer {
    background-color: #1f1f1f73;
    color: #ffffff;
    padding: 2rem 0;
  }

  .footer-item h2 {
    font-size: 1.2rem;
    margin-bottom: 1rem;
    color: #ffffff;
  }

  .footer-item ul {
    list-style: none;
    padding: 0;
  }

  .footer-item ul li {
    margin-bottom: 0.5rem;
  }

  .footer-item ul li a {
    color: #23d9b7;
    text-decoration: none;
  }

  .footer-item ul li a:hover {
    text-decoration: underline;
  }

  .footer-copyright {
    background-color: #1414142f;
    padding: 1rem 0;
  }

  .footer-copyright p {
    margin: 0;
  }

 



  .footer-copyright ul li a {
    color: #23d9b7;
    text-decoration: none;
  }

  .footer-copyright ul li a:hover {
    text-decoration: underline;
  }
</style>
