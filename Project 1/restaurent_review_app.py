import os
from dotenv import load_dotenv
import openai

def get_api_key():
    load_dotenv()
    key = os.getenv("OPEN_API_KEY")
    if not key:
        raise RuntimeError("Could not find OPENAI_API_KEY in your environment")
    return key

def create_client(api_key):
    return openai.OpenAI(api_key=api_key)

def classify_sentiment(client, text):
    messages = [
        {
            "role": "system",
            "content": (
                "You’re an assistant that reads restaurant reviews "
                "and tells whether they’re Positive, Negative, or Neutral."
            )
        },
        {
            "role": "user",
            "content": f'Here’s the review:\n\n"{text}"\n\nHow would you classify its sentiment?'
        }
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content.strip()

def main():
    api_key = get_api_key()
    client = create_client(api_key)

    review = input("Please enter a restaurant review: ")
    sentiment = classify_sentiment(client, review)

    print(f"\nSentiment: {sentiment}")

if __name__ == "__main__":
    main()
