import os
import re

FILE_ARGUMENT = 'file_path'    # name of InArg for HPC file upload


def get_file_path_from_line(line):
    """
    Get the absolute path of a file provided as input argument to a Xircuits component
    :param line: line where the file_input param. of a component gets a value (a path from disk)
    :return: absolute path to the file
    """
    file_path = line.split('"""')[1]    # the relative file path is always between these this sequence of characters
    abs_file_path = os.path.abspath(file_path)  # absolute file path
    return abs_file_path


def get_file_name_from_line(line):
    """
    Get just the file name of a file provided as input argument to a Xircuits component
    :param line: line where the file_input param. of a component gets a value (a relative path from disk)
    :return: the file name of the file
    """
    file_path = line.split('"""')[1]    # the relative file path is always between these this sequence of characters
    file_name = os.path.basename(file_path)
    return file_name


def get_files_to_upload(xircuits_file_path):
    """
    Retrieve the list of files that need to be uploaded to the HPC.
    Also modify the compiled xircuits file, such that for the components using the uploaded files, only the file
    names are specified, not their path (relative or absolute).
    :param xircuits_file_path: path to the compiled xircuits workflow file
    :return: list containing the files that need to be uploaded to the HPC
    """
    print("Gathering input files...", flush=True)
    files_to_upload = []  # will contain the paths of all files that need to be uploaded
    new_file = []   # will contain the xircuits .py file, but keeping only the file names, not their whole relative path
    with open(xircuits_file_path) as f:
        lines = f.readlines()

    # if FILE_ARGUMENT is nowhere in the compiled .py file, don't search for it in every line
    # TODO: make this nicer
    if any(FILE_ARGUMENT in line for line in lines):
        for line in lines:
            if FILE_ARGUMENT in line:
                # store the path of the file that needs to be uploaded
                file_to_upload = get_file_path_from_line(line)
                files_to_upload.append(file_to_upload)

                # replace in the compiled .py file the relative path with the file name for `file_path` arguments
                new_line = line
                input_file_name = get_file_name_from_line(line)
                new_line = re.sub('""".*?"""', '"""' + input_file_name + '"""', new_line)
                new_file.append(new_line)
            else:
                new_file.append(line)

        # rewrite the compiled .py file:
        with open(xircuits_file_path, 'w') as f:
            f.writelines(new_file)

    return files_to_upload

