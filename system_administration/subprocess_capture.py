#!/usr/bin/env python

import sys
# Need to import PIPE and STDOUT
from subprocess import check_output, Popen, CalledProcessError, STDOUT, PIPE
from glob import glob
import shlex

"""
Capturing stdout and stderr
    Add stdout, stderr args
    Assign subprocess.PIPE
"""
if sys.platform == 'win32':
    CMD = 'cmd /c dir'
    FILES = r'data\t*'
else:
    CMD = 'ls -ld'
    FILES = 'data/t*'

cmd_words = shlex.split(CMD)
cmd_files = glob(FILES)

full_cmd = cmd_words + cmd_files

# Capture only stdout
print('--> Capture only stdout')
try:
    # checkout_output() returns stdout
    output = check_output(full_cmd)

    # stdout is returned as bytes (decode to str)
    print("Output:", output.decode(), sep='\n')
except CalledProcessError as e:
    print("Process failed with return code", e.returncode)

print('-' * 50)

# Capture stdout and stderr together
print('--> Capture stdout and stderr together')
try:
    cmd = cmd_words + cmd_files + ['spam.txt']

    # Assign PIPE to stdout, so it is captured
    # Assign STDOUT to stderr, so both are captures together.
    proc = Popen(cmd, stdout=PIPE, stderr=STDOUT)

    # Call communicate to get the input streams of the process
    # It returns two bytes objects representing stdout and stderr.
    stdout, stderr = proc.communicate()

    # Decode the stdout object to a string
    print("Output:", stdout.decode())
except CalledProcessError as e:
    print("Process failed with return code", e.returncode)

print('-' * 50)

# Capture stdout and stderr individually
print('--> Capture stdout and stderr individually')
try:
    cmd = cmd_words + cmd_files + ['spam.txt']

    # Assign PIPE to stdout and PIPE to stderr, so both are captured individually
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE)

    # Now stdout and stderr each have data
    stdout, stderr = proc.communicate()

    # Decode from bytes and output
    print("Output:", stdout.decode())
    print("Error:", stderr.decode())
except CalledProcessError as e:
    print("Process failed with return code", e.returncode)

print('-' * 50)
