import asyncio

'''
	Python3.4语法 利用@asynicio.coroutine把生成器标记为协程
@asyncio.coroutine
def hello():
	print('Hello world')
	r = yield from asyncio.sleep(1)
	print(r)
	print('Hello world again')
'''

'''
	Python3.5语法 利用async把生成器标记为协程，用 await 代替 yield from
'''	
async def hello():
	print('Hello world')
	r = await asyncio.sleep(1)
	print(r)
	print('Hello world again')
	
loop = asyncio.get_event_loop()
loop.run_until_complete(hello())

print('-----------------------------------')

tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()