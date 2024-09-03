import json
import os
import sys
import time
from .modules.db import PostgresManager
from .modules import llm
import dotenv
import argparse
import autogen
from autogen.oai.openai_utils import config_list_from_json
from .modules.Orchestrator import Orchestrator
from .modules.Table import get_relevant_tables_op1, get_relevant_tables_op2
import tiktoken
from ..models import APIConfiguration
dotenv.load_dotenv(override=True)




model_name=''
hugging_api = ''

POSTGRES_TABLE_DEFINITIONS_CAP_REF = "TABLE_DEFINITIONS"
RESPONSE_FORMAT_CAP_REF = "RESPONSE_FORMAT"
SQL_DELIMITER = "---------"

# Para el recuento de tokens y cálculo de costos
TOKEN_COSTS = {
    "gpt-3.5-turbo": 0.002,  # Cost per 1k tokens in dollars
    "gpt-4": 0.03,           # Cost per 1k tokens in dollars
}

system_message="""You are an expert in classifying Natural Language Queries (NLQ) for SQL. 
        Your task is to determine if a given input is relevant to an SQL query.
        Rank the input from 1 to 5, where:
        1: Definitely not NLQ
        2: Likely not NLQ
        3: Neutral / Unsure
        4: Likely NLQ
        5: Definitely NLQ
        Respond with only the number representing your ranking."""
