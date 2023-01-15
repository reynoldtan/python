#!/usr/bin/env python3
name = input("Please enter your name: ")
print("Hello, " + name)

def to_seconds(hour, minutes, seconds):
  return hours*3600+minutes*60+seconds

print("Welcome to this time converter")

cont = "y"
while(cont.lower() == 'y'):
  # Input returns string, use int() to convert to integer.
  hours = int(input("Enter the number of hours: "))
  minutes = int(input("Enter the number of minutes: "))
  seconds = int(input("Enter the number of seconds: "))

  print("That is {} seconds".format(to_seconds(hours, minute, seconds)))
  print()
  cont = input("Do you want to do another conversion? [y to continue] ")

print("Good bye!")

# I/O Streams
# STDIN, STDOUT, STDERR
data = input("This is stdin: ")
print("This is stdout: " + data)
print("This is stderr: " data * 20)

# Environment Variables
import os
print("HOME: " + os.environ.get("HOME", ""))

# Command-line Arguments and Exit Status
import sys
print(sys.argv)
# $ ./script.py one two three
# ['./script.py', 'one', 'two', 'three']

filename = sys.argv[1]
if not os.path.exists(filename):
  with open(filename, 'w') as f:
    f.write('New file created')
else:
    print("ERROR")
    # Exit code 0 is successful and > 0 is error
    sys.exit(1)