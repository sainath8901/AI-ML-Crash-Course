import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from a .env file in the project root
load_dotenv()

# Retrieve your OpenAI API key from the environment
api_key = os.getenv("OPEN_API_KEY")

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=api_key)

def generate_unique_pairs_prompt(numbers: str, target: str) -> str:
    """
    Send a prompt to GPT-4o asking it to generate a Python function
    that finds all unique pairs summing to the target.
    """
    # system_message tells the model the overall task and constraints
    system_message = {
        "role": "system",
        "content": (
            "Write a Python function that finds all unique pairs of numbers "
            "from the provided list whose sum equals the target. "
            "Each pair should appear only once (e.g., treat (2, 3) and (3, 2) as the same). "
            "Optimize for time and space complexity."
        )
    }
    # user_message provides the actual input data (the list and target)
    user_message = {
        "role": "user",
        "content": f"Array: {numbers}\nTarget: {target}"
    }

    # Call the chat completion endpoint with our messages
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[system_message, user_message],
        temperature=0  # deterministic output
    )

    # Extract and return the generated code from the model's response
    return response.choices[0].message.content

def main():
    # Prompt the user to enter a space-separated list of integers
    raw_numbers = input("Enter a list of integers (space-separated): ").strip()
    # Prompt the user to enter the target sum
    target = input("Enter the target sum: ").strip()

    print("\nGenerating function from GPT-4o...\n")
    # Call our function that interacts with OpenAI and print the result
    result = generate_unique_pairs_prompt(raw_numbers, target)
    print(result)

# Standard Python idiom to ensure main() runs when this script is executed,
# but not when imported as a module in another script.
if __name__ == "__main__":
    main()
