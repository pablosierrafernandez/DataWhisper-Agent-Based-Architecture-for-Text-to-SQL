
import json
import os
from ...models import APIConfiguration
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers.openai_tools import PydanticToolsParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import CommaSeparatedListOutputParser
import faiss
import numpy as np
import tiktoken
from sentence_transformers import SentenceTransformer



def count_tokens(text, model_name="gpt-3.5-turbo"):
    encoding = tiktoken.encoding_for_model(model_name)
    tokens = encoding.encode(text)
    return len(tokens)
class Table(BaseModel):
    """Table in SQL database."""
    name: str = Field(description="Name of table in SQL database.")

def get_table_schema(db, table_name):
    query = f"""
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = '{table_name}'
    """
    result = db.run_sql(query)
    return ', '.join([f"{col[0]} ({col[1]})" for col in result])

def get_table_schema(db, table_name):
    query = f"""
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = '{table_name}'
    """
    result = db.run_sql(query)
    result_list = json.loads(result)
    return ', '.join([f"{col['column_name']} ({col['data_type']})" for col in result_list])

def get_relevant_tables_op2(db, user_query, top_k=3):
    try:
       
        table_names = db.get_all_table_names()
        
      
        table_schemas = {}
        for table in table_names:
            try:
                table_schemas[table] = get_table_schema(db, table)
            except Exception as e:
                print(f"Error getting schema for table {table}: {e}")
                table_schemas[table] = "Schema unavailable"
        
       
        table_descriptions = [f"Table: {table}, Schema: {schema}" for table, schema in table_schemas.items()]
        
        
        model = SentenceTransformer('all-MiniLM-L6-v2')
        
       
        table_embeddings = model.encode(table_descriptions)
        
        
        dimension = table_embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(table_embeddings.astype('float32'))
        
       
        query_embedding = model.encode([user_query])
        
       
        k = min(top_k, len(table_names))
        distances, indices = index.search(query_embedding.astype('float32'), k)
        
       
        relevant_tables = [table_names[i] for i in indices[0]]
        
        
        total_tokens = count_tokens(str(table_descriptions) + user_query)
        
       
        return relevant_tables, total_tokens
    except Exception as e:
        print(f"Error in get_relevant_tables: {e}")
        return [], 0
    
    
def get_relevant_tables_op1(db, user_query):
    table_names = "\n".join(db.get_all_table_names())
    system = f"""You are a database expert. Your task is to identify the MOST RELEVANT tables for a given SQL query.
    Available tables are:
    {table_names}

    Rules:
    1. Only select tables that are DIRECTLY relevant to answering the query.
    2. Do not include tables that are merely related but not necessary for the specific query.
    3. If the query can be answered with a single table, only return that table.
    4. Return table names as a comma-separated list, with no additional text or explanations.
    5. If no tables are relevant or you're unsure, return an empty list.
    """
    
    human = "User query: {input}\nRelevant tables:"
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system),
        ("human", human),
    ])
    config=APIConfiguration.get_global_config()['openai_api_key']
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, api_key=config)
    output_parser = CommaSeparatedListOutputParser()
    
    chain = prompt | llm | output_parser
    
    result = chain.invoke({"input": user_query})
    # Retrieve token count
    total_tokens = count_tokens(system) + count_tokens(human)
    return result,total_tokens