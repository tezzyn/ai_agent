from pathlib import Path
import subprocess
import time
import sys
from subprocess import SubprocessError


def run_python_file(working_directory, file_path, args=[]):

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
        prompt = ["uv", "run",f"{combined}",args[0]]
    else:
        prompt = ["uv", "run",f"{combined}"]

    try:
   
        process = subprocess.run(
            prompt, 
            capture_output=True, 
            # shell=True, 
            text=True,
            timeout=5,
            check=True,
            )
        
        
        

        # if process.returncode != 0:

        #     return f"STDERR:\n {process.stderr}"
        # elif process.stdout != '':
        #     return f"STDOUT:\n {process.stdout}" 
        # else:
        #     return "No output produced."

        
        #print(process.stdout)
        # print(process.stderr)
    except subprocess.SubprocessError as e:
        return(e)
    
     
    if process.returncode != 0:

        return f"STDERR:\n {process.stderr}"
    elif process.stdout != '':
        return f"STDOUT:\n {process.stdout}" 
    else:
        return "No output produced."


    



