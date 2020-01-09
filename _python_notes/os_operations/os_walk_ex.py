#!/usr/bin/env python

import os

"""
os.walk()
    Walk a directory tree.
    Provides iterator for a directory and all subdirectories.
    For each directory returns tuple(directory_abs_path, subdirectories_relative_names, files_relative_names)
"""

START_DIR = "."  # Start in the root of the project


def main():
    # Don't use dir as var name when looping through the iterator, it will conflict with python builtin dir function.
    for currdir, subdirs, files in os.walk(START_DIR):
        for file in files:
            # Print size of every python file whose name starts with "c"
            if file.endswith('.py') and file.startswith('c'):
                os.path.abspath(file)
                with open(os.path.abspath(file), 'r') as file_in:
                    print(file)

                # Use os.path.join() to put together the directory and the file or subdirectory name.
                full_path = os.path.join(currdir,file)
                file_size = os.path.getsize(full_path)
                print("{:8d} {:s}".format(file_size, full_path))


if __name__ == '__main__':
    main()
