#coding=UTF-8
#Author:Winyn
'''
已知字符串：

info = 'test,&nbsp;url("http://www.baidu.com")&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com">ininnnin<img src="http://www.dd.com">'

要求完成下面2个小功能：
1.1 关闭[img]标签
1.2 将url()中的["]转为[']

最后结果字符串：

"test,&nbsp;url('http://www.baidu.com')&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com"></img>ininnnin<img src="http://www.dd.com"></img>"

'''
info = 'test,&nbsp;url("http://www.baidu.com")&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com">ininnnin<img src="http://www.dd.com">'
info = info +'</img>'


import re
text = re.findall(r'url(.*?)&',info)
text_new = []
for each in text:
	e = each.replace('"',"'")
	text_new.append(e)

l = len(text_new)
for i in range(0,l):
	info =info.replace(text[i],text_new[i])
print(info)
	
	
	

