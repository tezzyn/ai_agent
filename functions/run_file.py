from pathlib import Path
import subprocess
import time
import sys
from subprocess import Popen, SubprocessError


def run_python_file(working_directory, file_path, args=[]):

    combined = Path(working_directory)/Path(file_path)

    cwd = Path.cwd()
    #print(cwd)

    rel_check = ( 
        
        Path(file_path).resolve().is_relative_to(cwd)
        
        )

    if not rel_check:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not Path(file_path).exists():
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'


    # print(Path(file_path).resolve().is_relative_to(cwd))
    

    prompt = []

    if len(args) != 0:
        prompt = ["uv", "run",f"{combined}",args[0]]
    else:
        prompt = ["uv", "run",f"{combined}"]

   
    try:
   
        process = subprocess.run(
            prompt, 
            #capture_output=True, 
            #shell=True, 
            # stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True,
            timeout=20,
            check=True,
            )

        
        # print(process.stdout)
        #print(process.stderr)
    except subprocess.SubprocessError as e:
        return(e)

    return process.stdout
    



