<template>
  
    <!--=======================================================
                          FEATURE
  =========================================================-->
 <div class="feature-area mt-192">
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <h2 class="title-2">
          Simplify Your SQL Queries <span>with AI-Powered Assistance</span>
        </h2>
      </div>
    </div>
    <div class="row gy-4">
      <div class="col-md-4">
        <div class="feature-item">
          <img src="/src/assets/img/icon/27.svg" alt="icon" />
          <h3>Human-Like Query Parsing</h3>
          <p>
            Translate natural language questions into accurate SQL queries,
            enabling quick access to the data you need without complex syntax.
          </p>
        </div>
      </div>
      <div class="col-md-4">
        <div class="feature-item">
          <img src="/src/assets/img/icon/2.svg" alt="icon" />
          <h3>Seamless Database Integration</h3>
          <p>
            Effortlessly connect to multiple databases, allowing the assistant
            to pull data from various sources for comprehensive analysis.
          </p>
        </div>
      </div>
      <div class="col-md-4">
        <div class="feature-item">
          <img src="/src/assets/img/icon/3.svg" alt="icon" />
          <h3>AI-Powered Insights</h3>
          <p>
            Leverage AI to automatically generate insights and reports, helping
            you make informed decisions with minimal effort.
          </p>
        </div>
      </div>
    </div>
  </div>
</div>

    <!--=======================================================
                          SOLUTION
  =========================================================-->
    <div class="solution-area mtb-192">
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <h2 class="title-2">
              Your AI-Driven SQL Query <span>Automation Solution</span>
            </h2>
          </div>
          <div class="col-md-12">
            <div class="solution-item">
              <div class="row align-items-center">
                <div class="col-md-6 pr-47">
                  <img src="/src/assets/img/solution2.svg" alt="solution" />
                </div>
                <div class="col-md-6 pl-47">
                   <h3>🤝 Multi-Agent Collaboration</h3>
                  <p>
                Harness the power of multiple intelligent agents working together to automate SQL query generation, execution, and analysis. Each agent specializes in different tasks, ensuring accuracy and efficiency.
              </p>
                  <a target="_blank" class='btn btn-secondary' href='https://github.com/pablosierrafernandez'>Learn more</a
                  >
                </div>
              </div>
            </div>
            <div class="solution-item">
              <div class="row align-items-center">
                <div class="col-md-6 pr-47">
                  <h3>🚀 Insights Generation</h3>
                   <p>
                Automatically generate additional SQL queries to uncover deeper insights from your data, maximizing the value of your database interactions.
              </p>
                  
                </div>
                <div class="col-md-6 pl-47 mt-30">
                  <div class="solution-item-list">
                    <div class="solution-single">
                      <img src="/src/assets/img/check.svg" alt="check" />
                      <div>
                         <h4>Automatic Table Selection</h4>
                        <p>
                      The system identifies relevant tables for your query either through intelligent agents or using semantic approximation techniques.
                    </p>
                      </div>
                    </div>
                    <div class="solution-single">
                      <img src="/src/assets/img/check.svg" alt="check" />
                      <div>
                        <h4>Iterative Query Refinement</h4>
                        <p>
                      Agents collaborate to refine and correct queries, ensuring successful execution even in the face of errors or empty results.
                    </p>
                      </div>
                    </div>
                    <div class="solution-single">
                      <img src="/src/assets/img/check.svg" alt="check" />
                      <div>
                         <h4>Cost-Efficient Operations</h4>
                         <p>
                      Track and optimize the costs of AI operations by monitoring token usage, ensuring that your resources are used effectively.
                    </p>
                      </div>
                    </div>
                    <div class="solution-single">
                      <img src="/src/assets/img/check.svg" alt="check" />
                      <div>
                        <h4>Adaptive Query Relevance</h4>
                        <p>
                      Our system intelligently assesses the relevance of user prompts for SQL queries. Only the most pertinent prompts trigger database interactions, optimizing performance and reducing unnecessary costs.
                    </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
           <div class="solution-item">
    <div class="row align-items-center">
        <div class="col-md-6 pr-47">
            <div class="hero-chat-list">
                <!-- Mensajes del chat -->
                <div class="hero-chat-item">
                    
                    <div class="hero-chat-item-content">
                        <h3>😊 You <span>28/8/2024, 13:21:23</span></h3>
                        <!-- Mostrar tabla si el contenido es JSON, sino mostrar texto -->
                        <p>¿Quien es el usuario que más ha gastado?</p>
                        <!-- Mostrar coste si está disponible -->
                        <!--v-if-->
                        <!-- Mostrar insights si existen -->
                        <!--v-if-->
                    </div>
                </div>
                <div class="hero-chat-item">
                    
                    <div class="hero-chat-item-content">
                        <h3>🤖 DataWhisper <span>28/8/2024, 13:21:37</span></h3>
                        <!-- Mostrar tabla si el contenido es JSON, sino mostrar texto -->
                        <div>
                            <table>
                                <thead>
                                    <tr>
                                        <th>FirstName</th>
                                        <th>LastName</th>
                                        <th>TotalSpent</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>Helena</td>
                                        <td>Holý</td>
                                        <td>49.62</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <!-- Mostrar coste si está disponible -->
                        <div class="cost-info">
                            <strong>Cost:</strong> 0.002798
                        </div>
                        <!-- Mostrar insights si existen -->
                        <div class="insights">
                            <h4>Recommendations:</h4>
                            <ul>
                                <li>
                                    <button>Una consulta que tiene como objetivo descubrir en qué ciudad viven la mayoría de los clientes que más gastan.</button>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <!-- Skeleton Loader Manual -->
                <!--v-if-->
            </div>
        </div>
       <div class="col-md-6 pl-47 mt-30">
    <h3>👀 Intuitive and User-Friendly</h3>
    <p>
        Our system offers a seamless and user-friendly interface, making data analysis more accessible 
        than ever. No need for deep technical knowledge—simply input your query, and our intelligent 
        agents handle the rest, as demonstrated in the example on the left.
    </p>
    <p>
        Whether you're looking to extract insights, run complex queries, or just get quick answers, 
        our intuitive design ensures that anyone on your team can easily navigate and use the platform 
        to its full potential.
    </p>
    
</div>

    </div>
</div>

            
          </div>
        </div>
      </div>
    </div>
   
 
</template>
