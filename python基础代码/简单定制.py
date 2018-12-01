#类的定制
'''
简单定制:
基本要求：
	定制一个计时器的类
	start和stop方法代表启动计时和停止计时
	假设计时器对象t1，print(t1)和直接调用t1均显示结果
	当计时器未启动或已经停止计时，调用stop方法会给予温馨的提示
	两个计时器对象可以进行相加：t1+t2
	只能使用提供的有限资源实现

'''
#__str__魔法方法运用于需要字符输
class A:
	def __str__(self):
		return '我最棒'
a = A()
print(a)
class B:
	def __repr__(self):
		return '我是最胖的！'
b = B()
b
print(b)

import time as t
class MyTimer:
	def __init__(self):
		self.unit = ['年','月','天','小时','分','秒']
		self.prompt = '未开始计时'
		self.lasted =[]
		self.begin = 0
		self.end = 0
	def __add__(self,other):
		prompt ='总共运行了'
		result =[]
		for index in range(6):
			result.append(self.lasted[index]+other.lasted[index])
			if result[index]:
				prompt += (str(result[index])+self.unit[index])
		return prompt
		
		
	def __str__(self):
		return self.prompt
	__repr__ = __str__  
	def start(self):
		self.begin = t.localtime()
		print('计时开始....')
	def stop(self):
		self._calc()
		self.end = t.localtime()
		print('停止计时')
	#内部方法，计算运行时间
	def _clac(self):
		self.lasted =[]
		self.prompt = '总共运行了'
		for index in range(6):
			self.lasted.append(self.end[index]-self.begin[index])
			if self.lasted[index]:
				self.prompt +=str(self.lasted[index])+self.unit[index]
		
		  




	