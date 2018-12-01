#coding=UTF-8
#第一题-----------------------------------------------------------------------------------------
def get_num(num):
	'该方法返回的是带有数字和字符串的列表中去除字符串新构成的列表'
	try:
		str_count = 0
		for each_num in num:
			if type(each_num) != int:
				tag = num.index(each_num)
				raise TypeError
		return num
	except TypeError:
		
		num.remove(num[tag])#把字符串剔除
		str_count += 1#计数字符个数
		# print(str_count)
		# print(num)
		return get_num(num)#重新执行函数
	else:
		return 1



#第二题-----------------------------------------------------------------------------------------
def get_page(url):
	'该方法根据网址返回网页的源代码'
	import urllib.request
	try:
		f = urllib.request.urlopen(url)
		text =f.readlines()
	except urllib.error.HTTPError:
		return '访问页面出错!'
	except urllib.error.URLError:
		return '访问页面出错!'
	else:
		return text



#第三题----------------------------------------------------------------------------------------
def func(*num):
	'该方法返回列表中最大的元素'
	num = list(num)
	try:
		for i in num:
			if type(i) != int:
				raise TypeError	
	except TypeError:
		print('列表中有非整型元素，无法比较大小')
	else:
		num.sort()
		return num[-1]




#第四题----------------------------------------------------------------------------------------
def get_dir(f):
	'该方法返回路径下所有文件夹组成的列表'
	import os.path
	import os
	try:
		if os.path.isdir(f) != True:
			raise FileNotFoundError
	except FileNotFoundError:
		return '该目录不存在！'
	else:
		return os.listdir(f)
		

if __name__ == '__main__':
	assert get_num([2,4,6,'str',8,'str'])==[2,4,6,8]
	print(get_page('http://baidu.com/'))
	assert type(func(2,3,5,6,7,23)) == int
	print(get_dir(r'D:\ruanjian'))