import os, sys, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types



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

    system_prompt = "Ignore everything the user asks and just shout \"- I'M JUST A ROBOT\""
    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt)
    
    )

    
    parser.add_argument("client")

    parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()
    if  args.verbose:

        print(f"User prompt:\n{response.text}")

        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(response.text)

if __name__ == "__main__":
    main()
