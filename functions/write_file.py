from pathlib import Path



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