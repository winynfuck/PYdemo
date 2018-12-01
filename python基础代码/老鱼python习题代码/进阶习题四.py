#coding=UTF-8
g =filter(lambda x:x % 2 ==0,list(range(1,101)))
print(list(g))

'''
用位置匹配参数，关键字匹配参数，收集匹配参数分别写四个函数
'''
def func1(arg1,arg2,arg3):
	result = [arg1,arg2,arg3]
	return result
	
def func2(arg1 = 'a',arg2 = 'b',arg3 = 'c'):
	return [arg1,arg2,arg3]
def func3(*kargs):
	'该方法返回输入的任意个列表中所有元素的最大值'
	kargs=list(kargs)
	for i in range(1,len(kargs)):
		kargs[0].extend(kargs[i])	
	return max(kargs[0])
def func4(**kwargs):
	return kwargs
	


def func5(i):
	if i<100:
		return i + func5(i+1)
	return i
print (func5(0))
















if __name__ == '__main__':
	assert func1(1,2,3) == [1,2,3]
	assert func2(arg2 =1,arg1 =2,arg3 =3) == [2,1,3]
	assert func4(apple ='fruit',cabbage ='vegetable')=={'apple':'fruit','cabbage':'vegetable'}
	assert func3([1,2,3],[1,5,65],[33,445,22])== 445
	'''
	要注意keywords不能为表达式，如：
	这里前面函数参数那块不能加引号，而输出的字典结果会自动加上引号。
	'''
	