import requests
def generate_sql_with_sqlcoder_api(prompt, table_definitions):
    API_URL = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {"Authorization": f"Bearer {hugging_api}"}

    full_prompt = f"""### SQL tables, with their properties:
{table_definitions}

### A query to answer:
{prompt}

### SQL query to answer the question:
"""

    payload = {
        "inputs": full_prompt,
        "parameters": {
            "max_new_tokens": 250,
            "temperature": 0,
            "do_sample": True,
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

    result = response.json()
    
    if isinstance(result, list) and len(result) > 0:
        sql_query = result[0].get('generated_text', '').strip()
        # Extract the SQL query from the generated text
        sql_parts = sql_query.split('```sql')
        if len(sql_parts) > 1:
            sql_query = sql_parts[1].split('```')[0].strip()
        return sql_query
    else:
        raise Exception("Unexpected API response format")

def count_tokens(text, model='gpt-3.5-turbo'):
    enc = tiktoken.encoding_for_model(model)
    tokens = enc.encode(text)
    return len(tokens)

class SQLEngineerAgent(autogen.AssistantAgent):
    def __init__(self, name, system_message, table_definitions):
        super().__init__(name=name, system_message=system_message, llm_config=False)
        self.table_definitions = table_definitions

    def generate_reply(self, messages=None, sender=None, config=None):
        last_message = messages[-1]['content'] if messages else ""
        try:
            sql_query = generate_sql_with_sqlcoder_api(last_message, self.table_definitions)
            return f"Here's the SQL query generated:\n\n```sql\n{sql_query}\n```"
        except Exception as e:
            return f"An error occurred while generating the SQL query: {str(e)}"


def main(prompt):
    start_time = time.time()  # Inicia el temporizador
    total_tokens = 0
    # Lógica anterior en main(), adaptada para recibir el prompt directamente
    if not prompt:
        return "Please provide a prompt"
    
    prompt = f"Fulfill this database query: {prompt}. "
    sql_relevance_agent = autogen.AssistantAgent(
            name="SQL_Relevance_Agent",
            llm_config={
                "temperature": 0,
                "config_list": [
                    {
                        "model": "gpt-3.5-turbo",
                        "api_key": APIConfiguration.get_global_config()['openai_api_key']
                    }
                ]
            },
            system_message=system_message,
            code_execution_config=False,
            human_input_mode="NEVER"
        )
    def check_relevance(prompt):
            sql_relevance_agent.send(prompt, sql_relevance_agent)
            reply = sql_relevance_agent.generate_reply(sender=sql_relevance_agent)
            
            try:
                return int(reply.strip().replace("\n", "").replace("\t", "").replace(" ", ""))
            except Exception as e:
                print(e)
                return -1
            

    relevance_score = check_relevance(prompt)
    
    if relevance_score == -1:
        print("Error: NLQ Classifier did not return a valid integer.")
        return 0
    if relevance_score > 3:    
        total_tokens
        total_tokens += count_tokens(prompt) + count_tokens(system_message)
        with PostgresManager() as db:
            
            
                try:
                    config=APIConfiguration.get_global_config()
                   
                    db.connect_ddbb(config['hostname'], config['database'], config['username'], config['password'], config['port'])
                   
                   
                    # Get relevant tables
                   
                    if config['opcion']:
                        relevant_tables, tokens_relevants = get_relevant_tables_op2(db, prompt)
                        tokens_relevants = 0
                       
                    else:
                        
                        ### XXX Si uso op2 no se hay que contar los tokens ya qye se hace insitu
                        relevant_tables, tokens_relevants = get_relevant_tables_op1(db, prompt)
                    
                    
                    # Get table definitions for relevant tables only
                    table_definitions = db.get_table_definitions_for_prompt(relevant_tables)

                    prompt = llm.add_cap_ref(
                        prompt,
                        f"Use these {POSTGRES_TABLE_DEFINITIONS_CAP_REF} to satisfy the database query.",
                        POSTGRES_TABLE_DEFINITIONS_CAP_REF,
                        table_definitions,
                    )

                    # Configuración base GPT
                    base_config = {
                        "temperature": 0,
                        "config_list": [
                            {
                                "model": "gpt-3.5-turbo",
                                "api_key": config['openai_api_key']
                            }
                        ]
                    }

                    # Contar tokens en el prompt inicial
                  
                    
                    
                    total_tokens += tokens_relevants
                    # Configuración GPT con funciones para el Sr Data Analyst
                    gpt4_config_with_functions = base_config.copy()
                    gpt4_config_with_functions["functions"] = [
                        {
                            "name": "run_sql",
                            "description": "Run a SQL query against the postgres database",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "sql": {
                                        "type": "string",
                                        "description": "The SQL query to run",
                                    }
                                },
                                "required": ["sql"],
                            },
                        }
                    ]

                    # Mapa de funciones
                    function_map = {
                        "run_sql": db.run_sql,
                    }

                    # Función de terminación
                   

                   

                    # Definición de los agentes
                    user_proxy = autogen.UserProxyAgent(
                        name="Admin",
                        system_message="A human admin. Interact with the Product Manager to discuss the plan. Plan execution needs to be approved by this admin.",
                        code_execution_config=False,
                        human_input_mode="NEVER",
                    
                    )
                    if config['model_name'] == '':
                        print("entro")
                        
                        data_engineer = autogen.AssistantAgent(
                            name="Engineer",
                            llm_config=base_config,
                            system_message="A Data Engineer. You follow an approved plan. Generate the initial SQL based on the requirements provided. Do not use SQL reserved words as aliases. put the name of the tables and columns in double quotes.  If there's an error in the SQL execution, analyze the error message and provide a corrected SQL query.",
                            code_execution_config=False,
                            human_input_mode="NEVER",
                            
                        )
                    else:
                        global model_name 
                        model_name = config['model_name']
                        global hugging_api 
                        hugging_api = config['huggingface_api_key']
                        data_engineer = SQLEngineerAgent(
        name="Engineer",
        system_message="A Data Engineer. You follow an approved plan. Generate the initial SQL based on the requirements provided. Do not use SQL reserved words as aliases. put the name of the tables and columns in double quotes.  If there's an error in the SQL execution, analyze the error message and provide a corrected SQL query.",
        table_definitions=table_definitions
    )

                    sr_data_analyst = autogen.AssistantAgent(
                        name="Sr_Data_Analyst",
                        llm_config=gpt4_config_with_functions,
            system_message="Sr Data Analyst. You follow an approved plan. You run the SQL query. Only run SQL and not show the results",            
                        human_input_mode="NEVER",
                        function_map=function_map,
                        
                    
                    )

                    

                    # Crear grupo de chat e iniciar la conversación
                    # Crear y ejecutar el orquestador
                    data_engineering_agents = [
                        user_proxy,
                        data_engineer,
                        sr_data_analyst,
                    
                    ]
                    data_eng_orchestrator = Orchestrator(
                        name="Data Analytics Multi-Agent",
                        agents=data_engineering_agents, tables_def= table_definitions
                    )
                   
                    messages = data_eng_orchestrator.sequential_conversation(prompt)

                    total_tokens+=count_tokens(str(messages), model="gpt-3.5-turbo")
                   

                   
                  

                    insights_agent = autogen.AssistantAgent(
                        name="Insights_Generator",
                        llm_config={
                            "temperature": 0.7,
                            "config_list": [
                                {
                                    "model": "gpt-4",  # Usamos GPT-4 para generar insights más creativos
                                    "api_key": config['openai_api_key']
                                }
                            ]
                        },
                        system_message="You are a data analyst expert in SQL. You generate insightful SQL queries based on given information.",
                    )
                    if config["num_insights"]!=0:
                       
                        insights_result, prompt_insights = data_eng_orchestrator.generate_insights(prompt, table_definitions, insights_agent, config['num_insights'])

                        
                        json.dumps(insights_result, indent=2)

                        # Guardar los insights en un archivo JSON
                        with open("generated_insights.json", "w") as f:
                            json.dump(insights_result, f, indent=2)
                        # Calcular y mostrar el costo total
                        
                        insights_tokens = count_tokens(str(prompt_insights)) 
                        total_tokens += insights_tokens

                    total_cost = (total_tokens / 1000) * TOKEN_COSTS["gpt-3.5-turbo"]  
                    print(f"\nTotal Tokens: {total_tokens}")
                    print(f"Total Cost: ${total_cost:.4f}")
                except:
                    return "ERROR"
    else:
        print("Error: No se ha detectado NLQ.")
      
    end_time = time.time()  
    elapsed_time = end_time - start_time  # Calcular el tiempo transcurrido
    print(f"Time taken to execute main: {elapsed_time:.2f} seconds")
    return "OK", total_cost

if __name__ == "__main__":
    main(sys.argv[1])