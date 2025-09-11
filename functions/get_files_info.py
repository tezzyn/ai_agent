
from pathlib import Path
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )

def get_files_info(working_directory, directory="."):


    combined = Path(working_directory)/Path(directory) 

    cwd = Path.cwd()

    prompt = []


    rel_check = ( 
        
        Path(directory).resolve().is_relative_to(cwd) 
        
        )



    if combined.absolute().is_dir() == False:

        return f'Error: "{directory}" is not a directory'
 
    
    if rel_check == True:

        for i in combined.iterdir():

            contents = (

                f"- {i.name}: file_size={i.stat().st_size} bytes, is_dir={i.is_dir()}"
                
            )
            prompt.append(contents)
    else:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    return "\n".join(prompt)