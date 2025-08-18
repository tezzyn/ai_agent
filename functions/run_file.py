from pathlib import Path
import subprocess
import time
import sys
from subprocess import Popen


def run_python_file(working_directory, file_path, args=[]):

    combined = Path(working_directory)/Path(file_path)

    cwd = Path.cwd()
    #print(cwd)

    rel_check = ( 
        
        Path(file_path).resolve().is_relative_to(cwd)
        
        )

    if not rel_check:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not combined.parent.exists:
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'


    #print(args[0])
    print(cwd)


    try:
        process = subprocess.run(
            ["uv", "run",f"{combined}",args[0]], 
            #capture_output=True, 
            #shell=True, 
            # stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True,
            timeout=20,
            )
        
        if args:
            process.input = args[0]
        
        print(process.stdout)
        #print(process.stderr)
    except ChildProcessError as e:
        return(e)


    



