
from google.genai import types
from functions import *
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_file import run_file
from functions.write_file import write_file

def call_function(function_call_part, verbose=False):

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    # function_name = {
    #     function_call_part["get_file_content"]: get_file_content(function_call_part.args),

    #     function_call_part["get_files_info"]: get_files_info(function_call_part.args),
        
    #     function_call_part["run_file"]: run_file(function_call_part.args),

    #     function_call_part["write_file"]: write_file(function_call_part.args),
        
    #     }

    function_name = function_call_part.name 

    for i in function_name:
        func = i.get(function_name)


    func_dict = {function_name: func}

    if func == None:

        return types.Content(  
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_name}"},
            )
        ],
    )

    kwargs = dict(function_call_part.args)
    kwargs["working_directory"] = "./calculator"



    result = func(**kwargs)

    