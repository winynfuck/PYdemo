#coding=UTF-8
#Author:Winyn
'''
作业：

1 已知字符串:
info = '<a href="http://www.baidu.com">baidu</a>'

用正则模块提取出网址："http://www.baidu.com"和链接文本:"baidu"

2 字符串："one1two2three3four4" 用正则处理，输出 "1234"

3 已知字符串：text = "JGood is a handsome boy, he is cool, clever, and so on..." 
查找所有包含'oo'的单词。

4 为什么在unix里，grep后面的正则有些时候要加引号，有些时候不需要。

'''
#------------------------------------------------------------------------------------------
info = '<a href="http://www.baidu.com">baidu</a>'
import re
compile1 = 'http://\w{3}\.\w+\.\w+'
compile2 = '>\w+</a>'
sub_str1 = re.findall(compile1,info)
sub_str2 = re.findall(compile2,info)
print('网址：%s'%sub_str1)
print('链接文本：%s'%sub_str2[0][1:-4])


#------------------------------------------------------------------------------------------
str1 = "one1two2three3four4"
# compile3 = '\w+(\d)\w+(\d)\w+(\d)\w+(\d)'
# d =re.match(compile3,str1)
# print(''.join(d.groups()))
a = re.split(r'[a-z]+',str1)
a.remove('')
print(''.join(a))

#------------------------------------------------------------------------------------------
text = "JGood is a handsome boy, he is cool, clever, and so on..." 
oo = re.findall(r'\w+oo\w+',text)
print(oo)	


