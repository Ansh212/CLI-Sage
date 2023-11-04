import openai
import os
from typing import Dict, Any

# Set your OpenAI API key here
api_key: str = "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"
openai.api_key = api_key

def chat_with_gpt(prompt: str) -> str:
    response: Dict[str, Any] = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the GPT-3.5 Turbo engine
        messages=[
            {"role": "system", "content": "You are a code assistant, respond only with the code without explanation, do not include ''' on the top and bottom"},
            {"role": "user", "content": prompt}
        ]
    )
    # Extract the assistant's reply from the response
    response_text: str = response['choices'][0]['message']['content']
    return response_text

# Input prompt
user_input = input("You: ")

# Get the response from GPT-3.5 Turbo
response = chat_with_gpt(user_input)

# Deduce file extension based on user input
file_extension = ".txt"  # Default to text file if language is not recognized

if "python" in user_input.lower():
    file_extension = ".py"
elif "c++" in user_input.lower() or "cpp" in user_input.lower():
    file_extension = ".cpp"
elif "java" in user_input.lower():
    file_extension = ".java"

# Specify the file name with appropriate extension
file_name = "code_output" + file_extension

# Save the GPT response to the file
with open(file_name, "w") as code_file:
    code_file.write(response)

print(f"Code response saved to {file_name}")

