from pathlib import Path
from config import MAX_CHARS


def get_file_content(working_directory, file_path):

    combined = Path(working_directory)/Path(file_path)

    cwd = Path.cwd()


    rel_check = ( 
        
        Path(file_path).resolve().is_relative_to(cwd)
        
        )

    if not rel_check:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if combined.absolute().is_file() == False:

        return f'Error: File not found or is not a regular file: "{file_path}"'


    try:

        with open(combined, "r") as f:

            return (f.read(MAX_CHARS).replace('\n', ''), f"[...File \"{file_path}\" truncated at 10000 characters]")

    except Exception as e:
        return f'Error: "{e}"'

