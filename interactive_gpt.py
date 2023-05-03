import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config.get("OPENAI_API_KEY")

## Define what is the chatbot ideally supposed to do.
messages = [{"role": "user", "content": "Hi!"}]
# {"role": "system", "content": "You are a kind helpful assistant"}

## Hold the memory of previous reply and answer under the context
while True:
    msg = input("User : ")
    if msg:
        messages.append(
            {"role": "user", "content": msg}
        )    
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages,
        )
    
    reply = chat.choices[0].message.content
    print("ChatGPT : ", reply)
    messages.append({"role": "assistant", "content": reply})