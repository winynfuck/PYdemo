#coding=UTF-8
#--------------------------------------------------------------------------------------------#

def func1(name_str):
	'该方法用于将name_str的首字母变成大写'
	first = name_str[0].upper()
	last = name_str[1:]
	#这里不使用+进行拼接是因为效率低，会生成新的字符串占内存。
	return '%s%s'%(first,last)

assert func1("lilei") == "Lilei"
assert func1("hanmeimei") == "Hanmeimei"
assert func1("Hanmeimei") == "Hanmeimei"

#--------------------------------------------------------------------------------------------#

def func2(name_str,callback = None):
	'''
	该方法用于将字符串以不同的callback方式处理后返回.
	callback = None，则将字符串首字母变大写后返回
	callback = 'string.lower'，则将字符串全部变成小写后返回
	callback = 'string.upper'，则将字符串全部变成大写后返回
	
	'''
	
	if callback ==None:
		return func1(name_str)
	elif callback == 'string.lower':
		return name_str.lower()
	else:
		return name_str.upper()

assert func2("lilei") == "Lilei"
assert func2("LILEI",callback='string.lower') == "lilei"
assert func2("lilei",callback='string.upper') == "LILEI"

#--------------------------------------------------------------------------------------------#

def func3(*kargs):
	'该方法用于将字符串进行处理'
	result = ''
	for each in kargs:
		result +=str(each)
	return ' '.join(result)
assert func3(1,2,3,4,5)=='1 2 3 4 5'
assert func3(5,3,4,5,6)=='5 3 4 5 6'

#--------------------------------------------------------------------------------------------#

def func4(*kargs):
	'该方法返回输入的任意数据之中第一个字符串'
	tag = 0
	for each in kargs:
		tag +=1
		if type(each)==str:
			return each
			break
	if tag ==len(kargs):
		return None
	


assert func4(222,1111,'xixi','hahahah')=='xixi'
assert func4(7,'name','dasere') == 'name'
assert func4(1,2,3,4) == None

#--------------------------------------------------------------------------------------------#

def func5(name = None,**kargs):
	'该方法用于按一定的格式返回数据'
	result =[]
	if name != '':
		result.append(name)
	k = list(kargs.keys())
	v = list(kargs.values())
	_kv =[]
	for i in range(len(k)):
		_kv.append(k[i]+':'+str(v[i]))
	for i in range(len(k)):
		result.append(_kv[i])
	return ','.join(result)
	
assert func5('lilei') == "lilei"
assert func5("lilei",years=4) == "lilei,years:4"
assert func5("lilei",years=10,body_weight=20)== "lilei,years:10,body_weight:20"
		