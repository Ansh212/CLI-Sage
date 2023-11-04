import openai
import time
from typing import Dict, Any

# Set your OpenAI API key here
api_key: str = "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"
openai.api_key = api_key

def chat_with_gpt(prompt: str) -> str:
    response: Dict[str, Any] = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the GPT-3.5 Turbo engine
        messages=[
            {"role": "system", "content": "You are a code assistant, respond only with the code without explaination "},
            {"role": "user", "content": prompt}
        ]
    )
    # Extract the assistant's reply from the response
    response_text: str = response['choices'][0]['message']['content']
    return response_text

print("Welcome to ChatGPT terminal interface!")
while True:
    user_input: str = input("You: ")
    if user_input.lower() in ['quit', 'exit', 'bye', 'q', 'x', 'b']:
        print("ChatGPT: Goodbye!")
        break
    response: str = chat_with_gpt(user_input)

    # Print the response characters one by one with a delay
    for char in response:
        print(char, end='', flush=True)
        time.sleep(0.05)  # Adjust the sleep duration to control the streaming speed

    print()  # Move to the next line after the streaming response



