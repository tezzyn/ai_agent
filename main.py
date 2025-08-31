import os, sys, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions
from functions.do_function import do_function
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
    
    # verbose = "-v" in sys.argv or "--verbose" in sys.argv

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
        if not response.function_calls:
            return response.text

        for function_call_part in response.function_calls:

            print(do_function(function_call_part, verbose=True).parts[0].function_response.response)

        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:

        if not response.function_calls:
            return response.text

        for function_call_part in response.function_calls:
            print(do_function(function_call_part).parts[0].function_response.response)





if __name__ == "__main__":
    main()
