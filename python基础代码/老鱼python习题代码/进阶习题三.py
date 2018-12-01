#coding=UTF-8
def func1():
	'人生不必太圆满，求而不得未必是遗憾'
	return 'be easy'
def func2():
	return 'be easy'
'''
函数文档如果为空，function.__doc__的值为：None
'''
def get_fundoc(func):
	'该方法返回的是任意一个函数对象的描述文档'
	#判断一个变量是否是函数，可以通过isfunction方法来判断
	from inspect import isfunction
	if(isfunction(func)):
		if func.__doc__ != None:
			return func.__doc__
		else:
			return 'not found'
	else:
		return 'Error:该对象不是函数'
		
def get_cjsum():
	'该方法用于求1-100范围内所有整数的平方和，返回结果为整型'
	cjsum = 0
	for i in range(1,101):
		cjsum += i*i
	return cjsum

def list_info(list):
	'该方法用于探讨怎么保证在列表list中进行某些操作而不改变原来列表的值'
	import copy
	deepcopy_list = copy.deepcopy(list)#这里考察的深拷贝和浅拷贝的区别
	deepcopy_list[-1] = 5
	return deepcopy_list
	
def get_funcname(func):
	'该方法用于判断函数是否可以调用'
	from inspect import isfunction
	if isfunction(func) and callable(func):
		return func.__name__#获取函数对象的名字，function_name.__name__
	else:
		return 'func is not function'

	
	
	
		

	

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
if __name__ == '__main__':
	func =1
	a = [1 , 2 , 3]
	assert list_info(a) == [1,2,5]
	assert a == [1,2,3]
	assert get_fundoc(func1)== '人生不必太圆满，求而不得未必是遗憾'
	assert get_fundoc(func2)== 'not found'
	assert get_fundoc(func) =='Error:该对象不是函数'
	assert isinstance(get_cjsum(),int)
	assert get_funcname(func1) =='func1'