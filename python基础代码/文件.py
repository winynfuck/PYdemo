'''
我们在使用python进行编程，不是所有的数据都是保存在内存里的，
更多的情况是保存在磁盘内的文件里的。因此，要想调用数据进行
计算，就必须掌握在python中如何对文件里的数据进行读写。
'''
#创建一个文件
''' 如果文件名指定了位置'''
f = open('D:\\new_file.txt','r')
str1 = ''
file = f.read()
for each_line in file:
	     str1 +=each_line
print(str1)

