#属性访问魔法方法
'''
__getattr__(self,name)定义当用户试图获取一个不存在的属性时的行为
__getattribute__(self,name)定义当该类的属性被访问时的行为
__setattr__(self,name,value)定义当一个属性被设置时的行为
__delattr__(self,name)定义一个属性被删除时的行为



'''
#注意死循环的陷阱
class Rectangle:
	def __init__(self,width = 0,height = 0):
		self.width = width
		self.height = height
	def __setattr__(self,name,value):
		if name =='square':
			self.width = value
			self.height = value
		else:
			#self.name =value
			super().__setattr__(name,value)
			#对象有一个特殊的属性dict，用于以字典的形式输出所有属性和对应的值
			#或者self.__dict__[name] = value
	def getArea(self):
		return self.width * self.height
	
