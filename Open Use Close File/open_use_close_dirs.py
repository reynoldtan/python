#!/usr/bin/env python3
import os

# Current DIR.
print(os.getcwd())

# Create DIR.
os.mkdir('new_dir')

# Change DIR.
os.chdir('new_dir')
print(os.getcwd())

# Remove DIR.
# MUST BE EMPTY DIR.
os.rmdir('new_dir')

# List files in a DIR.
os.listdir('dir')

dir = 'my_dir'
for files in os.listdir(dir):
    # Join the dir/path to the filename.
    # will ensure that it will use the right char in directory
    # (Linux + iOS = / and Windows = \)
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))