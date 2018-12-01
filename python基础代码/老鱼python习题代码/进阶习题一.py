#coding=UTF-8
#第一题----------------------------------------------------------------------------------
def func_cmp(*num):
	'该方法返回任意多的整型参数中的最大值最小值'
	try:
		for i in num:
			if type(i) != int:#这里不用加引号，加引号就成字符串了。
				raise TypeError
	except	TypeError:
		print('Error：输入类型错误！')
	else:
		list(num).sort()#sort()原地进行排序，返回值为none，因此不能进行赋值
		result ='最大值是：'+ str(num[-1])+','+'最小值是：'+str(num[0])
		return result

	
#第二题----------------------------------------------------------------------------------
def func_str_longest(*strs):
	'该方法返回任意多的字符串参数中字符最长的字符串'
	try:
		for each in strs:
			if type(each) != str:
				raise TypeError
	except TypeError:
		print('Error：输入类型错误！')
	else:
		str_len_max = 0
		for each_str in strs:
			if len(each_str) >= str_len_max:
				str_longest = each_str
				str_len_max =len(each_str)
	return str_longest
	

			
#第三题----------------------------------------------------------------------------------
#TODO:这一题缺少判断输入对象是否是一个存在的模块的异常检测过程。
def get_doc(module):
	return help(module)


#第四题----------------------------------------------------------------------------------
import os.path
def get_text(f):
	try:
		if os.path.exists(f) == False:
			raise FileNotFoundError
	except FileNotFoundError:
		return 'Error:文件不存在！'
		
	else:
		with open(f,'r') as file:
			text = file.read()
		return text
	


#第五题----------------------------------------------------------------------------------
import os
def get_dir(folder):
	try:
		if os.path.exists(folder) == False:
			raise FileNotFoundError
	except FileNotFoundError:
		return 'Error:文件不存在!'
		
	else:
		folder_file = folder 
		return os.listdir(folder_file)



if __name__ == '__main__':
	assert func_cmp(1,2,3,4) =='最大值是：4,最小值是：1'
	assert func_str_longest('shighs','shifgsissisif','123') == 'shifgsissisif'
	assert get_text(r'D:/A/new.txt') =='a\nb\nc'
	assert get_text(r'D:/A/ne1.txt') =='Error:文件不存在！'
	print(get_doc('urllib'))
	assert get_dir('D:\A') == ['B', 'new.txt', 'old.txt']
