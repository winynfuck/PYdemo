#coding: utf-8
'''
爬取煎蛋网上的美女图片
'''

import urllib.request
import os
import os.path
import re
from bs4 import BeautifulSoup
import json
import time
from selenium import webdriver

def get_page_source(url):
	'根据输入的url，以字符串的形式输出网页源代码'
	driver =webdriver.PhantomJS(executable_path="D:\ruanjian\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe")#使用下载好的phantomjs，网上也有人用firefox，chrome，但是我没有成功，用这个也挺方便
	driver.set_page_load_timeout(30)
	time.sleep(3)
	html=driver.get(url)#使用get方法请求url，因为是模拟浏览器，所以不需要headers信息    
	html=driver.page_source#获取网页的html数据
	soup=BeautifulSoup(html,'lxml')#对html进行解析，如果提示lxml未安装，直接pip install lxml即可
	print(soup)

def get_page_num(url):
	html =get_page_source(url).decode('utf-8')
	a = html.find("current-comment-page")+23
	b = html.find(']',a)
	num =html[a:b]
	return num
	
	
def find_imgs(url):
	html =get_page_source(url).decode('utf-8')
	print(html)
	#img_addrs = []
	#pa =re.compile(r'<img src="(*\.*.cn*\.(?:jpg|jpeg|gif|bmp|png))"')
	pa =re.compile(r'http:.+\.jpg')
	img_addrs = re.findall(pa,html)
	print(img_addrs)
	return img_addrs
	
	
	
def save_imgs(img_adds):
	for each in img_addrs:
		filename = each.split('/')[-1]
		with open(filename,'wb') as f:
			#获取图片的实际步骤
			img =get_page_source(each)
			f.write(img)
	


def download_mm2(folder ='D://MM_jpg',pages = 10):
	#创建存储爬取图片的文件夹
	if os.path.exists(folder) ==False:
		os.mkdir(folder)
	os.chdir(folder)#更改当前目录
	
	
	url_init ='http://jandan.net/ooxx'#初始url
	
	#根据初始url获取首页的num
	page_num = int(get_page_num(url_init))
	
	
	for i in range(pages):
			page_num -= 1
			#根据首页的num获取其他页面的url
			page_url = url_init	+'/page' + str(page_num) +'#comments'
			
			#根据其他页面的url获得图片地址,返回地址的列表
			img_addrs = find_imgs(page_url)
			
			#根据地址的列表，获取图片并保存到本地
			save_imgs(folder , img_addrs)
			
download_mm2()