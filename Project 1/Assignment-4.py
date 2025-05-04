# Question:
# Write 3 different prompts asking an LLM to summarize a news article.
# Test each prompt on the same article using GPT-4
# Analyze & summarize the news about the tone & detail level.

import os
from dotenv import load_dotenv
import openai

def load_api_key():
    load_dotenv()
    return os.getenv('OPENAI_API_KEY')

def build_prompts(article: str):
    return [
        (
            "Basic Summary",
            "Read the paragraph and provide a concise summary.",
            f"Please summarize the following article:\n\n{article}"
        ),
        (
            "Student Summary",
            "Summarize the news article by highlighting key facts and issues for a student audience.",
            f"Article to summarize:\n\n{article}"
        ),
        (
            "Objective Summary",
            "Provide a brief overview of the news article focusing only on the facts, no speculation.",
            f"Article:\n\n{article}"
        )
    ]

def summarize(client, model: str, system_msg: str, user_msg: str, temperature: float = 0):
    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user",   "content": user_msg},
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content.strip()

def main():
    api_key = load_api_key()
    client = openai.OpenAI(api_key=api_key)
    model = "gpt-4o"

    article = input("Enter the news article text:\n")

    prompts = build_prompts(article)
    for label, sys_msg, usr_msg in prompts:
        summary = summarize(client, model, sys_msg, usr_msg)
        print(f"\n=== {label} ===\n{summary}\n")

if __name__ == "__main__":
    main()
