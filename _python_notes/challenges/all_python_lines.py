#!/usr/bin/env python

import os

"""
Find all Python files (.py) in the root directory of the project and count the total
number of lines in all of them.
"""

START_DIR = "."  # Start in the root of the project


def main():
    total_lines = 0
    for curr_dir, sub_dirs, files in os.walk(START_DIR):
        for file in files:
            # Print size of every python file whose name starts with "c"
            if file.endswith('.py'):
                full_path = os.path.join(curr_dir, file)
                with open(full_path, 'r') as file_in:
                    lines = file_in.readlines()
                    total_lines += len(lines)
    print(total_lines)


if __name__ == '__main__':
    main()