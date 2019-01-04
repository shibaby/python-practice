import time, threading

def task():
    print('Thread 【%s】 is running' % threading.current_thread().name)

    for x in range(1, 6):
        print('%s >>> %d' % (threading.current_thread().name, x))
        time.sleep(1)

    print('Thread 【%s】 END' % threading.current_thread().name)

if __name__ == '__main__':
    print('Thread 【%s】 is running' % threading.current_thread().name)
    thread = threading.Thread(target = task, name = 'NewThread')
    thread.start()
    thread.join()
    print('Thread 【%s】 END' % threading.current_thread().name)

print('----------------------------------------------')
