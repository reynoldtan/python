#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    '''Check system health: disk usage'''
    du = shutil.disk_usage(disk)
    # Free disk space is free space divided by total space times 100
    free = du.free / du.total * 100
    # Notify if there is just 20% free space available.
    return free > 20

def check_cpu_usage():
    '''Check system health: CPU usage'''
    # 1 second test.
    usage = psutil.cpu_percent(1)
    # CPU is okay if usage is less than 75%.
    return usage < 75


disk_health = check_disk_usage('/')
cpu_health = check_cpu_usage()
if not disk_health or not cpu_health:
    print('ERROR!')
else:
    print('All is okay!')
