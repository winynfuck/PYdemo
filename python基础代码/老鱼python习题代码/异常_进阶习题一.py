#coding=UTF-8
#@Author:Winyn
'''
1 定义一个函数func(filename) filename:文件的路径，
函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误。

2 定义一个函数func(urllist)   urllist:为URL的列表，
例如：['http://xx.com','http://www.xx.com','http://www.xxx.com'...] 

函数功能：要求依次打开url，打印url对应的内容，
如果有的url打不开，则把url记录到日志文件里，并且跳过继续访问下个url。

3 定义一个函数func(domainlist)   domainlist:为域名列表，
例如：['xx.com','www.xx.com','www.xxx.com'...]
函数功能：要求依次ping 域名，如果ping 域名返回结果为：request time out，
则把域名记录到日志文件里，并且跳过继续ping下个域名。（提示用os模块的相关方法）

'''
import logging
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler(r'D:\A\log.txt')
formatter = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s')
handler.setFormatter(formatter)
#控制台输出
console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(handler)
logger.addHandler(console)
#-----------------------------------------------------------------------------------------
def func1(filename):
	
	'该方法打开文件并返回文件内容'
	try:
		with open(filename,'r') as f:
			return f.read()
	except FileNotFoundError:
		logger.info('Error:没有找到错误！')
		
	except OSError:
		logger.info('Error:路径中要注意\的转义作用')
		
		
		
		
#-----------------------------------------------------------------------------------------
def func2(urllist):
	import urllib.error,sys
	import urllib.request as ur
	for each_url in urllist:
		try:
			data = ur.urlopen(each_url)
			text = data.readlines()		
		except urllib.error.HTTPError:
			print(sys.exc_info())
			logger.info('Error:HTTP访问页面出错!'+'--url:'+each_url)	
		except urllib.error.URLError:
			print(sys.exc_info())
			logger.info('Error:打不开网页!'+'--url:'+each_url)
		continue
		
		
#-----------------------------------------------------------------------------------------
def func3(domainlist):
	'该方法用于鉴别列表中ping outtime的域名'
	import os,sys
	for yuming in domainlist:
		try:
			os.system('ping ' +yuming)
		except :
			print(sys.exc_info())
			logger.info('Error:请求超时!'+'--url:'+yuming)
		continue
		
			

			
			
		
	

if __name__ =='__main__':
	print(func1(r'D:\A\new.txt'))
	func2(['https://www.baisdu.com','http://www.xx22.com','http://www.x22xx6.com'])
	#func3(['xx2.com','www.x2x.com','www.x11xx.com'])
	
	
	