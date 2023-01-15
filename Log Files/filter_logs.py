#!/usr/bin/env python3

# LOG FILE - logs.log
# Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)
# Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)
# Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)
# Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)
# Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"
# Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)
# Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)

import re
import sys

# Get USER values in log file - who starts the cron jobs.
logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
    for line in f:
        if 'CRON' not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
print(usernames)
      
#!/usr/bin/env python3
#import sys
#import re
import os

# Log file format 
# Month Day hour:minute:second mycomputername "process_name"["random 5 digit number"] "ERROR/INFO/WARN" "Error description"

def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
    file.close()
  return returned_errors
  
def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)