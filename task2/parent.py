from os import fork, getpid, wait, execv
from sys import argv
from random import randint

n = int(argv[1])
child = fork()
i = 0
while True:
    if child == 0:
        number = randint(5, 10)
        print('Сгенерированное число секунд: {0}'.format(number))
        execv('/usr/bin/python3', ['python3', 'child.py', str(number)])
    else:
        ret = wait()
        print('Дочерний процесс с PID {0} завершился. Статус завершения {1}.'.format(ret[0], ret[1]))
        i += 1
        if i < n:
            child = fork()
        else:
            break
