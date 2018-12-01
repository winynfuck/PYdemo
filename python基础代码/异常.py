# import os
# print(os.getcwd())
# filename =  input('请输入文件名:')
# f =open(filename,'r')
# for eachline in f:
	# print(eachline)
# f.close()
	

'''

检测异常的方法：
try:
	检测范围	
except 	Exception[as reason]:
	出现异常(Exception)后的处理代码
finally:
	无论如何都会被执行的代码
	
try语句捕获到异常之后就不会再执行之后的语句
'''
	
try:
	
	f =open('我为什么是一个文件.txt')
	print(f.read())
	f.close()
	sum = 1 + '1'
#except OSError as reason1:
	print('文件出错！'+'错误的原因是:'+str(reason1))
#except TypeError as reason2:
	print('类型出错！'+'错误的原因是:'+str(reason2))
#except:
	print('类型错误！')
except (OSError,TypeError):
	print('出现异常!')try:
	
	f =open('我为什么是一个文件.txt')
	print(f.read())
	f.close()
	sum = 1 + '1'
#except OSError as reason1:
	print('文件出错！'+'错误的原因是:'+str(reason1))
#except TypeError as reason2:
	print('类型出错！'+'错误的原因是:'+str(reason2))
#except:
	print('类型错误！')
except (OSError,TypeError):
	print('出现异常!')
	
'''
raise 语句，代码自己引发异常
'''

	