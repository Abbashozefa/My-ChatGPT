import openai
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv('api_key')

openai.api_key=api_key

prompt=input("Ask ChatGPT:")


response =openai.Completion.create(engine="text-davinci-003",prompt=prompt,max_tokens=2000)

print(response['choices'][0]["text"])