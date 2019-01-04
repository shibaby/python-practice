import time, queue, sys
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

def main():
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    manager = QueueManager(address = ('127.0.0.1', 5000), authkey = b'abc')
    manager.connect()

    print('worker was connected to master\n')

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(5):
        try:
            n = task.get(timeout = 1)
            print('run task %d * %d' % (n, n))
            time.sleep(1)
            result.put('%d * %d = %d' %(n, n, n * n))
        except queue.Empty:
            print('\ntask queue is empty')

    print('\nworker exit...')

if __name__ == '__main__':
    main()