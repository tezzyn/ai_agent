from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_file import schema_run_file
from functions.write_file import schema_write_file

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_file import run_file
from functions.write_file  import write_file


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_file,
        schema_write_file,
    ]
)


def call_function(function_call_part, verbose=False):

    if verbose:
        print(f"-> Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f"-> Calling function: {function_call_part.name}")

    func_map = {
        "get_file_content": get_file_content,

        "get_files_info": get_files_info,
    
        "run_file": run_file,

        "write_file": write_file,
        
        }

    func_name = function_call_part.name
    
    # func = name_to_func.get(function_name)

    if func_name not in func_map:

        return types.Content(  
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=func_name,
                    response={"error": f"Unknown function: {func_name}"},
                )
            ],
        )

    args = dict(function_call_part.args)
    args["working_directory"] = "./calculator"

    result = func_map[func_name](**args)
    
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=func_name,
                response={"result": result},
            )
        ],
    )