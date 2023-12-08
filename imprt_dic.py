#code by "Code with Harry"

import os

# Replace 'path_to_directory' with the path to the directory you want to list
directory_path = 'path_to_directory'

# Check if the path exists and is a directory
if os.path.isdir(directory_path):
    # List all files and directories in the specified path
    print(f"Contents of directory '{directory_path}':")
    for item in os.listdir(directory_path):
        print(item)
else:
    print(f"'{directory_path}' is not a valid directory.")
