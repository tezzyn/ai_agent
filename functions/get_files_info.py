import os
from pathlib import Path


def get_files_info(working_directory, directory=None):
    # try:

    #     path = os.path.join(working_directory, directory)

    #     print(os.path.abspath(path))
        

    #     if directory not in path:
    #         return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
    #     if not os.path.isdir(directory):
    #         return f'Error: "{directory}" is not a directory'

         
        
    #     contents = (
    #         f"- {directory}: file_size={os.path.getsize(directory)} bytes, is_dir={os.path.isdir(directory)}\n"
    #     )

    #     return contents
    # except OSError as e:
    #     print(f"Error: {e}")

    wd = Path(working_directory)
    d = Path(directory)

    path = wd / d

    #full_path = os.listdir(path)

    #print(f"~~~{full_path}~~~")

    try:

        for i in path.iterdir():

            print(i.name)
            #print(f"~~~{os.path.isdir(full_path[i])}~~~")
            #items = full_path[i]
            contents = (
                f"- {i.name}: file_size={i.stat().st_size} bytes, is_dir={path.is_dir(i)}\n"
            )
        return contents
    except OSError as e:
        print(f"Error: {e}")