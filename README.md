# DataWhisper: Agent-Based Architecture for *Text-to-SQL*







![DataWhisper Arquitectura Basada En Agentes Para Text-to-SQL-1](https://github.com/user-attachments/assets/1a5a38e9-787d-41c8-8ca2-1cc049999060)
![DataWhisper Arquitectura Basada En Agentes Para Text-to-SQL-2](https://github.com/user-attachments/assets/48ca4772-abc6-459c-8fd8-742ff3710093)
![DataWhisper Arquitectura Basada En Agentes Para Text-to-SQL-3](https://github.com/user-attachments/assets/b691e454-ed81-44e5-aac0-51a83edec02c)
![DataWhisper Arquitectura Basada En Agentes Para Text-to-SQL-4](https://github.com/user-attachments/assets/74c1ff0b-019c-4791-9965-dcdbe803be6e)
![DataWhisper Arquitectura Basada En Agentes Para Text-to-SQL-5](https://github.com/user-attachments/assets/e05e7300-865d-4e7f-83ad-185d568ce39a)
![DataWhisper Arquitectura Basada En Agentes Para Text-to-SQL-6](https://github.com/user-attachments/assets/96d7113e-41df-4b35-b58a-e6ae96116ccb)
![DataWhisper Arquitectura Basada En Agentes Para Text-to-SQL-7](https://github.com/user-attachments/assets/079de604-92ec-4fbc-a0ab-64933064775a)
![DataWhisper Arquitectura Basada En Agentes Para Text-to-SQL-8](https://github.com/user-attachments/assets/99e8e21f-ec0c-420f-b5be-501c9ea70d36)
![DataWhisper Arquitectura Basada En Agentes Para Text-to-SQL-9](https://github.com/user-attachments/assets/4723d8a0-861d-4e5c-93ee-6ddec1a2c7f5)
![DataWhisper Arquitectura Basada En Agentes Para Text-to-SQL-10](https://github.com/user-attachments/assets/a5d89edd-a6b0-41f3-aefb-a30b652a1687)
![DataWhisper Arquitectura Basada En Agentes Para Text-to-SQL-11](https://github.com/user-attachments/assets/b395415e-dfac-483e-bf72-357ac50cd31a)
![DataWhisper Arquitectura Basada En Agentes Para Text-to-SQL-12](https://github.com/user-attachments/assets/a1ce491b-0df8-4a22-b71b-2f8a1e9bd1fb)


https://github.com/user-attachments/assets/052d7e0c-c3a0-42be-b2a5-287801852849

![](https://img.shields.io/badge/URV-Universitat_Rovira_i_Virgili-red)

Here's the translation to English:

Here's the translation to English:

## Index

1.  [Introduction](#introduction)
2.  [Objective](#objective)
3.  [Features](#features)
4.  [Architecture](#architecture)
    *   [Proxy Agent (NLQ Evaluator)](#proxy-agent-nlq-evaluator)
    *   [Selector Agent (Table Selection)](#selector-agent-table-selection)
    *   [Analyst Agents (Iteration and Correction)](#analyst-agents-iteration-and-correction)
    *   [Explorer Agent (Insights Generator)](#explorer-agent-insights-generator)
5.  [Requirements](#requirements)
6.  [Application](#application)
    *   [Backend in Django](#backend-in-django)
    *   [Frontend in Vue.js with Vite](#frontend-in-vuejs-with-vite)
7.  [Usage Instructions](#usage-instructions)
    *   [Manual (without Docker)](#manual-without-docker)
    *   [Automatic](#automatic)
8.  [Contribution](#contribution)
9.  [License](#license)
10.  [Authors](#authors)

## Introduction

The need for systems that allow users without technical knowledge to generate accurate SQL queries is becoming increasingly critical in the data era. While SQL is a powerful and versatile language, its use requires a deep understanding of data structures and relationships between tables in a database. This technical requirement has been a barrier for many users who need access to the information stored in databases.

This project addresses this problem by developing a system that translates natural language queries into SQL using an intelligent agent-based architecture. These agents work in coordination to identify relevant tables, generate SQL queries, execute the queries, and ultimately provide additional insights based on the obtained results. 
<p align="center">
  <img src="https://github.com/user-attachments/assets/85066ab8-e053-4342-9b99-012882a89335"/>
</p>

**Figure 1:** Web Interface - DataWhisper

## Objective

The primary goal of this project is to transform how users interact with relational databases, facilitating the generation, evaluation, and execution of SQL queries from natural language inputs. This system is designed to reduce technical barriers, improve accessibility for non-technical users, and provide an efficient solution for data management and analysis.

## Features

1.  **Facilitates interaction with databases**: Allows users to generate precise and optimized SQL queries using natural language, without needing advanced technical knowledge of SQL.
2.  **Implements a multi-agent system**: An architecture of intelligent agents that collaborate to perform specific tasks within the SQL query generation process, such as table selection, query generation, error iteration and correction, and the generation of insights.
3.  **Accessible and user-friendly web interface**: Allows users to interact with the system intuitively, including generating SQL queries, viewing results, and configuring personalized preferences.
4.  **Optimization and cost reduction**: Allows users to select models to optimize resources based on the specific use case.
5.  **Ensures database security and integrity**: Implements effective security measures against attacks like command or prompt injection, protecting the database's integrity.

## Architecture

The system's architecture is composed of several intelligent agents, each designed to perform specific tasks in the SQL query generation and execution process. These agents work collaboratively under the supervision of an orchestrator that ensures the correct sequence and coordination of tasks.

![Architecture (1)](https://github.com/user-attachments/assets/d6120b71-354c-4245-9f60-4e1543437681)

**Figure 2:** Architecture

### Proxy Agent (NLQ Evaluator)

The Proxy Agent is the first system component that interacts with the user's natural language queries (NLQ). Its primary function is to evaluate the relevance of these queries to determine if they are suitable for translation into SQL. This agent uses an advanced language model (GPT-3.5) to classify queries on a scale of 1 to 5, where 1 indicates total irrelevance and 5 indicates maximum relevance.

The Proxy Agent implementation has demonstrated a 95% accuracy rate.

### Selector Agent (Table Selection)

Once the Proxy Agent has identified a relevant query, the next step in the process is table selection, which is performed by the Selector Agent. This agent is responsible for identifying the database tables most relevant to the SQL query being generated.

The Selector Agent employs two distinct approaches to accomplish this task:

1.  **Language model-based approach (Option 1)**: This approach uses a language model, like GPT-3.5, to identify the most relevant tables based on the user's input. This method is highly accurate but also more costly in terms of processing and resource usage.
2.  **Semantic approach with cosine similarity (Option 2)**: This approach combines semantic processing techniques with cosine similarity to identify relevant tables. Although it is less costly and faster than the language model-based approach, it may not be as accurate in all cases since it will always return `k` relevant tables, and there may be cases where more than `k` tables are needed.

Both approaches have proven effective in table identification, with comparable results in tests. The choice between these two approaches will depend on the user's specific needs, including factors like cost, execution time, accuracy, query complexity, or the number of tables in the database.

### Analyst Agents (Iteration and Correction)

Once the relevant tables have been selected, the next step is SQL query generation and execution. This process is carried out by a team of analyst agents, which include:

1.  _**Data Engineer Agent**_ **(**_**SQL Coder**_**)**: This agent is responsible for the initial SQL query generation based on the user's specifications and the selected tables. The agent ensures that the generated query is correctly structured and free of basic syntax errors or incorrect references.
2.  _**Sr Data Analyst Agent**_: This agent executes the SQL query generated by the _Data Engineer Agent_ and verifies its correctness. If errors are detected, such as unexpected or empty results, the _Sr Data Analyst Agent_ initiates an iterative correction process, sending feedback to the _Data Engineer Agent_ to adjust the query until a correct result is obtained.

The iterative correction process has proven highly effective, reaching 95% accuracy after two iterations in tests conducted. 

> The **Data Engineer Agent (SQL Coder)** model can be changed from the GUI.
> 
> It supports **small** models hosted on HuggingFace.
> 
> By default, if no model is applied, it will use GPT 3.5.

### Explorer Agent (Insights Generator)

In addition to generating and executing SQL queries, the system also includes an Explorer Agent, whose goal is to generate additional insights from the obtained results. This agent uses an advanced language model (GPT-4 in tests) to identify patterns and trends in the data that may not be evident in the original query.

The Explorer Agent generates new SQL queries based on the original query and provides insights that can be of great value to the user. 

While using the Explorer Agent may significantly increase operational costs (especially when using advanced models like GPT-4), it also offers considerable added value by providing additional information. To reduce costs, it is recommended to use less expensive models like GPT-3 for this agent, depending on the project's specific needs.

> Insight generation can be disabled from the GUI.

## Requirements

To access the language models used in the system, an OpenAI API key is required. This API key is necessary to authenticate requests to the OpenAI API and enable the use of models like GPT-3.5 and GPT-4.

For other models, you'll need the HuggingFace API key (optional), but you'll need it for Option 2 of table selection.

## Application

The user interface is designed with a focus on usability and accessibility, allowing users to interact with the system smoothly and efficiently. The web application has been developed using Django for the backend and Vue.js with Vite for the frontend, providing a modern and reactive architecture.

### Backend in Django

The backend, developed in Django, handles interactions with the database and language models. It uses Django REST Framework to expose the necessary APIs that interact with the agents and process user queries.

### Frontend in Vue.js with Vite

The frontend has been developed using Vue.js, a progressive JavaScript framework that facilitates building interactive user interfaces. Vite, a fast build tool, has been used to optimize frontend development, providing a more agile and efficient development experience.

The interface includes several key pages and components:

*   **Chat Page**: Allows users to input natural language queries and view generated responses.
*   **Settings Page**: Offers options to customize the system's behavior and database connection.

## Usage Instructions

### Manual (without Docker)

To use the system, follow the steps below:

1.  **Clone the repository**
    
    ```bash
    git clone https://github.com/pablosierrafernandez/DataWhisper-Arquitectura-basada-en-Agentes-para-text-to-sql.git
    ```
    
2.  **Set up the backend**
    1.  Virtual Environment
        
        ```bash
        cd DataWhisper-Arquitectura-basada-en-Agentes-para-text-to-sql
        cd back
        python -m venv env . # create virtual environment
        source env/bin/activate  # Linux/MacOS
        source env\Scripts\activate  # Windows
        pip install -r requirements.txt
        ```
        
    2.  Migrations
        
        ```bash
        # in back/
        python manage.py migrate
        ```
        
3.  **Set up the frontend**
    
    You need to have [Node.js](https://nodejs.org/en) installed beforehand
    
    ```bash
    # in front
    npm install
    ```
    
4.  **Start the services**
    
    ```bash
    # in back
    python manage.py runserver
    ```
    
    ```bash
    # in front
    npm run dev
    ```
    
5.  **Access the application** 
    
    Open your browser and go to `http://localhost:5173` to access the user interface.
    

### Automatic

1.  **Clone the repository**
    
    ```bash
    git clone https://github.com/pablosierrafernandez/DataWhisper-Arquitectura-basada-en-Agentes-para-text-to-sql.git
    ```
    
2.  **Start the containers**
    
    You should have [Docker and Docker Compose](https://www.docker.com/) installed.
    
    ```bash
    docker-compose up --build
    ```
    
3.  **Access the application**: 
    
    Open your browser and go to `http://localhost:5173` to access the user interface.
    

## Contribution

Contributions are welcome. If you have suggestions for improvements, new features, or find any issues, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).  
Check the `LICENSE` file for more details.

## Authors

*   [@pablosierrafernandez](https://github.com/pablosierrafernandez): Project researcher and developer.

In collaboration with:

| Logo | Entity | Description |
| --- | --- | --- |
| ![urv-centrat-color (1)](https://github.com/user-attachments/assets/90bda3f7-7e0f-4e4e-908b-238c6f85c3a7) | [Universitat Rovira i Virgili](https://www.urv.cat) | A higher education institution located in Tarragona, Spain, known for its academic excellence and multidisciplinary research. |
