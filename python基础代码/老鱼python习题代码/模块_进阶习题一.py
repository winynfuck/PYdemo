#coding=UTF-8
#@Author:Winyn
'''
python模块的导入方式：
1.import module  常用的导入方式
2.from module import module.method  导入某个方法
3.from module import *   导入所有方法

包的概念：
包是模块的集合。例如python中的urllib就是一个包。
包也可以看作一个文件夹，因为module可以看作是一个.py文件。
定义一个包，必须在文件夹下新建一个__init__.py文件，文件内容可以为空。

如何寻找模块：
假如你要使用一个你自己写的.py文件作为模块使用，那么首先
你要让系统知道这个模块在哪里。
使用：
import sys
sys.path.append('模块的绝对路径')


如何查找第三方库：
pypi.python.org上面搜索所需要的库即可

如何查看python的标准库
doc.python.org上查看
'''
#----------------------------------------------------------------------------------------
'''
习题一：
 
1.1 用time模块获取当前的时间戳.
1.2 用datetime获取当前的日期，例如：2013-03-29
1.3 用datetime返回一个月前的日期：比如今天是2013-3-29 一个月前的话：2013-02-27


'''
import time
from datetime import datetime,timedelta
from datetime import date
print('当前的时间点是：%d s'%time.time())
print('当前的日期是：%s '%date.today())

#datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
time1 = datetime.strptime('2013-3-29','%Y-%m-%d')#日期转化为时间对象
print(time1.strftime('%y-%m-%d'))#时间对象格式化
print((time1+timedelta(days =-30)).strftime('%y-%m-%d'))#timedelta代表两个datetime之间的时间差
'''
@好坑爹：
datetime.datetime.strptime(时间，格式)这个格式居然要Y的大写
而转换后的时间对象进行格式化的y要小写。

'''



#----------------------------------------------------------------------------------------
'''
习题二:
1 用os模块的方法完成ping www.baidu.com 操作。
2 定义一个函数kouzhang(dirpwd)，用os模块的相关方法，
返回一个列表，列表包括：dirpwd路径下所有文件不重复的扩展名，
如果有2个".py"的扩展名，则返回一个".py"。

'''
import os,os.path
# os.system('ping www.baidu.com')
def kuozhan(dirpwd):
	'定义一个函数kouzhang(dirpwd)，用os模块的相关方法的扩展名'
	#判断目录是否存在
	if not os.path.exists(dirpwd):
		return '目录不存在'
	#获取目录下所有文件的名称
	file_list = os.listdir(dirpwd)

	#分离获取扩展名
	kuozhan_list = []
	for each_file in file_list:
		#判断是否是目录，如果不是目录则进行提取扩展名
		if not os.path.isdir(os.path.join(dirpwd,each_file)):
			kuozhan_list.append(os.path.splitext(each_file)[1])
		'''
		@惊喜：os.path.splitext()居然可以直接对a.txt进行分离，而不用加上绝对路径
		'''
	return set(kuozhan_list)
print(kuozhan('D://ruanjian/Anaconda'))

#----------------------------------------------------------------------------------------
'''

习题三：

定义一个函数xulie(dirname,info) 
参数：dirname:路径名，info:需要序列化的数据，
功能：将info数据序列化存储到dirname路径下随机的文件里。  
'''
def xulie(dirname,info):
	'该方法将对象进行序列化，并保存到指定文件夹下随机的文件里'
	#生成随机文件名
	import pickle	
	from datetime import date
	import random,os.path
	now_time = date.today()
	num_range = random.randint(0,1000)
	file_name =str(now_time) + '_love_'+str(num_range)+ '.pkl'
	#将序列化对象保存到指定文件夹下
	file_name = os.path.join(dirname,file_name)
	#将对象进行序列化
	with open(file_name,'wb') as f:
		info_p = pickle.dump(info,f)
	with open(file_name,'rb') as f:
		info_d = pickle.load(f)
	return info_d

info = [1,2,3,4,5,6]
print(xulie('D:\A\B',info))


	