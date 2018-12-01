'''
列表就像一个仓库，可以存放字符串，整型，浮点型，对象，甚至一个小列表

定义一个列表也很简单，name = [元素1 , 元素2 , ....... , 元素n],

有时候我们事先不知道列表内元素的具体值，但是我们又确定列表在后续会使用，可以定义
一个空列表:name = []
'''

'''
对列表进行插入元素的内置方法有：append(),extend(),insert()
其中:
append('待插入的元素'),作用是在列表的最后插入新元素
extend([待插入的列表]),作用是在列表的最后按照顺序添加待插入列表的每一个元素
insert(列表序号，待插入的袁术),作用是在列表的某一个位置插入新值
注:列表序号从0开始

'''
member =['小甲鱼','小飞鱼']
member.append('大王八')
member.extend([1,2,3,4])
member.insert(3,'9')
print(member)
print(len(member))

'''
对列表进行删除元素的内置方法有:remove(),del ,pop()
其中:
remove(列表中已存在元素的值),前提是这个元素必须存在列表中
del list[待删除元素的序号],若del list[]，则表示删除列表
pop(待删除元素的序号),若 pop(),则表示删除列表最后一位。pop()这个方法是有返回值的，
执行的先返回再删除的操作

'''

member1 =['小甲鱼','小飞鱼','牡丹','玉林','黑夜']
member1.remove('小飞鱼')
print(member1)
del member1[0]
print(member1)
name = member1.pop()
print(name)
print(member1)
member1.pop(1)
print(member1)



'''
列表分片操作
列表的深拷贝问题，我们知道list1 = list2[:]能拷贝一个列表，
而list3 = list1 也能赋值一个列表。
但是对list1作改变，list3会做同样改变,而list2不会作改变.
'''

print(member1[1:3])
print(member1[:3])
print(member1[1:])
print(member1[:])


'''
列表的比较运算符，算术运算符，关系运算符
比较运算符可用于两列表之间的大小比较，有> , < , =,若两列表中元素的个数大于1
，则比较结果与两列表第一个元素的比较结果一致

逻辑运算与其他情况一样

判断元素是否再列表中，用in ,not in 

'''
list1 = [123,234]
list2 = [234,345]
#列表之间进行大小比较
print(list1 > list2)
print(list2 < list1)
#列表之间进行逻辑运算
list3 = [123,234]
print((list1 < list2) and (list1 == list3))
print((list1 > list2) and (list1 == list3))
#判断元素是否在列表里
print(123 in list1)
print('小鲫鱼' not in list1)

'''
列表的几种重要的方法count,index,reverse,sort
list.count(a),作用是求出元素a在列表list中出现的次数
list.reverse(),作用是将列表list颠倒过来
list.index(a,num1,num2),作用是求出元素a在列表list的序号num1和num2间第一次出现的序号数
如果index的参数仅有一个a,则默认是num1 = 0 , num2 = len(list)-1
'''
list3*=15
print(list3)
#元素a在列表list中出现的次数
print(list3.count(123))
#reverse方法用户将列表颠倒过来
print(list2.reverse())
#index 方法用于得出列表中某个元素第一次出现的序号数，3，8表示从3到8的一小段列表中第一次出现该元素的序号
print(list3.index(123))
print(list3.index(123,3,8))
#sort方法能将列表进行排序，默认是从小到大排序，默认值True,如果改成False,则是从大到小排序
list4 = [1,2,4,22,12,45,21]
print(list4.sort())
print(list4.sort(reverse = True))

