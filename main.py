import os, sys, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions
from prompts import system_prompt


def main():

    load_dotenv()

    args = sys.argv[1:]

    if not args:
            print("invalid input")
            sys.exit(1)

    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
 
    ]


    generate_content(client, messages)
    

def generate_content(client, messages):

    parser = argparse.ArgumentParser()
    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    
    )

    parser.add_argument("client")

    parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()

    if  args.verbose:

        print(f"User prompt: {response.text}\n")


        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:

        # print(f"No function call found: {response.text}\n")

    if not response.function_call:
        return f"No function call found: {response.text}\n"
    else:
        function_call
 
    for function_call_part in response.function_call:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")

if __name__ == "__main__":
    main()
