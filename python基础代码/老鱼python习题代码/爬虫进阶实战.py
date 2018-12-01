#coding=UTF-8
#Author:Winyn

#---------------------------------------------------------------------------------------------------
'''
作业1：

url :"http://money.163.com/special/pinglun/"
抓取第一页的新闻信息，并按照以下规格输出。

[

  {'title':'生鲜电商为何难盈利？','created_at':'2013-05-03 08:43','url':'http://money.163.com/13/0503/08/8TUHSEEI00254ITK.html'}

  {'title':'生鲜电商为何难盈利？','created_at':'2013-05-03 08:43','url':'http://money.163.com/13/0503/08/8TUHSEEI00254ITK.html'}


]


'''
import urllib.request
url ='http://money.163.com/special/pinglun/'
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
response = urllib.request.urlopen(url)
f_text = response.read().decode('gbk','ignore')

#利用正则表达式提取出页面信息。
#提取标题title
import re
compile_title = r'title=".*?" class="newsimg"'
titles = re.findall(compile_title,f_text)
titles_lens = len(titles)
for i in range(0,titles_lens):
	titles[i] = titles[i][7:-18]


#提取时间time	
compile_time = r'<span class="time">(.*?)</span>'
times = re.findall(compile_time,f_text)



#提取url	
compile_url = r'href=".*?" title=".*?" class="newsimg" lang=".*?"><img '
urls = re.findall(compile_url,f_text)
urls_lens = len(urls)
for i in range(0,urls_lens):
	urls[i] = urls[i].split('title')[0][6:-2]


result =[]

for i in range(0,urls_lens):
	dict_temp={}#因为每次都要刷新，因此这里用空字典
	dict_temp['title']=titles[i]
	dict_temp['creat_at']=times[i]
	dict_temp['url']= urls[i]
	result.append(dict_temp)
	
# print(result)

#--------------------------------------------------------------------------------------------------
'''
作业2：

url: "http://search.jd.com/Search?keyword=%E5%B9%BC%E7%8C%AB%E7%8C%AB%E7%B2%AE&enc=utf-8#filter"


print jd_search(keyword)

[dict,dict,dict]
dict {pic:'',title:'',price:'',url:''}

'''
#连接网页获取源代码
url2 ='http://search.jd.com/Search?keyword=%E5%B9%BC%E7%8C%AB%E7%8C%AB%E7%B2%AE&enc=utf-8#filter'
req2 = urllib.request.Request(url2)
req2.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
response2 = urllib.request.urlopen(url2)
f_text2 = response2.read().decode('utf-8','ignore')
# print(f_text2)

#利用正则表达式提取出页面信息。
#提取标题title
import re
# compile_title2 = r'<div class="p-img"><a target="_blank" title=".*?" href='
# titles2 = re.findall(compile_title2,f_text2)
# titles_lens2 = len(titles2)
# for i in range(0,titles_lens2):
	# titles2[i] = titles2[i][26:-7]
# print(titles2)

#提取价格price
compile_prices = r'strong class=.*? data-done="\d"><em>\W</em><i>.*?</i>'
prices = re.findall(compile_prices,f_text2)
lens_prices = len(prices)
for i in range(0,lens_prices):
	prices[i] = prices[i].split('</em>')[1][3:-5]
	
# print(lens_prices)

#提取url


compile_url2 = r'<a target="_blank" title=".*?" href=".*?" onclick="searchlog'
urls2 = re.findall(compile_url2,f_text2)
lens_urls2 = len(urls2)
urls_final = []
for i in range(0,lens_urls2):
	urls2[i] = urls2[i].split('href=')[1][1:-20]
	if not urls2[i].startswith('https:'):
		urls2[i] = 'https:'+urls2[i]
	if urls2[i] not in urls_final:
		urls_final.append(urls2[i])
# print(len(urls_final))


