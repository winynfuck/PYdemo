'''
python的循环语句有两种，一种是
while 条件:
	语句
只要条件为真就执行循环体里面的语句

另一种是:for 循环
for 目标 in 表达式：
	语句
其中表达式通常是一个列表[],也就是依次取出列表中的数据作为目标进行运算，直到全部取完为止。

range(start,stop,step)
在Python3.x 中 range() 函数返回的结果是一个整数序列的对象，而不是列表。所以要生成列表，
要写成list(range(start,stop,step))

表达式还可以是一个字符串str,也就是依次取出字符串中的每一位字符参与运算，直到取完为止。


'''

#coding:utf-8
#表达式是列表
for i in list(range(10)):
	if i % 2 == 0:
		print(i)
		continue
	i+=2
	print(i)
	
for i in list(range(1,10,2)):
	print(i,end ='')
print('\n')	
member = ['小甲鱼','小布丁','黑夜','迷途','一经']
for each in member:
	print(each ,len(each))
	
#表达式是字符串
favourite = 'fishc'
for i in favourite:
	print(i,end =' ')

	
