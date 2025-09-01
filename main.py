import os, sys, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt


def main():

    load_dotenv()
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    args = sys.argv[1:]

    if not args:
            print("invalid input")
            sys.exit(1)

    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
  
    user_prompt = " ".join(args)
    
    if verbose:
        print(f"-> User prompt: {user_prompt}\n")

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
        print(f"-> Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"-> Response tokens: {response.usage_metadata.candidates_token_count}\n")

    if not response.function_calls:
        return response.text
    
    function_responses = []

    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, args.verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")



if __name__ == "__main__":
    main()
