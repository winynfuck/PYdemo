'''
定制序列，首先要讲一下协议
协议与其他编程语言中的接口很相似，它规定你哪些方法必须要定义
然而，在python中的协议就显得不那么正式。事实上，在python中，
协议更像是一种指南。

容器类型的协议
如果你希望定制的容器是不可变的话，你只需要定义
__len__()和__getitem__()方法。

如果你希望定制的容器是可变的话，除了定义
__len__()和__getitem__()方法，你还需要定义
__setitem__()和__delitem__()两个方法。


练习：
编写一个不可改变的自定义列表，要求记录列表中每个元素被访问的次数
'''
class zdyseq:
	def __init__(self,*args):
		self.values = [ x for x in args]
		self.count = {}.fromkeys(range(len(self.values)),0)
	def __len__():
		return len(self.values)
	
	def __getitem__(self,key):
		self.count[key]+= 1
		return self.values[key]

c1 =zdyseq(1,2,35,4)
c2 =zdyseq(354,42,1,2)
print(c1[1])
print(c2[1])
print(c1[1]+c2[1])
print(c1.count)