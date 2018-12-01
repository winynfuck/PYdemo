'''
每一次迭代的的结果会作为下一次迭代的初始值。
提供迭代方法的容器我们称为迭代器。如序列、字典
关于迭代操作python提供了两个BIF
iter()对于一个容器对象调用iter()就得到一个对应的迭代器
next()next(迭代器)返回下一次迭代的值，如果下一个值没有，就会抛出异常StopIteration


迭代器的魔法方法有两个：
__iter__()返回本身
__next__()决定迭代的规则
'''

string = 'i love you '
it =iter(string)
for each in range(11):
	print(next(it))
	
	
#这里可以看出for语句的运行原理
string2 = 'i miss you '
it2 = iter(string2)
while True:
	try:
		each =next(it2)
		print(each)
	except StopIteration:
		break

		
#构建一个斐波那契迭代器
class Fibs:
	def __init__(self,n=10):
		self.a = 0
		self.b = 1
		self.n = n
	def __iter__(self):
		return self
	def __next__(self):
		self.a , self.b = self.b ,self.a +self.b
		if self.a > self.n:
			raise StopIteration
		return self.a
fibs =Fibs()
for each in fibs:
		print(each)

