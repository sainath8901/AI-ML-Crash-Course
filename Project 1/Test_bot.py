import os
from dotenv import load_dotenv
import openai

def load_api_key():
    load_dotenv()
    key = os.getenv("OPEN_API_KEY")
    if not key:
        raise RuntimeError("OPEN_API_KEY not found in environment")
    return key

def build_client(api_key):
    return openai.OpenAI(api_key=api_key)

def days_old(client, text):
    messages = [
        {
            "role": "system",
            "content": "You tell me how old am I in days, When I give you my birthday."
        },
        {
            "role": "user",
            "content": f'Please Enter your Birthday:\n\n{text}'
        }
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content.strip()

def main():
    api_key = load_api_key()
    client = build_client(api_key)

    user_input = input("Please Enter your Birthday: ")
    corrected = days_old(client, user_input)
    print("\nDays old:")
    print(corrected)

if __name__ == "__main__":
    main()
