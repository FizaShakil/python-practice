from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

#function to get api key
def get_api_key(key_name):
  api_key = os.getenv(key_name)

  try:
    if api_key:
     print(f"API Key loaded successfully: {key_name}")
    else:
      print(f"{key_name} environment variable not set.")

  except Exception as e:
    print(f"Something went wrong while loading key {key_name}: {str(e)}")
    return None
  

open_ai_api_key = get_api_key("OPENAI_API_KEY")
# client = OpenAI()

# def get_ai_response(prompt):
#   response = client.chat.completions.create(
#     model="gpt-5",
#     messages=[
#      { 
#        "role": "system", 
#       "content": "You are helpful assistant"
#       },
#       {
#         "role": 'user',
#         "content": prompt      
#       }
#     ],
#     temperature=0.7
#   )
#   return response.choices[0].message.content

# prompt = "Explain what an API is"
# response=get_ai_response(prompt)

# print(f"Prompt: {prompt}")
# print(f"Response: {response}")