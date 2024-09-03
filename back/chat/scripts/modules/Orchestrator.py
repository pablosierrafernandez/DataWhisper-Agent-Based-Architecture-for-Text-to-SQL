import json
import re
from typing import List, Optional, Tuple
import autogen

def is_empty_result(content):
    try:
        result = json.loads(content)
        if not result:
            return True
        if len(result) == 1:
            first_item = result[0]
            if all(value == 0 or value is None or value == '' for value in first_item.values()):
                return True
        return False
    except json.JSONDecodeError:
        return False

class Orchestrator:
    def __init__(self, name: str, agents: List[autogen.ConversableAgent], tables_def):
        self.name = name
        self.agents = agents
        self.messages = []
        self.complete_keyword = "APPROVED"
        self.error_keyword = "ERROR"
        self.tables_def = tables_def

        if len(self.agents) < 2:
            raise Exception("Orchestrator needs at least two agents")
    import re
    import json

    def generate_insights(self, original_query: str, table_definitions: str, insights_agent: autogen.AssistantAgent, num_insights: int):
       
        
        prompt = f"""Based on the original query: '{original_query}' and the following table definitions:

    {table_definitions}

    Generate {num_insights} new SQL queries that could provide additional valuable insights related to the original query. Translate the 'description' value into the language of the original query (Rembember de query: {original_query}). Each insight should include:
    1. A brief description of what the query aims to uncover. Always must start by: 'A query that aims...'
    2. The business value of this information
    3. The SQL query itself
    
    Format your response as a JSON array with the following structure:
    [
    {{
        "description": "Brief description of what the query aims to uncover in the original languaje from query",
        "business_value": "Explanation of how this information can drive business value",
        "sql": "The SQL query"
    }}
    ]
    Ensure that each SQL query is valid and uses the provided table structures correctly. 
    IMPORTANT: Your entire response must be a valid JSON array."""

        
        
        insights_agent.send(prompt, insights_agent)
        reply = insights_agent.generate_reply(sender=insights_agent)
        
       
        
        try:
            # Intenta parsear la respuesta como JSON
            insights = json.loads(reply)
        except json.JSONDecodeError:
            # Si falla, intenta extraer el JSON de la respuesta
            json_match = re.search(r'\[[\s\S]*\]', reply)
            if json_match:
                try:
                    insights = json.loads(json_match.group())
                except json.JSONDecodeError:
                    print("Error: No se pudo extraer un JSON válido de la respuesta")
                    return []
            else:
                print("Error: No se encontró una estructura JSON en la respuesta")
                return [], ""

        # Asegúrate de que tenemos el número correcto de insights
        insights = insights[:num_insights]
        
        # Verifica que cada insight tenga la estructura correcta
        valid_insights = []
        for insight in insights:
            if all(key in insight for key in ["description", "business_value", "sql"]):
                valid_insights.append(insight)
            else:
                print(f"Advertencia: Se omitió un insight con estructura incorrecta: {insight}")

        return valid_insights, prompt
    @property
    def total_agents(self):
        return len(self.agents)

    @property
    def last_message_is_dict(self):
        return isinstance(self.messages[-1], dict)

    @property
    def last_message_is_string(self):
        return isinstance(self.messages[-1], str)

    @property
    def last_message_is_func_call(self):
        return self.last_message_is_dict and self.latest_message.get(
            "function_call", None
        )

    @property
    def last_message_is_content(self):
        return self.last_message_is_dict and self.latest_message.get("content", None)

    @property
    def latest_message(self) -> Optional[str]:
        if not self.messages:
            return None
        return self.messages[-1]

    def add_message(self, message: str):
        self.messages.append(message)

    def has_functions(self, agent: autogen.ConversableAgent):
        return len(agent._function_map) > 0

    def basic_chat(
        self,
        agent_a: autogen.ConversableAgent,
        agent_b: autogen.ConversableAgent,
        message: str,
    ):
       
        
        agent_a.send(message, agent_b)
       
        reply = agent_b.generate_reply(sender=agent_a)
        
        
       
        
        self.add_message(reply)
       

   
    
    def function_chat(
        self,
        agent_a: autogen.ConversableAgent,
        agent_b: autogen.ConversableAgent,
        message: str,
        previous_agent
    ):
        self.basic_chat(agent_a, agent_a, message)
       
        iterations = 0
        assert self.last_message_is_content
        while(iterations < 2):
            if re.search(r'\berror\b', self.latest_message['content'], re.IGNORECASE):

              
                self.basic_chat(previous_agent, agent_a, "Generate the correct SQL. Fix the following bug or bugs to fix the correct SQL: "+self.latest_message['content']+" \n Keep the following in mind when creates the SQL: 1. Put the tables names between quotes.\n 2.Check the aliases that correspond correctly with the tables. \n 3. Check the correct columns names and table names. \nScheme:" + self.tables_def + "\n Only retrieve the SQL.")
                self.basic_chat(agent_a, agent_a, self.latest_message)
                iterations+=1
            elif is_empty_result(self.latest_message['content']):
                additional_instructions = """
                When performing SQL queries, keep the following in mind:
                1. You can use `LOWER()` for case-insensitive comparisons.
                2. Consider using `LIKE` and wildcards like '%' to search for partial matches, as a word you're looking for might appear partially.
                """
                self.basic_chat(previous_agent, agent_a, "Fix the following bug or bugs: " + self.latest_message['content'] + "\nScheme:" + self.tables_def + "\n" + additional_instructions)
                self.basic_chat(agent_a, agent_a, self.latest_message)
                iterations+=1
            else:
                break
        content = self.latest_message['content']
        parsed_content = json.loads(content)
        formatted_json = json.dumps(parsed_content, indent=4)
        

    def sequential_conversation(self, prompt: str) -> Tuple[bool, List[str]]:
       

        self.add_message(prompt)
       
        
        for idx, agent in enumerate(self.agents):
           
            agent_a = self.agents[idx]
            if idx == 2:
                agent_b = self.agents[idx]
            else:
                agent_b = self.agents[idx + 1]

           
            if self.last_message_is_string:
                self.basic_chat(agent_a, agent_b, self.latest_message)
            if self.last_message_is_func_call and self.has_functions(agent_a):
                self.function_chat(agent_a, agent_b, self.latest_message, self.agents[idx-1])

            if idx == self.total_agents - 1:
               
                
                
               
                # Guardar la respuesta final en un archivo JSON formateado
                self.save_final_response(self.latest_message)
                del self.messages[-1]

                return self.messages

    
        

    def save_final_response(self, response):
        try:
            # Verificar si la respuesta ya es un diccionario
            if isinstance(response, dict):
                parsed_content = response
            else:
                parsed_content = json.loads(response)
            
            # Extraer y guardar solo el contenido relevante
            content = parsed_content.get("content", parsed_content)
            content = json.loads(content)
                
            with open("final_response.json", "w") as json_file:
                json.dump(content, json_file, indent=4)
        except json.JSONDecodeError:
            print("La respuesta final no es un JSON válido")
