#coding=UTF-8
#Author:Winyn
'''
python的多线程是一种伪多线程，因为python的核心机制全局锁。
全局锁限制了python在任何时候都只能运行一个线程。



'''
# import threading
# import time
# def func1(p):
	# time.sleep(0.01)
	# print(p)


# for i in range(15):
	# th = threading.Thread(target = func1,args = [i])
	# th.start()
	# th.join()
	
# print('end')
'''
习题一：已知列表 info = [1,2,3,4,55,233]

生成6个线程对象,每次线程输出一个值，最后输出："the end"。


习题二：已知列表 
urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com']
 用多线程的方式分别打开列表里的URL，并且输出对应的网页标题和内容。

习题三：已知列表
urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com']
 用多线程的方式分别打开列表里的URL，输出网页的http状态码。

'''


#----------------------------------------------------------------------------------------
import threading
import time
info = [1,2,3,4,55,233]
def output(i):
	# time.sleep(0.01)
	print(info[i])
ts=[]
l = range(0,len(info))
for i in l:
	th = threading.Thread(target = output,args =[i])
	th.start()
	ts.append(th)

for each in ts:
	each.join()

print('the end')	
	
#----------------------------------------------------------------------------------------
def get_code(urlinfo):
	import urllib.request
	for each in urlinfo:
		code =urllib.request.urlopen(each).code
		print( code)
ts = []		
for i in range(0,6):
	th = threading.Thread(target = get_code,args =[['http://www.sohu.com','http://www.163.com','http://www.sina.com']])
	th.start()
	ts.append(th)

for each in ts:
	each.join()	

#----------------------------------------------------------------------------------------

