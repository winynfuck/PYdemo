#coding:UTF-8
#Author:Winyn
'''
定义一个列表的操作类：Listinfo

包括的方法: 

1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key() 

list_info = Listinfo([44,222,111,333,454,'sss','333'])

'''
class Listinfo():
	def __init__(self,list1):
		self.list = list1
	def __str__(self):
		return '%r' % self.list
	def add_key(self,keyname):
		'列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]'
		if isinstance(keyname,str) or isinstance(keyname,int):
			self.list.append(keyname)
			return self.list
		else:
			print('Error:添加的数据类型错误')
	def get_key(self,num):
		'列表元素取值：get_key(num) [num:整数类型]'
		if num >=0 and num <=len(self.list)-1:
			return self.list[num]
		else:
			return 'Error:列表的下标越界！'
	def update_list(self,*list1):
		'列表合并：update_list(list)	  [list:列表类型]'
		if isinstance(list1,tuple):
			
			return self.list.extend(list(list1))
		else:
			return 'Error:输入数据类型错误！'
	def del_key(self):
		'删除并且返回最后一个元素：del_key() '
		return self.list.pop()

	
	
'''
定义一个集合的操作类：Setinfo
包括的方法: 

1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]

set_info =  Setinfo(你要操作的集合)


'''
class Setinfo():
	def __init__(self,*set1):
		self.set = set(set1)
	def __str__(self):
		return '%s' % (self.set,)
	def add_setinfo(self,keyname):
		'集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]'
		self.set.add(keyname)
		return self.set
	def get_intersection(self,*unioninfo):
		'集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]'
		
		return self.set & set(unioninfo)
	def get_union(self,*unioninfo):
		'集合的并集： get_union(unioninfo)[unioninfo :集合类型]'
		
		return self.set | set(unioninfo)
	def del_difference(self,*unioninfo):
		'集合的差集：del_difference(unioninfo) [unioninfo :集合类型]'
		return self.set - set(unioninfo)
		
if __name__ =='__main__':
	
	list_info = Listinfo([44,222,111,333,454,'sss','333'])	
	list_info.add_key('234')
	print(list_info.get_key(2))
	list_info.update_list(1,2,3,4)
	list_info.del_key()
	print(list_info)			
	set_info = Setinfo(1,2,3,4,5)
	print(set_info)
	print(set_info.get_intersection(2,4,6,7))
	print(set_info.get_union(6,'3',9))
	print(set_info.del_difference(3,4,'3'))
		
		
		
		