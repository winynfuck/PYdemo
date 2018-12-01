'''


'''
import urllib.request
import os
import os.path
import re
import random
def get_page_source(url):
	
	req =urllib.request.Request(url)#修改访问的Request对象，避免被屏蔽
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0')
	response =urllib.request.urlopen(url)#打开url对应的Request对象，返回response对象
	html =response.read()	#response对象解码，html是返回的以字符串表示的网页源代码
	return html

def get_page(url):
#设置访问的Request对象，避免被屏蔽
	html =get_page_source(url).decode('utf-8')
	split_start =html.find("current-comment-page")+23
	split_stop =html.find(']',split_start)
	num =html[split_start:split_stop]
	return num
def find_imgs(url):
	print(url)
	
	url2 = 'http://jandan.net/ooxx/page-43#comments'
	n = 0
	html =get_page_source(url).decode('utf-8')
	html2 =get_page_source(url2).decode('utf-8')
	print(html == html2)
	
	
	pa = re.compile(r'<img src="(.*?\.(?:jpg|jpeg|gif|bmp|png))"')
	img_addrs = re.findall(pa,html)
	# x = 0
	# for imgurl in imglist:
		# urllib.urlretrieve(imgurl,'%s.jpg' % x)
		# x+=1
	
	# a =html.find('img src=')
	
	# while a != -1:
		# n +=1
		# b = html.find('.jpg',a,a+255)
		# if b != -1:
			# img_addrs.append(html[a+9:b+4])
		# else:
			# b = a +9
		# a = html.find('img src=',b) 
			
	return img_addrs
	# for each in img_addrs:
		# print(each,end ='\n')
	
		
		
	

	
def save_imgs(folder,img_addrs):
	for each in img_addrs:
		filename = each.split('/')[-1]
		with open(filename,'wb') as f:
			img =get_page_source(each)
			f.write(img)

def download_MM(local_folder ='D://MM_jpg',pages =10):
	if os.path.exists(local_folder) == False:
		os.mkdir(local_folder)#创建保存数据的文件夹
	os.chdir(local_folder)#更改当前目录
	url ='http://jandan.net/ooxx'
	
	page_num =int(get_page(url))
	
	for i in range(pages):
		page_num -=1
		print(page_num)
		page_url = url +'/page-'+str(page_num)+'#comments'
		print(page_url)
		img_addrs =find_imgs(page_url)
		save_imgs(local_folder,img_addrs)
#if __name__ ==' __main__':
download_MM() 
	