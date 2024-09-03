## **DataWhisper Arquitectura Basada En Agentes Para** _**Text-to-SQL**_

![](https://img.shields.io/badge/URV-Universitat_Rovira_i_Virgili-red)

### Índice

### Introducción

La necesidad de sistemas que permitan a los usuarios sin conocimientos técnicos generar consultas SQL precisas es cada vez más crítica en la era de los datos. Aunque SQL es un lenguaje poderoso y versátil, su uso requiere un entendimiento profundo de las estructuras de datos y las relaciones entre tablas en una base de datos. Este requisito técnico ha sido una barrera para muchos usuarios que necesitan acceder a la información contenida en bases de datos.

Este proyecto aborda este problema desarrollando un sistema que traduce consultas en lenguaje natural a SQL utilizando una arquitectura de agentes inteligentes. Estos agentes trabajan de manera coordinada para identificar las tablas relevantes, generar consultas SQL, ejecutar las consultas y, finalmente, proporcionar insights adicionales basados en los resultados obtenidos. 

\[XXX FOTO\] de la web

**Figura 1:** Arquitectura general del sistema basado en agentes para generación de SQL.

### Objetivo

El objetivo principal de este proyecto es transformar la forma en que los usuarios interactúan con las bases de datos relacionales, facilitando la generación, evaluación y ejecución de consultas SQL a partir de entradas en lenguaje natural. Este sistema está diseñado para reducir las barreras técnicas, mejorar la accesibilidad para usuarios no técnicos y proporcionar una solución eficiente para la gestión y análisis de datos.

### Características

1.  **Facilita la interacción con bases de datos**: Permite a los usuarios generar consultas SQL precisas y optimizadas utilizando lenguaje natural, sin necesidad de conocimientos técnicos avanzados en SQL.
2.  **Implementa un sistema multi-agente**: Arquitectura de agentes inteligentes que colaboran para llevar a cabo tareas específicas dentro del proceso de generación de consultas SQL, como la selección de tablas, la generación de consultas, la iteración y corrección de errores, y la generación de insights.
3.  **Interfaz web accesible y fácil de usar**: Permite a los usuarios interactuar con el sistema de manera intuitiva, incluyendo la generación de consultas SQL, la visualización de resultados y la configuración de preferencias personalizadas.
4.  **Optimización y reducción de los costos**: Permite seleccionar los modelos para optimizar los recursos según el caso que se desee.
5.  **Garantiza la seguridad y la integridad de la base de datos**: Implementa medidas de seguridad efectivas contra ataques como la inyección de comandos o prompt injection, protegiendo la integridad de la base de datos.

### Arquitectura

La arquitectura del sistema se compone de varios agentes inteligentes, cada uno de los cuales está diseñado para realizar tareas específicas en el proceso de generación y ejecución de consultas SQL. Estos agentes trabajan de manera colaborativa bajo la supervisión de un orquestador que asegura la correcta secuencialidad y coordinación de las tareas.

\[foto de la arquitectura\]

#### Agente Proxy (Evaluador de NLQ)

El Agente Proxy es el primer componente del sistema que interactúa con las consultas en lenguaje natural (NLQ) proporcionadas por el usuario. Su función principal es evaluar la relevancia de estas consultas para determinar si son aptas para ser traducidas a SQL. Este agente utiliza un modelo de lenguaje avanzado (GPT-3.5) para clasificar las consultas en una escala del 1 al 5, donde 1 indica irrelevancia total y 5 máxima relevancia.

La implementación del Agente Proxy ha demostrado una tasa de precisión del 95%.

#### Agente Selector (Selección de Tablas)

Una vez que el Agente Proxy ha identificado una consulta relevante, el siguiente paso en el proceso es la selección de tablas, que es realizada por el Agente Selector. Este agente tiene la responsabilidad de identificar las tablas de la base de datos que son más relevantes para la consulta SQL que se va a generar.

El Agente Selector emplea dos enfoques distintos para llevar a cabo esta tarea:

1.  **Enfoque basado en modelo de lenguaje avanzado (Opción 1)**: Este enfoque utiliza un modelo de lenguaje, como GPT-3.5, para identificar las tablas más relevantes basándose en la entrada proporcionada por el usuario. Este método es altamente preciso pero también más costoso en términos de procesamiento y uso de recursos.
2.  **Enfoque semántico con cercanía por coseno (Opción 2)**: Este enfoque combina técnicas de procesamiento semántico con la cercanía por coseno para identificar las tablas relevantes. Aunque es menos costoso y más rápido que el enfoque basado en modelos de lenguaje, puede no ser tan preciso en todos los casos ya que siempre devolverá `k` tablas relevantes y puede haber casos en los que se necesiten más de `k` tablas.

Ambos enfoques han demostrado ser efectivos en la identificación de tablas, con resultados comparables en las pruebas realizadas. La elección entre estos dos enfoques dependerá de las necesidades específicas del usuario, incluyendo factores como el costo, el tiempo de ejecución, precisión, complejidad de la consulta o el número de tablas en la base de datos.

#### Agentes Analistas (Iteración y Corrección)

Una vez que las tablas relevantes han sido seleccionadas, el siguiente paso es la generación y ejecución de la consulta SQL. Este proceso es realizado por un equipo de agentes analistas, que incluyen:

1.  **Data Engineer Agent (SQL Coder)**: Este agente es responsable de la generación inicial de la consulta SQL basándose en las especificaciones proporcionadas por el usuario y las tablas seleccionadas. El agente se asegura de que la consulta generada esté estructurada correctamente y no contenga errores básicos de sintaxis o referencias incorrectas.
2.  **Sr Data Analyst Agent**: Este agente ejecuta la consulta SQL generada por el Data Engineer Agent y verifica su corrección. Si se detectan errores, como resultados inesperados o vacíos, el Sr Data Analyst Agent inicia un proceso iterativo de corrección, enviando feedback al Data Engineer Agent para ajustar la consulta hasta que se obtenga un resultado correcto.

El proceso iterativo de corrección ha demostrado ser altamente efectivo, alcanzando una precisión del 95% después de dos iteraciones en las pruebas realizadas. 

> El modelo del agente **Data Engineer Agent (SQL Coder)** puede ser cambiado desde la GUI.

#### Agente Explorer (Generador de Insights)

Además de generar y ejecutar consultas SQL, el sistema también incluye un Agente Explorer, cuyo objetivo es generar insights adicionales a partir de los resultados obtenidos. Este agente utiliza un modelo de lenguaje avanzado (GPT-4 en las pruebas realizadas) para identificar patrones y tendencias en los datos que pueden no ser evidentes en la consulta original.

El Agente Explorer genera nuevas consultas SQL basadas en la consulta original y proporciona insights que pueden ser de gran valor para el usuario. 

Aunque el uso del Agente Explorer puede incrementar significativamente el costo de la operación (especialmente al utilizar modelos avanzados como GPT-4), también ofrece un valor añadido considerable al proporcionar información adicional. Para reducir los costos, se recomienda el uso de modelos menos costosos como GPT-3 para este agente, dependiendo de las necesidades específicas del proyecto.

> La generación de insights puede ser desactivada desde la GUI.

### Requisitos

Para acceder a los modelos de lenguaje utilizados en el sistema, se requiere una clave API de OpenAI. Esta clave API es necesaria para autenticar las solicitudes a la API de OpenAI y permitir el uso de modelos como GPT-3.5 y GPT-4.

(opcional) Para poner otros modelos necesitarás la clave API de HuggingFace.

### Interfaz Web

La interfaz de usuario ha sido diseñada con un enfoque en la usabilidad y accesibilidad, permitiendo a los usuarios interactuar con el sistema de manera fluida y eficiente. La aplicación web se ha desarrollado utilizando Django para el backend y Vue.js con Vite para el frontend, lo que proporciona una arquitectura moderna y reactiva.

#### Backend en Django

El backend, desarrollado en Django, gestiona las interacciones con la base de datos y los modelos de lenguaje. Utiliza Django REST Framework para exponer las APIs necesarias que interactúan con los agentes y procesan las consultas del usuario.

#### Frontend en Vue.js con Vite

El frontend ha sido desarrollado utilizando Vue.js, un framework progresivo de JavaScript que facilita la construcción de interfaces de usuario interactivas. Vite, una herramienta de compilación rápida, se ha utilizado para optimizar el desarrollo del frontend, proporcionando una experiencia de desarrollo más ágil y eficiente.

La interfaz incluye varias páginas y componentes clave:

*   **Página de Chat**: Permite introducir consultas en lenguaje natural y ver las respuestas generadas.
*   **Página de Configuración**: Ofrece opciones para personalizar el comportamiento del sistema y la conexión a la base de datos.

### Instrucciones de Uso

#### Manual (sin Docker)

Para utilizar el sistema, siga los pasos a continuación:

1.  **Clonar el repositorio**:
    
    ```plaintext
    git clone https://github.com/pablosierrafernandez/DataWhisper-Arquitectura-basada-en-Agentes-para-text-to-sql.git
    ```
    
2.  **Configurar el backend**
    1.  Entorno Virtual
        
        ```plaintext
        cd DataWhisper-Arquitectura-basada-en-Agentes-para-text-to-sql
        cd back
        python -m venv env . # crear entorno virtual
        source env/bin/activate  # Linux/MacOS
        source env\Scripts\activate  # Windows
        pip install -r requirements.txt
        ```
        
    2.  Migraciones
        
        ```plaintext
        # en back/
        python manage.py migrate
        ```
        
3.  **Configurar el frontend**
    
    **Deberás tener instalado Node.js de antemano.**
    
    **\# en front**
    
    **npm install**
    
4.  **Levantar los servicios**
    
    **\# en back**
    
    **python manage.py runserver**
    
    \# en front
    
    npm run dev
    
5.  **Acceder a la aplicación**: Abra su navegador y vaya a `http://localhost:5173` para acceder a la interfaz de usuario.

#### Automático

1.  **Clonar el repositorio**
    
    ```plaintext
    git clone https://github.com/pablosierrafernandez/DataWhisper-Arquitectura-basada-en-Agentes-para-text-to-sql.git
    ```
    
2.  **Levantar los contenedores**
    
    **Deberás tener instalado Docker   y Docker Compose.**
    
    ```plaintext
    docker-compose up --build
    ```
    
3.  **Acceder a la aplicación**: Abra su navegador y vaya a `http://localhost:5173` para acceder a la interfaz de usuario.
    

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE), lo que permite un uso libre y sin restricciones del código, siempre que se incluya la atribución adecuada al autor original.

## Autores

*   **Pablo Sierra Fernández** - Investigador principal y desarrollador del sistema.

## Referencias

1.  **Vaswani, A., et al.** (2017). _Attention is All You Need_. Advances in Neural Information Processing Systems.
2.  **McKinsey & Co.** (2018). _The State of AI in 2018_.
3.  **Sutskever, I., et al.** (2014). _Sequence to Sequence Learning with Neural Networks_.
4.  **Devlin, J., et al.** (2018). _BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding_.

Este sistema ha sido desarrollado en colaboración con la Universitat Rovira i Virgili, como parte de un proyecto de fin de grado en Ingeniería Informática y Biotecnología. Los resultados obtenidos demuestran la viabilidad y efectividad del enfoque propuesto, proporcionando una base sólida para futuras investigaciones en el campo de la inteligencia artificial y el procesamiento de lenguaje natural.
