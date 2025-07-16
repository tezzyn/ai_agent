import os
from pathlib import Path


def get_files_info(working_directory, directory=None):

    wd = Path(working_directory)
    d = Path(directory)

    path = wd / d

    prompt = []

    rel_check = (wd.absolute().parent == d.absolute())

    print(d)

    print(d.absolute())
    print(d.resolve())
    # print(rel_check)

    if d.is_dir() == False:
        return f'Error: "{directory}" is not a directory'

    if directory == "." or rel_check == True:

        for i in path.iterdir():
            #print(type(i))

            contents = (
                f"- {i.name}: file_size={i.stat().st_size} bytes, is_dir={i.is_dir()}"
            )
            prompt.append(contents)    
    else:

        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    return "\n".join(prompt)