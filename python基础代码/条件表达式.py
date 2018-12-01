
'''
python的条件表达式：
if 条件:
	条件为真执行
else:
	条件为假执行
多层嵌套条件表达可以用:
if 条件一:
	条件一为真执行
elif 条件二:
	条件二为真执行
elif 条件三:
	条件三为真执行
else:
	以上所有条件都不为真时候执行



'''
#coding:utf-8
score = int(input('请输入你的分数:'))

if 100 >= score >= 90:
	print('A')
elif 90 >= score >= 80:
	print('B')
elif 80 >= score >= 60:
	print('C')
elif 60 >= score >= 0:
	print('D')
else:
	print('输入错误！')