from multiprocessing import Process, Pool
import os

def task(name):
    print('\tSon process 【%s】 is running , pid: %s, parent_pid: %s' % (name, os.getpid(), os.getppid()))

if __name__ == '__main__':
    sun_process = Process(target = task, args = ('子线程1',))
    print('\nSTART')
    sun_process.start()
    sun_process.join()
    print('END\n')

import time, random

if __name__ == '__main__':
    print('\nParent process pid is: %s' % os.getpid())
    pool = Pool(5)

    for i in range(1, 10):
        pool.apply_async(task, args = (i, ))

    print('Wating for all subprocesses done...')
    pool.close()
    pool.join()
    print('All subprocesses has done.\n')