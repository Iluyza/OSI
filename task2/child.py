import os
import sys
import time
import random

pid = os.getpid()
ppid = os.getppid()

print(f'Child[{pid}]: I am started. My PID {pid}. Parent PID {ppid}.')

s = int(sys.argv[1])
time.sleep(s)
print(f'Child[{pid}]: I am ended. PID {pid}. Parent PID {ppid}.')

exit_status = random.choice([0, 1])
os._exit(exit_status)
