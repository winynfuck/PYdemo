#coding=UTF-8
#Author:Winyn
'''
习题：

有10个刷卡机，代表建立10个线程，
每个刷卡机每次扣除用户一块钱进入总账中，
每个刷卡机每天一共被刷100次。账户原有500块。
所以当天最后的总账应该为1500

用多线程的方式来解决，提示需要用到这节课的内容
'''
#----------------------------------------------------------------------------------------
import threading
import time
tlock = threading.Lock()
sum = 500

def ch_sum():
	tlock.acquire
	for i in range(0,100):
		global sum
		sum +=1
	tlock.release
		#要考虑加锁的位置对性能的影响
		

ts =[]	
time1 =time.time()
for i in range(0,10):
	th = threading.Thread(target = ch_sum)
	th.start()
	ts.append(th)
	

#join方法要和start方法分开写	
for each in ts:
	each.join()
	
print(sum)
print(time.time()-time1)
#----------------------------------------------------------------------------------------
# import time,threading
# time1 =time.time()
# def a():
	# print('a.begin')
	# time.sleep(2)
	# print('a.end')
	
# def b():
	# print('b.begin')
	# time.sleep(2)
	# print('b.end')
# a()
# b()
# # tha = threading.Thread(target = a)
# # thb = threading.Thread(target = b)	
# # tha.start()
# # thb.start()
# # tha.join()
# # thb.join()
# print(time.time()-time1)
	