#coding=UTF-8
#Author:Winyn
'''

一：定义一个学生类。有下面的类属性：

1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]

类方法：

1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int


'''
class Student():
	def __init__(self,name_str,age_int,*grades):
		'''
		对该类进行初始化
		1 姓名
		2 年龄
		3 成绩（语文，数学，英语)[每课成绩的类型为整数]
		
		'''
		
		self.name = name_str
		self.age = age_int
		self.grades = grades
	def get_name(self):
		'获取学生的姓名：get_name() 返回类型:str'
		return self.name
	def get_age(self):
		'获取学生的年龄：get_age() 返回类型:int'
		return self.age
	def get_course(self):
		'返回3门科目中最高的分数。get_course() 返回类型:int'
		return max(self.grades[0])
		
zm = Student('zhangming',20,[69,88,100])#这里的grade作为一个整体传入tuple的第一个元素中。
print(zm.get_name())
print(zm.get_age())
print(zm.get_course())
lq = Student('liqiang',23,[82,60,99])
print(lq.get_name())
print(lq.get_age())
print(lq.get_course())


'''
二：定义一个字典类：dictclass。完成下面的功能：


dict = dictclass({你需要操作的字典对象})

1 删除某个key

del_dict(key)


2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"

get_dict(key)

3 返回键组成的列表：返回类型;(list)

get_key()

4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)

update_dict({要合并的字典})



'''

class Dictclass():
	def __init__(self,dict):
		self.dict = dict
	def del_dict(self,key):
		'删除某个key'
		del self.dict[key]
	def get_dict(self,key):
		'判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"'
		if key in self.dict.get_key():
			return key
		else:
			return 'not found'
	def get_key(self):
		'返回键组成的列表：返回类型;(list)'
		return self.dict.keys()
	def update_dict(self,dict2):
		'合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)'
		return self.dict.update(dict2).values()
	
		
		