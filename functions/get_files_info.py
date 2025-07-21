import os
from pathlib import Path, PurePath


def get_files_info(working_directory, directory=None):


    wd = Path(working_directory)
    d = Path(directory)

    combined = wd/d

    cwd = Path.cwd()

    #print(cwd == combined)

    #print(d.resolve().is_relative_to(cwd))

    prompt = []
    try:

        rel_check = ( # check if d in wd- somehow
            d.resolve().is_relative_to(cwd)
            
            )
    except ValueError:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # print(PurePath(wd).is_relative_to(d.parent))
    #print(f"```{path.cwd()}````, ````{wd}`````, ````{d.parent}`````")

    if combined.absolute().is_dir() == False:
        return f'Error: "{directory}" is not a directory'
 

    
    if rel_check == True:

        for i in combined.iterdir():

            contents = (
                f"- {i.name}: file_size={i.stat().st_size} bytes, is_dir={i.is_dir()}"
            )
            prompt.append(contents)
    
    return "\n".join(prompt)