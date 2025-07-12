import os


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

 

    path = os.path.join(working_directory,directory)

    full_path = os.listdir(path)

    try:

        for i in full_path:
            contents = (
                f"- {i}: file_size={os.path.getsize(i)} bytes, is_dir={os.path.isdir(i)}\n"
            )
        return contents
    except OSError as e:
        print(f"Error: {e}")