import requests
import openai
import json

from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config.get("OPENAI_API_KEY")

## Pros of using API endpoint
# 1. apply method regardless of coding language
# 2. streaming ui by generating text can possible
# 3. update change parameter more easliy

URL = "https://api.openai.com/v1/chat/completions"

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "What is the first GUI computer in the world?"}
    ],
    ## Parameter settings
    ## reference : https://platform.openai.com/docs/api-reference/chat/create
    "temperature": 1.0,
    "top_p": 1.0,
    "n": 1,
    "stream": False,
    "presence_penalty": 0,
    "frequency_penalty": 0,
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
}

response = requests.post(URL, headers=headers, json=payload, stream=False)

json_obj = json.loads(response.content)

# with open('output.json', mode='w', encoding='utf-8') as f:
#     if f.readline == "":
#         json.dump([], f)
#     else:
#         entry = {'chat': }

with open('output.json', 'w') as f:
    json.dump(json_obj, f, indent = 2)