import os
import sys

FILE_ARGUMENT = 'file_path'    # name of InArg for HPC file upload

# TODO: Extract this method in a utils file? (used in pyunicore_config.py and here)
def get_xircuits_file():
    """
    :return: the file name and the absolute path for the compiled workflow file
    """
    # check that compiled .xircuits file is correctly passed as argument
    file_arg = sys.argv[-1]
    print(f'Identified the executable file: {file_arg}', flush=True)

    if os.path.exists(file_arg):
        full_path = os.path.abspath(file_arg)
    else:
        print("Cannot find " + file_arg)
        full_path = None

    filename = os.path.basename(file_arg)

    return filename, full_path


def get_file_path_from_line(line):
    file_path = line.split('"""')[1]    # the relative file path is always between these this sequence of characters
    abs_file_path = os.path.abspath(file_path)  # absolute file path
    print(abs_file_path)
    return abs_file_path


def get_files_to_upload():
    file_name, file_path = get_xircuits_file()
    files_to_upload = []  # will contain the paths of all files that need to be uploaded
    with open(file_path) as f:
        lines = f.readlines()

    # if FILE_ARGUMENT is nowhere in the compiled .py file, don't search for it in every line
    # TODO: make this nicer
    if any(FILE_ARGUMENT in line for line in lines):
        for line in lines:
            if FILE_ARGUMENT in line:
                file_to_upload = get_file_path_from_line(line)
                # print(file_to_upload)
                files_to_upload.append(file_to_upload)

    return files_to_upload

