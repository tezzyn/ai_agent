import os, sys, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions




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

    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    
    )


    if not response.function_calls:
        return response.text

    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")

    
    parser.add_argument("client")

    parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()
    if  args.verbose:

        print(f"User prompt:\n{function_call_part}")

        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(function_call_part)

if __name__ == "__main__":
    main()
