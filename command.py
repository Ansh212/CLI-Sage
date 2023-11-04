import openai
import subprocess,os
import sys
import signal

color_code = "1;32"

def signal_handler(signal, frame):
    print()
    print("Bye")
    sys.exit()

# Set your OpenAI API key here
api_key: str = ""
openai.api_key = api_key

def chat_with_gpt(prompt: str) -> str:
    generated_text = ""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Linux command assistant, respond only with the command without explanation"},
            {"role": "user", "content": prompt}
        ],
        stream=True
    )

    try:
        for chunk in response:
            delta_content = chunk['choices'][0]['delta'].get('content', '')
            if delta_content:
                # Print and append the generated content to generated_text variable
                generated_text += delta_content
                print(delta_content, end='', flush=True)
                
    except Exception as e:
        print(f"Error: {e}")

    print()  # Move to the next line after streaming the response
    return generated_text

def color_print(text, color_code):
    formatted_text = f"\033[{color_code}m {text} \033[0m"
    print(formatted_text, end='', flush=True)  # Print without newline and flush the output

if __name__ == "__main__":
    prev_res = ""
    response = ""

    print("press control-C to exit")
    signal.signal(signal.SIGINT, signal_handler)

    try:
        while True:
            user_input: str = input(">>> ")

            if user_input.lower() in ['quit', 'exit', 'bye', 'q', 'x', 'b']:
                break

            if user_input == "E":
                # Execute the generated command
                print()
                os.system(response)
                print()
                prev_res=""
                continue 

            if prev_res != "":
                prev_res = "This was the previous command " + prev_res

            response = chat_with_gpt(user_input + " " + prev_res)
            prev_res = response

    except KeyboardInterrupt:
        print("okay")

