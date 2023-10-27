from os import getpid, _exit
from sys import argv
from time import sleep
from random import randint

s = int(argv[1])
print('Запущена программа child в процессе с {0} - PID с аргументом {1}'.format(getpid(), s))
sleep(s)
print('Завершился процесс с {0} PID'.format(getpid()))
_exit(randint(0, 1))
