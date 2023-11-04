import openai
import subprocess, os
from typing import Dict, Any
import sys
import signal

color_code = "1;32"

def signal_handler(signal, frame):
    print()
    print("Bye")
    sys.exit()

# Set your OpenAI API key here
api_key: str = "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"
openai.api_key = api_key

def chat_with_gpt(prompt: str) -> str:
    response: Dict[str, Any] = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the GPT-3.5 Turbo engine
        messages=[
            {"role": "system", "content": "You are a Linux command assistant, respond only with the command without explanation"},
            {"role": "user", "content": prompt}
        ]
    )
    # Extract the assistant's reply from the response
    response_text: str = response['choices'][0]['message']['content']
    return response_text

def color_print(text, color_code):
    formatted_text = f"\033[{color_code}m {text} \033[0m"
    print(formatted_text)


if __name__ == "__main__":
    # Check if a command-line argument is provided
    #if len(sys.argv) != 2:
     #   print("Usage: python your_script.py 'Your user input'")
      #  sys.exit(1)

    # Get user input from the command-line argument
    #user_input = sys.argv[1]

    # Get the response from GPT-3.5 Turbo



    prev_res = ""
    response: str = ""

    print("press control-C to exit")
    signal.signal(signal.SIGINT, signal_handler)


try:
    while True:
        user_input: str = input(">>> ")

        if(user_input == "E"):
            # Print the response
            print()
            os.system(response)
            print()
            prev_res=""
            continue

        elif user_input.lower() in ['quit', 'exit', 'bye', 'q', 'x', 'b']:
            break

        if(prev_res != ""):
            prev_res = "This was the previous command " + prev_res

        response = chat_with_gpt(user_input + " " + prev_res)
        color_print(response, color_code)
        prev_res = response

except KeyboardInterrupt:
    print("okay")
