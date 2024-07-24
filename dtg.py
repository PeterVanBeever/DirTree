import os
from pathlib import Path
# create a function that list directory tree
# os walk


def directory_tree_generator(start_directory):
    for root, directories, files in os.walk(start_directory):
        print(f"Directory: {root}")
        for file in files:
            print (f"  File: {file}")


directory_tree_generator('/Users/peter/Dev/DirTree/test')


def directory_tree_gen_pathlib(start_directory):
    path_object = Path(start_directory)
    for file_path in path_object.rglob('*'):
        if file_path.is_file():
            print(f"File: {file_path}")
        elif file_path.is_dir():
            print (f"Directory: {file_path}")

directory_tree_gen_pathlib('/Users/peter/Dev/DirTree/test')    