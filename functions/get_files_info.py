import os
from pathlib import Path


def get_files_info(working_directory, directory=None):


    wd = Path(working_directory)
    d = Path(directory)

    path = wd / d

    def content(path):
        prompt = []

        for i in path.iterdir():
            print(i)
            try:
            
                contents = (
                    f"- {i.name}: file_size={i.stat().st_size} bytes, is_dir={i.is_dir()}"
                )
                prompt.append(contents)

            except OSError as e: 
                
                print(f"Error: {e}")
                
        return prompt

    return "\n".join(content(path))
