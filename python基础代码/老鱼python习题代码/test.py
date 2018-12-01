#coding=UTF-8
# def func1(arg1,arg2):
	# return arg1 + arg2
	
# print(dir(func1.__code__))
# print(func1.__code__.co_varnames)
# print(func1.__code__.co_filename)
# print(help(func1.__code__))



# def func2(arg):
	# arg[0] = 5
	# return arg
	
# print(func2.__name__)
# d =lambda x:x + 1 if x > 0 elsez 'error'  #三元表达式中的else后面没有引号
# print(d(4))
from urllib.parse import urlparse
url ='http://www.xx.com'
res = urlparse(url)
print(res)