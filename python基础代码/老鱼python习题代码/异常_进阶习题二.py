#coding=UTF-8
#Author:Winyn
'''
习题：

1 定义一个函数func(filename) filename:为文件名，用with实现打开文件，并且输出文件内容。

2 定好一个函数func(listinfo) listinfo:为列表，
listinfo=[133,88,33,22,44,11,44,55,33,22,11,11,444,66,555] 
返回一个列表包含小于100的偶数，并且用assert来断言
返回结果和类型。

3 自己定义一个异常类，继承Exception类, 捕获下面的过程：
判断raw_input()输入的字符串长度是否小于5，
如果小于5，比如输入长度为3则输出:" The input is of length 3,expecting at least 5'，
大于5输出"print success'

'''
#------------------------------------------------------------------------------------------
#logger的配置
import logging
#定义一个logging的对象
logger = logging.getLogger(__name__)
#声明下logging存储的文件位置
hdlr = logging.FileHandler(r'D:\A\log.txt')
#定义日志存储的格式
formatter = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s')
hdlr.setFormatter(formatter)
#将文件对象放到日志对象里面
logger.addHandler(hdlr)
#设置日志的等级
logger.setLevel(level = logging.INFO)

def func1(filename):
	'该方法返回文件中的内容'
	try:
		with open(filename,'r') as f:
			return f.read()
	except FileNotFoundError:
		logger.info('Error:文件未找到！')

#------------------------------------------------------------------------------------------
def func2(listinfo):
	'该方法返回列表中小于一百的偶数'
	#判断listinfo是否是个列表
	if not isinstance(listinfo,list):
		return '请输入一个列表！'
	num = []
	#找出列表中偶数元素
	for each in listinfo:
		if isinstance(each,int) and each < 100 and each % 2 ==0 :
			num.append(each)
	return num
		
#------------------------------------------------------------------------------------------	
class Ex(Exception):
	'自定义异常'
	def __init__(self,error,message):
		self.error = error
		self.message = message



	
		
		
		
if __name__=='__main__':
	func1(r'D:\A\none.txt')
	#print(func1(r'D:\A\log.txt'))
	assert func2([133,88,33,22,44,11,44,55,33,22,11,11,444,66,555])==[88, 22, 44, 44, 22, 66]
	assert type(func2([133,88,33,22,44,11,44,55,33,22,11,11,444,66,555])) ==list
	a = input('请输入一个长度大于5的字符串')
	if len(a)< 5:
		raise Ex(IOError,'The input is of length %d,expecting at least 5'%len(a))
	else:
		print('print success')
		
	
	
	