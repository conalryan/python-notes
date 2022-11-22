#!/usr/bin/env python

print('-' * 25, 'READ', '-' * 25)


# read() Store lines in an array
f = open("data/some_file.txt", "r")
print("[f.read()]\n" + f.read())
f.close()

# read(n)
f = open("data/some_file.txt", "r")
print("[f.read(10)]\n" + f.read(10))
f.close()

# readlines()
f = open("data/some_file.txt", "r")
print("[f.readlines()[0]]\n" + f.readlines()[0])
f.close()

# readline(n)
f = open("data/some_file.txt", "r")
print("[f.readline(2)]\n" + f.readline(2))
f.close()

# Loop lines of the array
f = open("data/some_file.txt", "r")
my_list = []
for line in f:
    my_list.append(line)

print("[Read lines into an array]")
print(my_list)

# DON'T FORGET TO CLOSE THE FILE
# Better to use with keyword of auto-close
f.close()

with open('data/mary.txt') as txt_in:
    # .read() will load entire file into memory as single item including new line chars
    all_content = txt_in.read()
    print(all_content)

with open('data/mary.txt') as txt_in:
    # .readlines() will read line by line into a list
    all_lines = txt_in.readlines()
    print(all_lines)


"""
Write file
    "w"

Remember 'w' will overwrite the if it exists so be CAREFUL!
"""
print('-' * 25, 'WRITE', '-' * 25)
f = open("data/test.txt","w")

f.write("I am a test file.\n")  # to break line add \n at end of line
f.write("Maybe someday, he will promote me to a real file.")
f.write("Man, I long to be a real file")
f.write("and hang out with all my new real file friends.")

f.close()


"""
Append to file
    "a"
"""
print('-' * 25, 'APPEND', '-' * 25)
f = open("data/test.txt", "a")

f.write("appending this string but it will be on the same line, unless the previous line had '\\n'")
f.write("\nappended this line\n")

f.close()

def save_file():
    a_value = "save me to the file"
    try:
        f = open("data/some_file.txt", "a")  # 'a' flag will append (and create a file if it doesn't exist)
        f.writelines(a_value + "\n")
        f.close()  # must close file to avoid memory leaks
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open("data/some_file.txt", "r")
        for line in f.readlines():
            print(line)
        f.close()
    except Exception:
        print("Could not read file")

#read_file()


"""
CSV
"""
print('-' * 25, 'CSV', '-' * 25)
import csv

# with keyword
# Automatically closes file handle when code block exits
#
# with open('example.csv') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     for row in reader:
#         print(row)
#         print(row[0])
#         print(row[0],row[1],row[2],)

with open('data/example_tab_delimiter.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        print(row)
        #print(row[0])
        #print(row[0],row[1],row[2])

"""
JSON
"""
print('-' * 25, 'JSON', '-' * 25)
import json
#
# with keyword
#     Auto closes file handler after block executes.
#
# open keyword
#     open('some file path', '<flag>')
#     r - read
#     w - write
#
# json
#     json.load(<some file>)
with open('data/example.json', 'r') as jsonfile:
    # Store json in local object.
    obj = json.load(jsonfile)

    with open('data/example_out.txt', 'w') as outputfile:
        # Write object to file.
        outputfile.write(obj['name'] + "'s Hobbies:\n")

        # Loop over object properties and write to file.
        for hobby in obj['hobbies']:
            outputfile.write(hobby + "\n")

"""
re - Regular Expression Operations
https://docs.python.org/3.6/library/re.html?highlight=rege#re.regex.pattern

"""
import re
import os

for file in os.listdir('.'):
    match = re.match("[a-z]{4}_[a-z]{4}.txt", file)
    if match:
        print(file)
