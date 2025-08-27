
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_file import run_file
from functions.write_file  import write_file

def call_function(function_call_part, verbose=False):

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    name_to_func = {
        "get_file_content": get_file_content,

        "get_files_info": get_files_info,
    
        "run_file": run_file,

        "write_file": write_file,
        
        }

    function_name = function_call_part.name
    
    func = name_to_func.get(function_name)

    # for i in function_name:
    #     func = i.get(function_name)


    # func_dict = {function_name: func}

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
    
    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"result": result},
        )
    ],
)

    