#创建和访问字典 
'''
字典是一种映射类型的数据，不是序列，它是通过键-值存储的
''' 
#定义一个字典
#通过大括号里面的键值对构成字典
dict1 ={ 1:'one' , 2:'two' , 3:'three', 4:'four'}
print(dict1)
#访问字典中具有某键的值，用dict[键]
print(dict1[1])
#创建一个空的字典
dict2 ={}
#也可以通过工厂函数-dict()函数创建字典
#此前学习的list(),str(),int(),tuple()都是工厂函数
dict3 = dict((('F',70),('i',105),('s',115),('h',104),('C',67)))
print(dict3)
#还可以通过关键字的形式来创建字典
dict4 = dict(小甲鱼 = '让编程改变世界',苍井空 = '让AV征服所有宅男')
print(dict4)
#通过对字典里已有键值对的键重新赋值，来改变字典
dict4['苍井空'] = '所有AV从业者都要通过学习编程来提高职业技能'
print(dict4)
#若没有这个键值对，则创建这个新键值对
dict4['爱迪生'] = '天才是百分之一的灵感加上百分之九十九的汗水'
print(dict4)


'''
字典的内置函数
1、fromkeys(键的元组，值)，实质上用于创建字典
作用是创建一个字典，此字典的键的元组中每一个键对应的值都设置为固定值，
如果只有一个参数，则设置为None

2、keys(),values()返回一个列表，这个列表分别存储字典里的所有的键或所有的值。items()
则是返回字典里的所有键值对,即返回所有的项

3、get(键)方法，访问字典中某个键对应的值，如果访问的键不存在，则返回None
如果希望找不到值的时候，返回一个具体的值可以设置get(不存在的键，返回的值)

4、通过成员资格in ,not in 来判断一个数据是否在字典中。与序列不同，这里查找的是元素
的键，而不是元素的值

5、清空一个字典，dict.clear()

6、dict.copy()浅拷贝函数，浅拷贝与赋值不一样，浅拷贝的地址与被拷贝的对象不一样，
而赋值的地址与被赋值的对象一样

7.dict.pop(键),给定键弹出对应的值；dict.popitem(),给定键弹出随机的项

8、dict.setdefault(键，值)，给字典添加项，如果没有给出值，则为None

9、dict.update(),用一个字典的映射关系去更新另外一个字典
'''
dict6 ={}
dict6.fromkeys(('小甲鱼','小鲶鱼','大鲨鱼'),'属于鱼类')
print(dict6)

dict6 =dict6.fromkeys(range(32),'赞')
print(dict6)
for eachkey in dict6.keys():
	print(eachkey)
for eachvalue in dict6.values():
	print(eachvalue)
print(dict6.items())
for eachItem in dict6.items():
	print(eachItem)
print(dict6.get(32))
print(dict6.get(32,'木有'))

print(32 in dict6)

dict7 = dict6.copy()
print(dict7)

print(dict7.pop(2))
print(dict7.popitem())

a ={}
a.setdefault('小白')
b = {'小白':'狗'}
a.update(b)
print(a)


#如何创建集合
'''
集合是字典的表亲，集合和字典都是无序的，你不能通过索引得到字典或集合中某
一个元素的值。集合是唯一的，即表示集合中没有重复的数据
创建集合的方法:1,用花括号包含一堆数据 2,用set()的内置方法
set(列表，元组，或字符串)


读取集合内的元素:
1.用for把集合中的数据一个个读取出来
2.通过成员关系符in 和not in判断元素是否在集合中

在集合中添加数据和删除数据，
添加,使用add()
删除,使用remove()

定义一个不可变的集合
用frozenset()

'''
set1 = set([1,2,35,4,56,35])
print(set1)
for each in set1:
	print(each)
print(2 in set1)

set1.add('新添加的数据')
set1.remove(35)
print('经过添加和删除操作后的set1.....',set1)

print('定义一个不可变的集合')
set2 =frozenset([1,2,35,456, 56])
print(set2)

	
