import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Function to get API key (corrected to return the key)
def get_api_key(key_name):
    api_key = os.getenv(key_name)
    if not api_key:
        raise ValueError(f"{key_name} environment variable not set.")
    return api_key

try:
    # 1. Get the API key
    google_key = get_api_key("GEMINI_API_KEY")

    # 2. Configure the API key with the library
    genai.configure(api_key=google_key)

    # 3. Correctly instantiate the GenerativeModel
    model = genai.GenerativeModel('gemini-2.5-flash')

    # 4. Correctly call the generate_content method directly on the model object
    prompt = input("Ask from gemini: ")
    response = model.generate_content(prompt)
    
    print(response.text)

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

