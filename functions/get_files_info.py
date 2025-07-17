import os
from pathlib import Path, PurePath


def get_files_info(working_directory, directory=None):

    wd = Path(working_directory)
    d = Path(directory)

    ppath = PurePath(working_directory, directory)

    pppath = Path(working_directory, directory)

    path = wd/d

    prompt = []

    rel_check = (
        wd.absolute().parent == d.absolute()
        )

    print(d) 

    print(wd.absolute(), d.absolute())

    print(pppath.resolve())

    #print([x.parent.name for x in path.iterdir()])
    #print(wd.absolute().parent, d.absolute())
    # print(rel_check)

    if d.is_dir() == False:
        return f'Error: "{directory}" is not a directory'

    if rel_check == True:

        for i in path.iterdir():
            #print(type(i))

            contents = (
                f"- {i.name}: file_size={i.stat().st_size} bytes, is_dir={i.is_dir()}"
            )
            prompt.append(contents)    
    else:

        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    return "\n".join(prompt)