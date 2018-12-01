'''
在 python中，else语句不仅仅可以用于if语句，而且可以用于for,while,try 语句

if 条件:
	条件为真执行语句
else:
	条件为假执行语句
即要么怎样，要么不怎样
	
while 条件:
	条件为真执行循环体
else:
	如果实现了循环并且没有break，执行语句
即干完了能怎样，干不完就别想怎样


try:
	语句
except:
	语句
else:
	语句
即没有问题，那就干吧

	

'''
#求一个数的最大公约数
def showMaxFactor(num):
	count = 1
	maxg = []
	while count <=(num//2):
		if num % count ==0:
			maxg.append(count)
		count +=1
			
	else:
		if max(maxg) != 1 and max(maxg) != num:
			print('%d 的最大公约数是：%d' %(num,max(maxg)))
		else:
			print('这个数是素数')

num = int(input('请输入一个数：'))
showMaxFactor(num)


# try:
	# int('abc')
# except 	ValueError as reason:
	# print('出错了!'+str(reason))
# else:
	# print('没有任何问题!')
	
	
	
	
'''
使用with语句避免文件打开忘记关闭的尴尬了，with会自动考虑文件关闭的问题

'''


'''
try:
	f =open('data.txt','w')
	for eachline in f:
		print(eachline)
except 	OSError as reason:
	print('出错了'+str(reason))
finally:
	f.close
'''
#以上可以用with语句写
try:
	with open('data.txt','w') as f:
		for eachline in f:
			print(eachline)
except 	OSError as reason:
	print('出错了'+str(reason))





