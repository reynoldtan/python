#!/usr/bin/env python3
import subprocess

# Print system date and time
print(subprocess.run(['date']))

# Sleep for 2 seconds
subprocess.run(['sleep', '2'])

# Run ls
subprocess.run(['ls', '/home/user/'])

# Fetch the result of the command
command = subprocess.run(['ls', 'file'])
print(command.resultcode)

# Capture result.
result = subprocess.run(['host', '8.8.8.8'], capture_output=True)
print(result.resultcode) # 0
print(result.stdout) # b'8.8.8.8.in-addr.apra domain name pointer dns.google.\n'
# b in the beginning of the output is an array of bytes and is not
# a proper string for Python. Does not know which encoding to use
# decode() uses UTF-8
print(result.stdout.decode().split())
# ['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns-google']

# Standard error.
# Remove file that does not exist.
result = subprocess.run(['rm', 'file_doesnotexist'], capture_output=True)
print(result.returncode) # 1
print(result.stdout) # b''
print(result.stderr) # b'rm: cannot remove file_doesnotexist: no such file or directory\n'
