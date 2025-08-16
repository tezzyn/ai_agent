from pathlib import Path
import subprocess, shlex 
import time


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
    


    foo = subprocess.Popen(f"uv run {Path(combined)}".split())

    uv_process = subprocess.Popen(foo,args)
    
    
    out,err = uv_process.communicate(timeout=5)

    print(uv_process)

    # if sub.returncode != 0:
    #     return f"Error: {sub.stderr}"


    # try:
    #     s_run = subprocess.run(f"uv run {combined}".split(), timeout=5, cwd=cwd, capture_output=True, text=True)
    #     return (s_run.decode())
    # except subprocess.TimeoutExpired:
    #     print("The command timed out.")
    
    
    # sub = subprocess.run(
    #     "uv run run_file.py".split(),
    #     timeout=10,
    #     )

    # print(sub.stderr, sub.stdout)