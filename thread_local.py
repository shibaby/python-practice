import threading

local_school = threading.local()

def get_student():
    stu = local_school.student
    print('Student 【%s】 in 【%s】' % (stu, threading.current_thread().name))

def task(name):
    local_school.student = name
    get_student()

if __name__ == '__main__':
    t1 = threading.Thread(target = task, args = ('Alers',), name = 'Thread-A')
    t2 = threading.Thread(target = task, args = ('Beail',), name = 'Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()