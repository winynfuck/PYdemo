#coding=UTF-8
#Author:Winyn
'''
异常习题：
 
 一 编写with操作类Fileinfo()，定义__enter__和__exit__方法。完成功能：

 1.1 在__enter__方法里打开Fileinfo(filename)，并且返回filename对应的内容。如果文件不存在等情况，需要捕获异常。

 1.2 在__enter__方法里记录文件打开的当前日期和文件名。并且把记录的信息保持为log.txt。内容格式："2014-4-5 xxx.txt"


 二：用异常方法，处理下面需求：

 info = ['http://xxx.com','http:///xxx.com','http://xxxx.cm'....]任意多的网址

 2.1 定义一个方法get_page(listindex) listindex为下标的索引，类型为整数。 函数调用：任意输入一个整数，返回列表下标对应URL的内容，用try except 分别捕获列表下标越界和url 404 not found 的情况。 

 2.2 用logging模块把404的url，记录到当前目录下的urlog.txt。urlog.txt的格式为：2013-04-05 15:50:03,625 ERROR http://wwwx.com 404 not foud、


 三：定义一个方法get_urlcontent(url)。返回url对应内容。

 要求：
 
 1自己定义一个异常类，捕获URL格式不正确的情况，并且用logging模块记录错误信息。

 2 用内置的异常对象捕获url 404 not found的情况。并且print 'url is not found'


 做为这周的习题。


'''
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
#--------------------------------------------------------------------------------------
class Fileinfo():
	def __init__(self,filename):
		self.filename = filename
	def __enter__(self):
		try:
			with open(self.filename,'r')as f:
				return f.read()
		except FileNotFoundError:
			return '文件不存在'
			logger.info('文件不存在！')
	def __exit__(self,type,value,traceback):
		if self.__enter__() !='文件不存在':
			from datetime import date
			nowtime =str(date.today())
			logger.info(nowtime +' '+self.filename)
			
#---------------------------------------------------------------------------------------
def get_page(listindex):
	import urllib.request
	import urllib.error
	import time
	info = ['http://xxx.com','http:///xxx.com','http://xxxx.cm','http://www.baidu.com']
	#判断listindex是不是整型
	if not isinstance(listindex,int):
		return '请输入一个整数'
	#返回列表对应url
	try:
		#捕获下标越界
		url = info[listindex]
		print(url)
		f = urllib.request.urlopen(url)
		
		return f.read()
	except IndexError:
		return '下标越界了'
	except urllib.error.URLError:
		
		nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
		logger.info(str(nowtime)+'Error '+url+'404 not found')
		return 'url 404  not found'#return 必须放在最后，否则前面的不会执行
	
			
			
#-------------------------------------------------------------------------------
class MyException(Exception):
	def __init__(self,message):
		self.message = message
def get_urlcontent(url):
	
	#判断URL格式是否正确，不正确则捕获
	try:
		from urllib.parse import urlparse
		url_tuple =urlparse(url)
		print(url_tuple[0].split('='))
		if (url_tuple[0].split('=') not in ['http','https','ftp','smtp']) or ('www' not in url_tuple[1].split('=')):
			raise MyException('URL格式错误')
	except MyException:
		return 'URL格式错误'
		logger.info(url +'  Error:URL格式错误！')

	#打开url并返回内容，打不开则捕获异常
	try:
		import urllib.request
		import urllib.error
		f =urllib.request.urlopen(url)
		return f.read()
	except urllib.error.URLError:
		return 'url is not found'
		logger.info('url 404 not found'+ url)
	
#测试

if __name__=='__main__' :
	# with Fileinfo(r'D:\A\new.txt') as f:
		# print(f)
	#print(get_page(2))
	print(get_urlcontent('hs://www.baidu.com'))
			
		
