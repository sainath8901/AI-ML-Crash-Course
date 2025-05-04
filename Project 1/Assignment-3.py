import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

def translate_to_spanish(text: str) -> str:
    system_prompt = (
        "Convert the following paragraph from English to Spanish. "
        "The text describes key features of an advanced renewable energy system. "
        "Use precise technical terminology from the renewable energy sector."
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": text}
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    english_paragraph = (
        "The advanced renewable energy system integrates solar panels with battery storage, "
        "allowing for optimized load management and seamless grid integration. "
        "State-of-the-art inverters and smart control algorithms ensure maximum efficiency."
    )
    spanish_translation = translate_to_spanish(english_paragraph)
    print("Spanish Translation:\n", spanish_translation)
