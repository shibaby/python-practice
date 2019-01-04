# -*- coding: utf-8 -*-
'''
a = input('Please Enter Your Age: ')
if eval(a) > 18:
    print('adult')
else:
    print('teenager')

print(eval('%d - %.2f' % (3, 1)))


#list操作：len(), append(), insert(), pop()
#tuple指向不变
height = 1.75
weight = 80.5
bmi = weight / height ** 2
if bmi < 18.5:
    print(bmi, '过轻')
elif 25 >= bmi >= 18.5:
    print(bmi, '正常')
elif 28 >= bmi >= 25:
    print(bmi, '过重')
elif 32 >= bmi >= 28:
    print(bmi, '肥胖')
else:
    print(bmi, '严重肥胖')

for x in range(1, 10, 3):
    if x >= 7: 
        print(x, end = '')
    else:
        print(x, end = ',')
'''
from school.student import *

alier = Student('Alier', 55)
alier.name = 'Biler'
print (alier.name)
print (alier._Student__name)
alier.print_stu()

def nop():
    pass

print('----------------------------------------------')

from school.person import *
from school.man import *
from school.woman import *
from school.dog import *

person = Person()
man = Man()
woman = Woman()
dog = Dog()
print(isinstance(person, Person))
print(isinstance(man, Person))
print(isinstance(woman, Person))
print(isinstance(person, Man))
print(isinstance(person, Woman))
print(isinstance(man, object))

print('----------------------------------------------')

def speak(person):
    person.speak()

speak(person)
speak(man)
speak(woman)
speak(dog)

print('----------------------------------------------')

person.age = 45
man.score = 99
print(person.age)
print(man.score)

print('----------------------------------------------')

person2 = Person()
person.name = 'Miler'
print(person.name)

print('----------------------------------------------')

from school.week_day import *
print(WeekDay.Sun.value == 0)
print(WeekDay.Sun.value == '0')
print([[x, v, v.name, v.value] for x, v in WeekDay.__members__.items()], sep='\n')

print('----------------------------------------------')

def fn(self, name = 'world'):
    print('Hello %s' % (name))

#Hello = type('Hello', (object, ), {'hello': fn})  #type()函数动态创建类
Hello = type('Hello', (object, ), {'hello': lambda self, name = 'world': print('Hello %s' % (name))})
hello = Hello()
hello.hello()
hello.hello('Baby')

print('----------------------------------------------')

import logging

logging.basicConfig(level = logging.INFO)
def divid(value):
    try:
        #value / 0
        raise ValueError('raise ValueError')
        print('Try Block Is Finished')
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except ValueError as ve:
        logging.info('ValueError: %s' % ve)
    except Exception:
        print('Exception')
    else:
        print('NoError')
    finally:
        print('Finally Always execute')
divid(10)

print('----------------------------------------------')

with open('./school/week_day.py') as f:
    #print(f.read())
    #print(dir(f))
    print(f.tell())
    
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
    
    for line in f.readlines():
        print(line.strip())

with open('./school/write.py', 'wb+') as f:
    f.write(bytes('This is first line 第一行：以二进制对文件进行读写操作，需要将内容按指定编码进行编码、解码', 'utf-8'))

with open('./school/write.py', 'r+', encoding = 'utf-8') as f:
    print(f.read())

with open('./school/write.py', 'a+', encoding = 'utf-8') as f:
    f.write('\nThis is second line 第二行：以非二进制对文件进行读写操作，最好在打开时指定编码格式')

with open('./school/write.py', 'rb+') as f:
    print(f.read().decode())

print('----------------------------------------------')

import os

print(os.name)
print(os.environ.get('PATH'))
print(os.path.abspath('./'))
dir_name = os.path.join(os.path.abspath('.'), 'testdir')
print(dir_name)

if os.path.exists(dir_name) and os.path.isdir(dir_name):
    os.rmdir(dir_name)
os.mkdir(os.path.join(os.path.abspath('.'), 'testdir'))

if not os.path.exists('./io'):
    os.rename('testdir', 'io')

print(os.path.split('./school/week_day.py'))
print(os.path.splitext('./school/week_day.py'))

print([x for x in os.listdir()])
print([x for x in os.listdir() if os.path.isdir(x)])
print([x for x in os.listdir() if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

print('----------------------------------------------')

import pickle

d = dict(name = 'Bllier', age = 20, score = 86)
d_bytes = pickle.dumps(d);

with open('./io/pickle_dumps.txt', 'wb+') as f:
    print(f.write(d_bytes))

with open('./io/pickle_dumps.txt', 'rb+') as f:
    print(pickle.loads(f.read()))

with open('./io/pickle_dump.txt', 'wb+') as f:
    pickle.dump(d, f)

with open('./io/pickle_dump.txt', 'rb+') as f:
    print(pickle.load(f))

print('----------------------------------------------')

import json

d_json = json.dumps(d)
print(d_json)
print(json.loads(d_json))

with open('./io/json_dump.txt', 'w') as f:
    json.dump(d, f)

with open('./io/json_dump.txt', 'r') as f:
    print(json.load(f))

alier_json = json.dumps(alier, default = lambda obj: obj.__dict__)
print(alier_json)
new_alier = json.loads(alier_json, object_hook = lambda obj: Student(obj['_Student__name'], obj['_Student__age']))
new_alier.print_stu()

print('----------------------------------------------')

import re

if(re.match('^\d{3}\-?\d{3,8}$', '015-66523648')):
    print('SUCCESS')
else:
    print('FAIL')

print('a b  c   d >>>', 'a b  c   d'.split(' '))
print('a, b:  c   d >>>', re.split(r'[\s\,\:]+', 'a, b:  c   d'))
print([x for x in re.match(r'^(\d{3})(\-)(\d{3,8})$', '010-5258').groups()])

print('----------------------------------------------')

from datetime import datetime, timedelta

now = datetime.now()
print(now)
print(type(now))

time = datetime(2019, 1, 3, 13, 15, 39)
print(time)
print(time.timestamp())
print(datetime.fromtimestamp(1546492539.333))
print(datetime.strptime('2018-12-19 00:23:30', '%Y-%m-%d %H:%M:%S'))
print(datetime.strftime(now, '%Y-%m-%d %H:%M:%S'))
print(now + timedelta(hours = 3, days = 1, minutes = 10))

print('----------------------------------------------')

from collections import namedtuple

Point = namedtuple('Points', ['x', 'y'])
p = Point(3, 'x')
print(p.y)
print(Point, p)

print('----------------------------------------------')

from urllib import request, parse

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print(k, ':', v)
	print('Data:', data.decode('utf-8'))
	
login_data = parse.urlencode([
	('identifier', 'ysh_PC'),
	('secret', '123456')
])

req = request.Request('http://localhost:52500/powerMobileApp/login')
req.add_header('Origin', 'http://localhost:52500')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
req.add_header('Referer', 'http://localhost:52500/powerMobileApp/resources/torch/login')

with request.urlopen(req, data = login_data.encode('utf-8')) as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print(data)
	
with open('data.json') as f:
	data_json = f.read()
	data_dict = json.loads(data_json)
	print(data_json)
	print(data_dict['data'][0])

print('----------------------------------------------')

def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print('【Consumer】 Consuming %s...' % n)
		r = '200 OK'
	
def produce(c):
	c.send(None) #用来启动consumer生产器
	for n in range(1, 6):
		print('【Producer】 Producing %s...' % n)
		r = c.send(n)
		print('【Producer】 Consumer return: %s' % r)
	c.close()
		
c = consumer()
produce(c)