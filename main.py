import os, sys, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt


def main():

    load_dotenv()
    
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
            print("invalid input")
            sys.exit(1)

    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
      
    if verbose:
        print(f"-> User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
 
    ]

    for _ in range(21):
        final = generate_content(client, messages, verbose)
        if final:
            print(f"Final response: {final}")
            break
            
     
    
    
    

def generate_content(client, messages,verbose=False):
        
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    
    )
    
    if verbose and response.usage_metadata:
        print(f"-> Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"-> Response tokens: {response.usage_metadata.candidates_token_count}\n")
        
    for candidate in (response.candidates or []):
        if candidate.content:
            messages.append(candidate.content)
                
    
    
    if not response.function_calls:
        return response.text
    
    
    function_responses = []

    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response['result'][0]}")
        function_responses.append(function_call_result.parts[0])

    # for fc in response.function_calls:
    #     result = call_function(fc, verbose)
    #     part = result.parts[0] if result.parts else None
    #     if not part or not part.function_response:
    #         raise Exception("empty function call result")
    #     if verbose:
    #         r = part.function_response.response
    #         if isinstance(r, dict) and "result" in r and r["result"]:
    #             print(f"-> {r['result'][0]}")
    #     function_responses.append(part)
        
    
        

    if not function_responses:
        raise Exception("no function responses generated, exiting.")
        
    for part in function_responses:
        messages.append(
            types.Content(role="user", parts=[part])
        )
            
                
    return None

if __name__ == "__main__":
    main()
