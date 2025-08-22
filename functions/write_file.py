from pathlib import Path
from google.genai import types


schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Write content to file in the specified directory and shows the character count",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to write files to, relative to the working directory. If not provided, list file content in the working directory itself.",
                ),
            },
        ),
    )


def write_file(working_directory, file_path, content):

    combined = Path(working_directory)/Path(file_path)

    cwd = Path.cwd()

    rel_check = ( 
        
        Path(file_path).resolve().is_relative_to(cwd)
        
        )

    if not rel_check:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if  not combined.parent.exists():
        combined.parent.mkdir(parents=True)


    try:

        with open(combined, "w") as f:

            f.write(content)

            return (f'Successfully wrote to "{combined}" ({len(content)} characters written)')

    except Exception as e:
        return f'Error: "{e}"'