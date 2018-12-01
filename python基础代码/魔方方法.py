#魔法方法
'''
魔法方法总是被双下划线包围，例如__init__()
魔法方法是面向对象的Python的一切，如果你不知道魔法方法，说明你还没能
意识到面向对象的Python的强大。
魔法方法的魔力是他们总会在适当的时候被调用。
'''

'''
1.__init__(self,[,,,])构造方法，类在实例化对象时会调用的方法。用来
初始化对象。
注意__init__方法的返回值一定是None

2.但是__init__方法并不是实例化对象时被调用的第一个方法，
而是__new__(cls[,,])，此方法需要一个实例对象作为返回值。
当继承不可变类型，又必须要修改的时候，需要用__new__方法。


3.__del__(self)析构方法。python的垃圾回收机制，只有当一个位置没有被贴上任何标签
的时候才会被调用，而不是有del 语句就执行析构方法。

'''
#构造方法
class A: 
	def __init__(self):
		return 'A for A-cup'
#a = A()

class CapStr(str):#因为str是不可修改的，因此需要在实例化之前第一步就对其修改
	def __new__(cls,string):
		string =string.upper()#将字符串变成大写
		return str.__new__(cls, string)#再将变成大写后的字符串传入str的__new__方法中
			
b =CapStr(' I 	love you')
print(b)

#析构方法
class C:
	def __init__(self):
		print('我是__init__方法，我被调用了...')
	def __del__(self):
		print('我是__del__方法,我被调用了.....')
c1 =C()
c2 =c1
c3 =c2
del c3
del c2
del c1


'''
python中用工厂函数代替其他函数中的数据类型，所谓的工厂函数如list,int,float,都是类对象。
算术运算。
python的魔法方法还可以自定义数值处理。
__add__(self,other)定义加法行为
__sub__(self,other)定义减法行为
__mul__(self,other)定义乘法行为
__truediv(self,other)定义真除法行为
__floordiv(self,other)定义整数除法的行为
__mod__(self,other)定义取模算法的行为
__divmod__(self,other)定义取余的行为
__pow__(self,other,[modulo])定义幂运算的行为
__lshift__(self,other)定义按左移位的行为
__rshift__(self,other)定义按右移位的行为
__and__(self,other)定义按位与操作的行为
__xor__(self,other)定义按位异或操作的行为
__or__(self,other)定义按位或操作的行为

'''
print(type(int))
print(type(list))
class C:
	pass
c =C()
print(type(c))

a =int('123')#将字符串通过int类实例化。
b =int('456')
print(a+b)

#自定义数值运算
class new_int(int):
	def __add__(self,other):
		return int.__add__(self,other)
	def __sub__(self,other):
		return int.__add__(self,other)
a =new_int(3)
b =new_int(5)
print(a+b)
print(a-b)