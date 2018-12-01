#coding=UTF-8
#Author:Winyn
'''

习题一：

定义一个生成器函数，函数里只能用yield，要求输出结果：

step 1
step 2 x=haha
step 3 y=haha

提示步骤：建立生成器对象，并且用对象的next()和send()方法来输出结果。
send()方法传入的参数是"haha"


习题二：用生成器yield实现斐波拉切数列。

'''
#-------------------------------------------------------------------------------------
# def generation():
	# x = yield 'step 1'
	# y = yield 'step 2 x =%s'%x
	# z = yield 'step 3 x =%s'%y
		
		
# t= generation()
# print(t.__next__())
# print(t.send('haha'))
# print(t.send('haha'))

'''
总结：
1.t.__next__和t.send都会返回yield后面的值
2.第一个t.send会对遇到的第一个yield赋值，第二个t.send会对遇到的第二个yield赋值

'''
#-------------------------------------------------------------------------------------
# def fblq(num):
	# '找出一个界限以内的费波列齐数列'
	# a = 0
	# b = 1
	# while b <= num:
		# yield b
		# a , b = b , a + b#先yield和后yield结果不同
		
		
# f=fblq(10000)#还是生成一个迭代器
# for i in f:
	# print(i)

# try:
	# while True:
		# print(f.__next__())
# except StopIteration:
	# pass

#-------------------------------------------------------------------------------------
'''
使用yield求一亿以后一百个素数

'''	
# import time,threading	
# tlock = threading.Lock()
def is_sus(num_int):
	'判断一个数是不是素数'
	if num_int == 1:
		return False
	if num_int == 2:
		return True
	for i in range(2,num_int):
		if num_int % i == 0:
			return False
	else:
		return True
def sus(num_int,geshu_int):
	'输出一个包含某个数之后多少个素数的列表'
	time = 0
	# tlock.acquire
	while time < geshu_int:
		if is_sus(num_int):
			time += 1
			yield(num_int)
		num_int += 1
	# tlock.release

# start = time.time()		
# # s =sus(1000,100)
# # print(s.__next__())
# # print(s.__next__())


# ts = []
# for i in range(0,10):
	# th = threading.Thread(target = sus,args =[10000000,100])
	# th.start()
	# ts.append(th)
# for each in ts:
	# each.join()


print(list(sus(10000000,100)))
print('耗时%s'%(time.time()-start))
	
	
	
