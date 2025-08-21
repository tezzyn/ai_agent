from pathlib import Path
import subprocess
import time
import types
import sys
from subprocess import SubprocessError


def run_python_file(working_directory, file_path, args=[]):


    # schema_get_files_info = types.FunctionDeclaration(
    #     name="run_python_file",
    #     # description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    #     parameters=types.Schema(
    #         type=types.Type.OBJECT,
    #         properties={
    #             "directory": types.Schema(
    #                 type=types.Type.STRING,
    #                 description="The directory to run files from, relative to the working directory. If not provided, lists files in the working directory itself.",
    #             ),
    #         },
    #     ),
    # )

    combined = Path(working_directory)/Path(file_path)

    cwd = Path.cwd()

    rel_check = ( 
        
        Path(file_path).resolve().is_relative_to(cwd)
        
        )

    if not rel_check:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not Path(file_path).exists():
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    

    prompt = []

    if len(args) != 0:
        prompt = ["uv","run",f"{combined}",args[0]]
    else:
        prompt = ["uv", "run",f"{combined}"]


    try:
        commands = ["python", combined.absolute()]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=cwd,
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"

    



