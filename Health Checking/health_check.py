#!/usr/bin/env python3

from network import *
import shutil
import psutil

def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    print('Free space: %d percent' % free)
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    print("CPU usage: %d percent" % usage)
    return usage < 75

# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything is Okay.")
else:
    print("Network checks failed")