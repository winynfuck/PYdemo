#组合
'''
现在要求定义一个类，叫水池，水池里要有乌龟和鱼
所谓组合是指把类的实例化放到一个新类里面去，就避免了继承。
'''
class Turtle:
	def __init__(self,x):
		self.num =x

class Fish:
	def __init__(self,x):
		self.num =x
		
class Pool:
	def __init__(self,x,y):
		self.turtle = Turtle(x)
		self.fish = Fish(y)
	def print_num(self):
		print('水池里有乌龟%d 只，小鱼%d 条！'% (self.turtle.num , self.fish.num))
pools =Pool(1,10)
pools.print_num()


#mix in 编程机制
'''
如果属性名字和方法名相同，属性会覆盖方法 
为了避免这种情况，我们需要对命名有一些技巧：
不要试图在一个类里边定义出所有能想到的特性和方法，应该利用继承和组合机制来进行扩展
用不同词性6命名，如属性名用名词，方法名用动词。

'''
class C:
	def x(self):
		print('x_man')
c = C()
c.x()
c.x =1
print(c.x)
#c.x()

'''
绑定的概念：
python严格要求方法需要有实例才能被调用，这种限制其实就是所谓的绑定。
这种机制归功于self
'''
class CC:
	def setXY(self,x,y):
		self.x = x
		self.y = y
	def printXY(self):
		print(self.x,self.y)
dd = CC()
print(dd.__dict__)
print(CC.__dict__)
dd.setXY(5,4)
print(dd.__dict__)
del CC
ee =CC()
dd.printXY()


'''
一些常用的BIF

关于类的检查
issubclass(class,classinfo)如果class是classinfo的子类，则返回True
不严格检查：
1、一个类被认为是其自身的子类
2、classinfo可以是类对象组成的元组，只要class与其中任何一个候选类的子类，
则返回True。


isinstance(object,classinfo),检查一个实例对象是否属于一个类的。

关于属性的检查
hasattr(object,name)，测试对象是否有指定的属性，其中检查的属性要用字符串''括起来。
getattr(object,name,[default])，获取对象的指定属性的值，如果属性不存在，可以打印default值。
setattr(object,name,values)，设置对象属性的值，如果属性不存在，则会新建一个属性并赋值。
delattr(object,name)删除对象的属性，属性不存在则抛出异常。

property(fget =none,fset =none ,fdel =none,doc =none)通过属性来设置属性

'''
class C:
	def __init__(self,size =10):
		self.size = size
	def getSize(self)
		return self.size
	def setSize(self,value):
		self.size = value
	def delSize(self):
		del self.size
	x =property(getSize,setSize,delSize)
	
c1 = C()
print(c1.getSize())
print(c1.x)
c1.x =18
print(c1.x)
del c1.x


