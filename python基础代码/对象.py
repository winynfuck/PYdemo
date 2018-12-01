'''
对象 = 属性+方法。对象是类的实例。
在python中类名是大写字母开头的。
面向对象的特征：
封装、继承、多态
继承是子类自动共享父类之间数据和方法的机制
多态是不同对象对同一方法的实现不一样。
'''
#继承
# class MyList(list):
	# pass
	
# list2 =MyList()
# list2.append(2)
# list2.append(4)
# print(list2)

#多态

# class Aa:
	# def fun(self):#python的self其实相当于C++的this指针。
		# print('我是小A....')
		
# class Ba:
	# def fun(self):
		# print('我是小B....')
# A =Aa()
# B =Ba()
# A.fun()
# B.fun()

#self怎么理解，就是在调用类的函数时，作为对象的标签。
# class Ball:
	# def setName(self,name):
		# self.name = name
		
	# def kick(self):
		# print("我叫%s ,该死是谁踢我的...." % self.name)v
		
# a = Ball()
# b = Ball()
# a.setName =('球A')
# b.setName =('球B')
# a.kick()
# b.kick()


#初始化构造参数
# class Ball:
	# def __init__(self,name):
		# self.name = name
	# def kick(self):
		# print("我叫%s ,该死是谁踢我的...." % self.name)
		
# ba = Ball('土豆')
# ba.kick()


#公有和私有
'''
为了实现对属性进行私有化，python采用name mangling技术
在python中定义私有变量只需要在变量名或者函数名前加上两个"__"，那么这个函数或变量就会为
私有的了。
那这样，要访问私有变量只能在内部进行，例如getName()
事实上，也可以通过_类名__私有变量来访问，python只是对私有变量进行了名字改编。
'''




'''
模拟一个场景，里面有一只乌龟和十条鱼
乌龟通过吃鱼来补充体力，当乌龟体力消耗殆尽或者鱼被吃光则游戏结束。
'''
class Tui:
	
	__tl = 80 #乌龟基础的体力
	
	def gettl(self):
		return self.__tl
	def update(self,change):
		self.__tl +=change
		
	def eatfish(self,eatfish_num):#吃鱼增加体力
		self.update(eatfish_num*16)
		
		
	def timegoing(self,day_num):#时间流逝消耗体力
		self.update(-day_num*10)

tui1 =Tui()

import random
num =0
day =0
while  1:
	#设置随机数模拟乌龟每天能否吃到鱼
	oppor =random.randint(1,10)
	if oppor > 5:
		tui1.eatfish(1)
		num =num +1
		
	tui1.timegoing(1)
	day =day + 1
	if tui1.gettl()  <= 0 or num ==10:
		print('乌龟死了!'+'\n'+'坚持了'+str(day)+'天,共吃了'+str(num)+'条鱼')
		break
		

	
'''
继承，class DerivedClassName(BaseClassName)括号里的是父类
子类可以继承父类的所有属性和方法。
注意：如果子类定义与父类同名的方法或属性，则会自动覆盖父类对应的
方法或属性

'''
class Parent:
	def hello(self):
		print('正在调用父类的方法.....')
		
class Child(Parent):
	def hello(self):
		print('正在调用子类的方法.....')
	

child =	Child()
child.hello()

class Fish:
	def __init__(self):
		self.x =random.randint(0,10)
		self.y =random.randint(0,10)
	def move(self):
		self.x -= 1
		print('我的位置是：',self.x,self.y)
class Goldfish(Fish):
	pass
	
class Carp(Fish):
	pass
	
class Salmon(Fish):
	pass

class Shark(Fish):
	def __init__(self):
		#Fish.__init__(self)#self是子类的实例对象
		super().__init__()
		self.hungry = True
		
	def eat(self):
		if self.hungry:
			print('我好饿，我刚吃完东西')
			self.hungry = False
		else:
			print('我不饿')
fish =Fish()
fish.move()
goldfish =Goldfish()
goldfish.move()

'''
子类对父类方法重写，因为会覆盖父类方法，所以取不出父类方法里的数据。
但有时候有需要这些数据，因此可用下面方法解决:

调用未绑定的父类方法或者使用super函数

多重继承，同时继承所有父类的属性和方法
class DerivedClassName(Base1,Base2)
'''
		
	
	
	
		
		
		

