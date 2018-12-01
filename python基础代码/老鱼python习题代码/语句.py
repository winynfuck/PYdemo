
#print语句
'''
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
观察上面的print方法的参数，可以
设置sep，自定义多输出之间的连接符
设置end，自定义输出结束后带的符号
设置file，将输出写入到文件中去，并自带换行
'''
print(2)
print(4)
print(2,4)
print(1,2,3, sep = 'to',end = ' this is the end\n')


#以下这种方法可以通过设置
#!/usr/bin/env python3  
#coding:utf-8
K = 10
f = open("new.txt", 'w')  
for i in range(K):
    print("第{0}条数据".format(i), file=f)  



	
	
# is 检查共享，检查是否引用同一个对象。
a = [12,23,34]
b = a
print(a is b)

#布尔值的惰性求值机制
'''
string.swapcase()大写变小写，小写变大写
string.isdigit()判断字符串内是否是纯数字，返回布尔值。
'''
a = '45shfisf55sfsjw636ajkgfj'
print(''.join([x for x in a if x.isdigit() == True]))
a = a.lower()
print(dict([(x,a.count(x)) for x in set(a) if x.isdigit() == False ]))
#牢记set集合的天然去重效果。
#sort()方法里的key=另一个方法。等价于先将list里每一个元素执行另一个方法，之后再进行排序。
a_list = list(a)#字符串转换位列表
set_list = list(set(a_list))#列表转换为集合天然去重后，再转换为集合
set_list.sort(key = a_list.index)#对集合进行排序，排序规则为原来的规则
print(''.join(set_list))

#字符串反转的简单方式
print(a[::-1])
#判断字符串内是否有某子字符串
a = 'aFJJhaJIKSJbpoyh4565'
search = 'boy'
u = set(a)
u.update(list(search))
print(len(set(a)) == len(u))

a ='我不爱你是因为我爱生活'
u =set(a)
u.update(list('我爱你'))
if len(set(a)) == len(u):
	print('I love you ,too')
	
#通过位移快速的到字节数
size = 102324123499123
print('%.2f Kb'%(size >> 10))
print('%.2f Mb'%(size >> 20))

#字典的内置keys()和items()方法
#对字典进行排序


#好用的translate和maketrans
'''
translate(,)有两个参数，第一个参数是翻译表对象，第二个参数是要删除的字符
'''
a = '1234567'
t =str.maketrans('123','abc')#构建一个翻译表，这个翻译表是一一对应的，长度要一致
a = a.translate(t)
print(a)