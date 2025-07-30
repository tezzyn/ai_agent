from pathlib import Path


def run_python_file(working_directory, file_path, args=[]):


    combined = Path(working_directory)/Path(file_path)

    cwd = Path.cwd()

    rel_check = ( 
        
        Path(file_path).resolve().is_relative_to(cwd)
        
        )

    if not rel_check:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not combined.parent.exists:
        return f'Error: File "{file_path}" not found.'
    
    if not Path(file_path).name().endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    