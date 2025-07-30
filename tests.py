

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

import subprocess


# print(get_files_info("calculator", "."))

# print("--------------------------------------------------------------------")

# print(get_files_info("calculator", "pkg"))

# print("--------------------------------------------------------------------")

# print(get_files_info("calculator", "/bin"))

# print("--------------------------------------------------------------------")

# print(get_files_info("calculator", "../"))

#           #


# print(get_file_content("calculator", "main.py"))

# print("--------------------------------------------------------------------")

# print(get_file_content("calculator", "pkg/calculator.py"))

# print("--------------------------------------------------------------------")

# print(get_file_content("calculator", "/bin/cat"))

# print("--------------------------------------------------------------------")

# print(get_file_content("calculator", "pkg/does_not_exist.py"))

#             #


# print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

# print("--------------------------------------------------------------------")

# print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

# print("--------------------------------------------------------------------")

# print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))


foo = ['oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo']

for i in foo:
    subprocess.run(['timeout','--kill-after=3'])
    print(i)