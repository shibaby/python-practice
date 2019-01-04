import random,time,queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

task_queue = queue.Queue()
result_queue = queue.Queue()

def return_task_queue():
    return task_queue # 不能直接返回queue.Queue()创建出来的实例

def return_result_queue():
    return result_queue

def main():
    QueueManager.register('get_task_queue', callable = return_task_queue) # 不支持匿名函数
    QueueManager.register('get_result_queue', callable = return_result_queue)
    manager = QueueManager(address = ('127.0.0.1', 5000), authkey = b'abc') # widows中ip地址不能为空
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(1, 1000)
        print('Put task %d' % n)
        task.put(n)

    print('\nTrying to get results...\n')

    try:
        for i in range(10):
            r = result.get(timeout = 10)
            print('Result: %s' % r)
    except queue.Empty:
        print('\nresult queue is empty')

    manager.shutdown()
    print('\nmaster exit...')

if __name__ == '__main__':
    main()