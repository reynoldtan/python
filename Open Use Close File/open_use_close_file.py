#!/usr/bin/env python3
import os
iport datetime

# OPEN
file = open('spider.txt')

# USE
# Prints the first line and set the internal 
# line pointer to the next line.
print(file.readline())
# Print next line and update line pointer.
print(file.readline())
# From the current line pointer, print all lines.
print(file.read())

# CLOSE
file.close()

# Close file automatically using with.
with open('spider.txt') as file:
    print(file.readline())

# Iterating through Files.
with open('spider.txt') as file:
    for line in file:
        print(line.strip().upper())

file = open('spider.txt')
# readlines() with s.
lines = file.readlines()
file.close()        

# Process lines.
# This may take up huge resource when file is large.
lines.sort()
print(lines)

# OPEN FILE MODES:
# https://docs.python.org/3/library/functions.html#open
# r - read.
# w - write.
# a - append.
# r+ - read + write.

# REMEMBER: when opening a file in w mode and file already
# exits, the contents will be deleted as soon as the file is opened.
with open('spider.txt', 'a') as file:
    file.write('The end')


# Using os module:
#  os.remove('spider.txt')
#  os.rename('spider.txt', 'spider2.txt')
#  os.path.exists('spider2.txt')
#  os.path.getsize('spider2.txt')
#  os.path.isfile('spider2.txt')
#  os.path.abspath('spider2.txt')

os.path.getmtime('spider.txt')
# This will return a UNIX timestamp - # seconds since
# January 1, 1970 (start publishing unix timestamps and
# there could be no file created before this date)

# Using datetime module to make the timestamp readable.
timestamp = os.path.getmtime('spider.txt')
datetime.datetime.fromtimestamp(timestamp)