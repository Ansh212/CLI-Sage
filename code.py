import openai
import sys
import argparse

# Set your OpenAI API key here
api_key: str = "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"
openai.api_key = api_key

def chat_with_gpt(prompt: str) -> str:
    generated_text = ""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the GPT-3.5 Turbo engine
        messages=[
            {"role": "system", "content": "You are a code assistant, respond only with the code without explanation"},
            {"role": "user", "content": prompt}
        ],
        stream=True  # Enable streaming
    )

    try:
        # Print the "Sage:" prompt at the beginning
        print("Sage:")

        response_text = ""

        for chunk in response:
            delta_content = chunk['choices'][0]['delta'].get('content', '')
            if delta_content:
                # Print subsequent responses on the same line
                print(delta_content, end='', flush=True)
                response_text += delta_content
        return response_text

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chat with GPT-3.5 Turbo")
    parser.add_argument("prompt", type=str, help="The prompt to send to GPT-3.5 Turbo")
    parser.add_argument("-f", "--file", type=str, help="Save the response to a file", default=None)

    args = parser.parse_args()

    response_text = chat_with_gpt(args.prompt)

    if args.file:
        with open(args.file, "w") as output_file:
            output_file.write(response_text)
            print(f"\nResponse saved to {args.file}")
    
    print("\nChatGPT: Goodbye!")

