# **DataWhisper Arquitectura Basada En Agentes Para** _**Text-to-SQL**_







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

## Índice

1.  [Introducción](#introducci%C3%B3n)
2.  [Objetivo](#objetivo)
3.  [Características](#caracter%C3%ADsticas)
4.  [Arquitectura](#arquitectura)
    *   [Agente Proxy (Evaluador de NLQ)](#agente-proxy-evaluador-de-nlq)
    *   [Agente Selector (Selección de Tablas)](#agente-selector-selecci%C3%B3n-de-tablas)
    *   [Agentes Analistas (Iteración y Corrección)](#agentes-analistas-iteraci%C3%B3n-y-correcci%C3%B3n)
    *   [Agente Explorer (Generador de Insights)](#agente-explorer-generador-de-insights)
5.  [Requisitos](#requisitos)
6.  [Aplicación](#aplicaci%C3%B3n)
    *   [Backend en Django](#backend-en-django)
    *   [Frontend en Vue.js con Vite](#frontend-en-vuejs-con-vite)
7.  [Instrucciones de Uso](#instrucciones-de-uso)
    *   [Manual (sin Docker)](#manual-sin-docker)
    *   [Automático](#autom%C3%A1tico)
8.  [Contribución](#contribuci%C3%B3n)
9.  [Licencia](#licencia)
10.  [Autores](#autores)

## Introducción

La necesidad de sistemas que permitan a los usuarios sin conocimientos técnicos generar consultas SQL precisas es cada vez más crítica en la era de los datos. Aunque SQL es un lenguaje poderoso y versátil, su uso requiere un entendimiento profundo de las estructuras de datos y las relaciones entre tablas en una base de datos. Este requisito técnico ha sido una barrera para muchos usuarios que necesitan acceder a la información contenida en bases de datos.

Este proyecto aborda este problema desarrollando un sistema que traduce consultas en lenguaje natural a SQL utilizando una arquitectura de agentes inteligentes. Estos agentes trabajan de manera coordinada para identificar las tablas relevantes, generar consultas SQL, ejecutar las consultas y, finalmente, proporcionar _insights_ adicionales basados en los resultados obtenidos. 
<p align="center">
  <img src="https://github.com/user-attachments/assets/85066ab8-e053-4342-9b99-012882a89335"/>
</p>

**Figura 1:** Interfaz Web - DataWhisper

## Objetivo

El objetivo principal de este proyecto es transformar la forma en que los usuarios interactúan con las bases de datos relacionales, facilitando la generación, evaluación y ejecución de consultas SQL a partir de entradas en lenguaje natural. Este sistema está diseñado para reducir las barreras técnicas, mejorar la accesibilidad para usuarios no técnicos y proporcionar una solución eficiente para la gestión y análisis de datos.

## Características

1.  **Facilita la interacción con bases de datos**: Permite a los usuarios generar consultas SQL precisas y optimizadas utilizando lenguaje natural, sin necesidad de conocimientos técnicos avanzados en SQL.
2.  **Implementa un sistema multi-agente**: Arquitectura de agentes inteligentes que colaboran para llevar a cabo tareas específicas dentro del proceso de generación de consultas SQL, como la selección de tablas, la generación de consultas, la iteración y corrección de errores, y la generación de _insights_.
3.  **Interfaz web accesible y fácil de usar**: Permite a los usuarios interactuar con el sistema de manera intuitiva, incluyendo la generación de consultas SQL, la visualización de resultados y la configuración de preferencias personalizadas.
4.  **Optimización y reducción de los costos**: Permite seleccionar los modelos para optimizar los recursos según el caso que se desee.
5.  **Garantiza la seguridad y la integridad de la base de datos**: Implementa medidas de seguridad efectivas contra ataques como la inyección de comandos o _prompt injection_, protegiendo la integridad de la base de datos.

## Arquitectura

La arquitectura del sistema se compone de varios agentes inteligentes, cada uno de los cuales está diseñado para realizar tareas específicas en el proceso de generación y ejecución de consultas SQL. Estos agentes trabajan de manera colaborativa bajo la supervisión de un orquestador que asegura la correcta secuencialidad y coordinación de las tareas.

![Architecture (1)](https://github.com/user-attachments/assets/d6120b71-354c-4245-9f60-4e1543437681)

**Figura 2:** Arquitectura

### Agente Proxy (Evaluador de NLQ)

El Agente Proxy es el primer componente del sistema que interactúa con las consultas en lenguaje natural (NLQ) proporcionadas por el usuario. Su función principal es evaluar la relevancia de estas consultas para determinar si son aptas para ser traducidas a SQL. Este agente utiliza un modelo de lenguaje avanzado (GPT-3.5) para clasificar las consultas en una escala del 1 al 5, donde 1 indica irrelevancia total y 5 máxima relevancia.

La implementación del Agente Proxy ha demostrado una tasa de precisión del 95%.

### Agente Selector (Selección de Tablas)

Una vez que el Agente Proxy ha identificado una consulta relevante, el siguiente paso en el proceso es la selección de tablas, que es realizada por el Agente Selector. Este agente tiene la responsabilidad de identificar las tablas de la base de datos que son más relevantes para la consulta SQL que se va a generar.

El Agente Selector emplea dos enfoques distintos para llevar a cabo esta tarea:

1.  **Enfoque basado en modelo de lenguaje avanzado (Opción 1)**: Este enfoque utiliza un modelo de lenguaje, como GPT-3.5, para identificar las tablas más relevantes basándose en la entrada proporcionada por el usuario. Este método es altamente preciso pero también más costoso en términos de procesamiento y uso de recursos.
2.  **Enfoque semántico con cercanía por coseno (Opción 2)**: Este enfoque combina técnicas de procesamiento semántico con la cercanía por coseno para identificar las tablas relevantes. Aunque es menos costoso y más rápido que el enfoque basado en modelos de lenguaje, puede no ser tan preciso en todos los casos ya que siempre devolverá `k` tablas relevantes y puede haber casos en los que se necesiten más de `k` tablas.

Ambos enfoques han demostrado ser efectivos en la identificación de tablas, con resultados comparables en las pruebas realizadas. La elección entre estos dos enfoques dependerá de las necesidades específicas del usuario, incluyendo factores como el costo, el tiempo de ejecución, precisión, complejidad de la consulta o el número de tablas en la base de datos.

### Agentes Analistas (Iteración y Corrección)

Una vez que las tablas relevantes han sido seleccionadas, el siguiente paso es la generación y ejecución de la consulta SQL. Este proceso es realizado por un equipo de agentes analistas, que incluyen:

1.  _**Data Engineer Agent**_ **(**_**SQL Coder**_**)**: Este agente es responsable de la generación inicial de la consulta SQL basándose en las especificaciones proporcionadas por el usuario y las tablas seleccionadas. El agente se asegura de que la consulta generada esté estructurada correctamente y no contenga errores básicos de sintaxis o referencias incorrectas.
2.  _**Sr Data Analyst Agent**_: Este agente ejecuta la consulta SQL generada por el _Data Engineer Agent_ y verifica su corrección. Si se detectan errores, como resultados inesperados o vacíos, el _Sr Data Analyst Agent_ inicia un proceso iterativo de corrección, enviando _feedback_ al _Data Engineer Agent_ para ajustar la consulta hasta que se obtenga un resultado correcto.

El proceso iterativo de corrección ha demostrado ser altamente efectivo, alcanzando una precisión del 95% después de dos iteraciones en las pruebas realizadas. 

> El modelo del agente **Data Engineer Agent (SQL Coder)** puede ser cambiado desde la GUI.
> 
> Admite modelos **pequeños** alojados en HuggingFace.
> 
> Por defecto, si no se aplica ningún modelo usará GPT 3.5.

### Agente Explorer (Generador de _Insights_)

Además de generar y ejecutar consultas SQL, el sistema también incluye un Agente Explorer, cuyo objetivo es generar _insights_ adicionales a partir de los resultados obtenidos. Este agente utiliza un modelo de lenguaje avanzado (GPT-4 en las pruebas realizadas) para identificar patrones y tendencias en los datos que pueden no ser evidentes en la consulta original.

El Agente Explorer genera nuevas consultas SQL basadas en la consulta original y proporciona _insights_ que pueden ser de gran valor para el usuario. 

Aunque el uso del Agente Explorer puede incrementar significativamente el costo de la operación (especialmente al utilizar modelos avanzados como GPT-4), también ofrece un valor añadido considerable al proporcionar información adicional. Para reducir los costos, se recomienda el uso de modelos menos costosos como GPT-3 para este agente, dependiendo de las necesidades específicas del proyecto.

> La generación de insights puede ser desactivada desde la GUI.

## Requisitos

Para acceder a los modelos de lenguaje utilizados en el sistema, se requiere una clave API de OpenAI. Esta clave API es necesaria para autenticar las solicitudes a la API de OpenAI y permitir el uso de modelos como GPT-3.5 y GPT-4.

Para poner otros modelos necesitarás la clave API de HuggingFace (opcional) pero la necesitarás para la Opción 2 de selección de tablas.

## Aplicación

La interfaz de usuario ha sido diseñada con un enfoque en la usabilidad y accesibilidad, permitiendo a los usuarios interactuar con el sistema de manera fluida y eficiente. La aplicación web se ha desarrollado utilizando Django para el backend y Vue.js con Vite para el frontend, lo que proporciona una arquitectura moderna y reactiva.

### Backend en Django

El _backend_, desarrollado en Django, gestiona las interacciones con la base de datos y los modelos de lenguaje. Utiliza Django REST Framework para exponer las APIs necesarias que interactúan con los agentes y procesan las consultas del usuario.

### Frontend en Vue.js con Vite

El _frontend_ ha sido desarrollado utilizando Vue.js, un _framework_ progresivo de JavaScript que facilita la construcción de interfaces de usuario interactivas. Vite, una herramienta de compilación rápida, se ha utilizado para optimizar el desarrollo del frontend, proporcionando una experiencia de desarrollo más ágil y eficiente.

La interfaz incluye varias páginas y componentes clave:

*   **Página de Chat**: Permite introducir consultas en lenguaje natural y ver las respuestas generadas.
*   **Página de Configuración**: Ofrece opciones para personalizar el comportamiento del sistema y la conexión a la base de datos.

## Instrucciones de Uso

### Manual (sin Docker)

Para utilizar el sistema, siga los pasos a continuación:

1.  **Clonar el repositorio**
    
    ```bash
    git clone https://github.com/pablosierrafernandez/DataWhisper-Arquitectura-basada-en-Agentes-para-text-to-sql.git
    ```
    
2.  **Configurar el** _**backend**_
    1.  Entorno Virtual
        
        ```bash
        cd DataWhisper-Arquitectura-basada-en-Agentes-para-text-to-sql
        cd back
        python -m venv env . # crear entorno virtual
        source env/bin/activate  # Linux/MacOS
        source env\Scripts\activate  # Windows
        pip install -r requirements.txt
        ```
        
    2.  Migraciones
        
        ```bash
        # en back/
        python manage.py migrate
        ```
        
3.  **Configurar el frontend**
    
    Deberás tener instalado [Node.js](https://nodejs.org/en) de antemano
    
    ```bash
    # en front
    npm install
    ```
    
4.  **Levantar los servicios**
    
    ```bash
    # en back
    python manage.py runserver
    ```
    
    ```bash
    # en front
    npm run dev
    ```
    
5.  **Acceder a la aplicación** 
    
    Abre el navegador y ve a `http://localhost:5173` para acceder a la interfaz de usuario.
    

### Automático

1.  **Clonar el repositorio**
    
    ```bash
    git clone https://github.com/pablosierrafernandez/DataWhisper-Arquitectura-basada-en-Agentes-para-text-to-sql.git
    ```
    
2.  **Levantar los contenedores**
    
    Deberás tener instalado [Docker y Docker Compose](https://www.docker.com/).
    
    ```bash
    docker-compose up --build
    ```
    
3.  **Acceder a la aplicación**: 
    
    Abre el navegador y ve a `http://localhost:5173` para acceder a la interfaz de usuario.
    

## Contribución

Las contribuciones son bienvenidas. Si tienes sugerencias de mejoras, nuevas funcionalidades o encuentra algún problema, por favor abre un _issue_ o envía un _pull request_.

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).  
Consulta el archivo `LICENSE` para más detalles.

## Autores

*   [@pablosierrafernandez](https://github.com/pablosierrafernandez): Investigador y desarrollador del proyecto.

En colaboración con:

| Logo | Entidad | Descripción |
| --- | --- | --- |
| ![urv-centrat-color (1)](https://github.com/user-attachments/assets/90bda3f7-7e0f-4e4e-908b-238c6f85c3a7) | [Universitat Rovira i Virgili](https://www.urv.cat) | Institución de educación superior ubicada en Tarragona, España, conocida por su excelencia académica e investigación multidisciplinaria. |
