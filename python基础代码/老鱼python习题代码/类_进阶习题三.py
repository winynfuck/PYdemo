#coding=UTF-8
#Author:Winyn
'''
1.定义一个fun(url,folder_path)
获取url地址的内容，保存到folder_path的文件目录下，并随即生成一个文件名。
2.定义一个func(folder_path),合并该目录下的所有文件，生成一个all.txt。
3.定义一个func(url),分析该url内容里有多少个链接
4.定义一个func(url),获取他？后的参数，并返回成一个dict
assert('http://url/api?param=2&param2=4') == {'param':'2','param2':'4'}
5.定义一个func(folder),删除该folder下所有文件


'''
import urllib.request,random,os,os.path,string
#func1-------------------------------------------------------------------------------------#

def func(url,folder_path):
	'该方法获取url地址的内容，保存到folder_path的文件目录下，并随即生成一个文件名。'
	try:
		f = urllib.request.urlopen(url)
		text =str(f.readlines())
	except urllib.error.HTTPError:
		return '访问页面出错!'
	except urllib.error.URLError:
		return '访问页面出错!'
	else:
		#对url进行修改
		tranlab =url.maketrans('/','_')
		url =url.translate(tranlab)
		
		#判断文件夹里是否已经存在文件
		#获取文件名列表
		file_name_list = os.listdir(folder_path)
		#判断是否存在url文件
		for each in file_name_list:
			if url[7:] in each:
				return '文件已存在，不用再保存一次!'
				
		#自动生成一个文件名。	
		file_name = folder_path +'\\' + url[7:] + str(random.randint(1,100))+ '.txt'
		#判断文件名是否存在
		if os.path.exists(file_name)==True:
			file_name = folder_path +'\\'+url[7:]+str(random.randint(1,100)+1)+ '.txt'
		
		with open(file_name,'w') as f:
			f.write(text)
			return '保存成功'
			
			
#func2-------------------------------------------------------------------------------------#			
def func2(folder_path):
	'该方法合并该目录folder_path下的所有文件，生成一个all.txt.'
	#判断目录是否存在
	if not os.path.exists(folder_path):
		return '目录不存在！'	
	#生成一个all.txt文件
	if 'all.txt' not in os.listdir(folder_path):
		f=open(folder_path+'\\'+'all.txt','w')
	#获取目录folder_path下的所有文件
	file_list = filter(lambda x: r'.txt' in x and x != 'all.txt',os.listdir(folder_path))
	fo=list(file_list)
	#将所有文件的内容读取并写入到all.txt中。
	try:
		for each_file_name in fo:
			with open(folder_path+'\\'+each_file_name,'r') as each_file:
				text =each_file.readlines()
			with open(folder_path+'\\'+'all.txt','a') as f:
				f.write(str(text)+'--------------------------------------------------\n\n\n\n\n')
			
		return '合并成功'
	except	Error as whaterror:
		return '发生错误！'+whaterror
		
		
		
#func3-------------------------------------------------------------------------------------#					
def func3(url):
	'定义一个func(url),分析该url内容里有多少个链接'
	pass
	
#func4-------------------------------------------------------------------------------------#					
def func4(url):
	'该方法获取url后的参数，并返回成一个dict'
	#获取url中？的索引值
	locality =url.index('?')
	#截取？后面的部分，并切分成列表
	url_next = url[locality+1:].split('&')
	#param=2,param2=4
	
	#生成字典
	k =[]
	v=[]
	for each in url_next:
		find_key = each.index('=')
		k.append(each[:find_key])
		v.append(each[find_key+1:])
	return dict(zip(k,v))
		
	
#func5-------------------------------------------------------------------------------------#		
def func5(folder):
	'该方法删除该folder下所有文件'
	file_list = list(filter(lambda x: r'.txt' in x ,os.listdir(folder)))
	for each in file_list:
		os.remove(folder + '\\'+each)
	return '删除成功'
			
			
			
			
			
			

if __name__ =='__main__':	

	# print(func('http://www.runoob.com/python3/python3-random-number.html','D:\A\B')	)
	# print(func('https://fishc.com.cn/forum-188-1.html','D:\A\B'))
	# print(func2('D:\A\B'))
	assert func4('http://url/api?param=2&param2=4') == {'param':'2','param2':'4'}
	func5('D:\A\B')
	
	
	
'''
总结：
1.若想将目录和文件名拼接成open()方法能够接受的形式，用os.path.join(目录名，文件名)
更简单的
2.对url进行解析可以使用urlparse
首先：import urllib.parse
urllib.parse.urlparse(url),将url分成不同的组件
urllib.parse.parse_qs(query组件)，解析url中query组件的参数，返回一个字典格式。
3.对于目录这种深层次的结构，使用递归进行操作很方便。比如递归删除每一层目录。


'''
