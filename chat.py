import openai
from typing import Dict, Any
import time
import sys 


# Set your OpenAI API key here
api_key: str = "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"
openai.api_key = api_key

def chat_with_gpt(prompt: str) -> str:
    generated_text = ""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the GPT-3.5 Turbo engine
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ],
        stream=True  # Enable streaming
    )

    try:
        # Print the "Sage:" prompt at the beginning
        print("Sage:", end=' ', flush=True)

        for chunk in response:
            delta_content = chunk['choices'][0]['delta'].get('content', '')
            if delta_content:
                # Print subsequent responses on the same line
                for i in (delta_content):
                    print(i, end='',flush=True)
                    time.sleep(0.02)
                #print(delta_content, end='', flush=True)
    except Exception as e:
        print(f"Error: {e}")

    print()  # Move to the next line after streaming the response
    return generated_text

if __name__ == "__main__":
              
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
        response_text = chat_with_gpt(user_input)
        # Do something with the final response_text if needed
    else:
        print("Usage: python your_script.py 'your_prompt'")
