'''
描述符就是将某种特殊类型的类的实例指派给另一个类的属性
何谓特殊类型：至少实现以下方法中的一个或者全部都实现
__get__(self,instance,owner)用于访问属性，它返回属性的值
__set__(self,instance,value)将在属性分配操作中调用，不返回任何内容
__delete__(self,instance)控制删除操作，不返回任何内容

'''
class MyDecriptor:
	def __get__(self,instance,owner):
		print('getting....',self,instance,owner)
	def __set__(self,instance,value):
		print('setting...',self,instance,value)
	def __delete__(self,instance):
		print('deleting...',self,instance)
class Test:
	x =	MyDecriptor()
	#MyDecriptor()是x的描述符，MyDecriptor是描述符类

	
class Celsius:
	def __init__(self,value = 26.0):
		self.value = float(value)
	
	def __get__(self,instance,owner):
		return self.value
		
	def __set__(self,instance,value):
		self.value = float(value)
		
class Fahrenheit:
	def __get__(self,instance,owner):
		return instance.cel *1.8+32
		
	def __set__(self,instance,value):
		instance.cel =(float(value)-32)/1.8
		
		
class Temperature:
	cel =Celsius()
	fah =Fahrenheit()
	
	
		