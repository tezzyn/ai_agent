
from pathlib import Path


def get_files_info(working_directory, directory=None):


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