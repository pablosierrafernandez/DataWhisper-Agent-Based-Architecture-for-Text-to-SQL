"""
Purpose:
    Interact with the OpenAI API.
    Provide supporting prompt engineering functions.
"""

import sys
from dotenv import load_dotenv
import os
from typing import Any, Dict
import openai
from ...models import APIConfiguration
# load .env file




# ------------------ helpers ------------------
# Desactivar o posponer el acceso a la configuración si aún no se ha migrado


def safe_get(data, dot_chained_keys):
    keys = dot_chained_keys.split(".")
    for key in keys:
        try:
            if isinstance(data, list):
                data = data[int(key)]
            else:
                data = data[key]
        except (KeyError, TypeError, IndexError):
            return None
    return data


def response_parser(response: Dict[str, Any]):
   
    return response.choices[0].message.content if response.choices else None

# ------------------ content generators ------------------


def prompt(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    # validate the openai api key - if it's not valid, raise an error
    config=APIConfiguration.get_global_config()
    if not config['openai_api_key']:
        sys.exit(
            """
ERORR: OpenAI API key not found. Please export your key to OPENAI_API_KEY
Example bash command:
    export OPENAI_API_KEY=<your openai apikey>
            """
        )

    response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)
   

    return response_parser(response)


def add_cap_ref(
    prompt: str, prompt_suffix: str, cap_ref: str, cap_ref_content: str
) -> str:
    """
    Attaches a capitalized reference to the prompt.
    Example
        prompt = 'Refactor this code.'
        prompt_suffix = 'Make it more readable using this EXAMPLE.'
        cap_ref = 'EXAMPLE'
        cap_ref_content = 'def foo():\n    return True'
        returns 'Refactor this code. Make it more readable using this EXAMPLE.\n\nEXAMPLE\n\ndef foo():\n    return True'
    """

    new_prompt = f"""{prompt} {prompt_suffix}\n\n{cap_ref}\n\n{cap_ref_content}"""

    return new_prompt