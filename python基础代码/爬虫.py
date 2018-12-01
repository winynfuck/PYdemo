'''
python如何访问互联网
URL的一般格式为(带方括号[]的为可选项):
protocol://hostname[:port]/path/[;parameters][?query]#fragment
url有三部分组成
第一部分是协议：http,https,ftp,file,ed2k....
第二部分是存放资源的服务器的域名系统或者IP地址
（有时候要包含端口号，各种传输协议都有默认的端口号，如
http的默认端口为80）
第三部分是资源的具体地址，如目录或者文件名


通过使用包urllib
'''
#通过网站下载一只猫的图片
# import urllib.request as ur
# from random import choice
# size ={ 200,300,400,500,600}
# for i in range(100):
	# width =choice(list(size))
	# height =choice(list(size))
	# print(width,height)
	# response =ur.urlopen('http://www.placekitten.com/g/'+str(height)+'/'+str(width))
	# cat_img =response.read()
	# with open('D://A//'+'cat_img_'+str(i)+'.jpg','wb') as f:
		# f.write(cat_img)
	
	#respone =''
'''
通过utllib.request(url)可以得到一个对象。这个对象除了read()方法，还有
geturl方法、getinfo方法、getcode方法。


get是指从服务器请求获得数据
post是指向指定服务器提交被处理的数据

Remote Address服务器的地址和打开的端口号
Request URL urlopen打开的实际地址，内部嵌入的地址。
Request Method请求的方法
Status Code状态，亮绿灯正常响应。


Request Headers客户端也就是浏览器，常常用于服务端判断是否非人类访问。
通过User Agent来识别是浏览器访问还是代码访问。User Agent可以简单的自定义的。

From data就是我们post提交的主要内容

json是一种轻量级的数据交换格式，说白了就是以字符串的形式把python的数据结构封装起来。
用json.loads()返回python的数据封装。



'''



import urllib.request 
# import urllib.parse

# url ='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
# data ={}
# data[i] ='I love fish'
# #data[from]= 'AUTO'
# data[to]= 'AUTO'
# data[smartresult]= 'dict'
# data[client]= 'fanyideskweb'
# data[salt]= '1534818034861'
# data[sign]= 'f55ded782577c7a21016652ea5d41156'
# data[doctype]= 'json'
# data[version]= '2.1'
# data[keyfrom] = 'fanyi.web'
# data[action]= 'FY_BY_CLICKBUTTION'
# data[typoResult]= 'false'
# response = urllib.request.urlopen(url,data)
# html =response.read().encode('utf-8')
# print(html)

'''
服务器非常痛恨python爬虫重复访问，为此要将python代码进行隐藏，使得更像
普通用户通过浏览器的访问。
有两种方法：
第一种是request对象生成之前，设置urlopen的head为正常访问时候的User-Agent.
第二种是request对象生成之后，使用add_header('key','value')，追加header。


但是这种只是人家服务器端最简单的屏蔽手段。
假如你在一个图片网站下载图片，一秒钟访问几十次，人家服务器端可以识别你
的访问频率，若大于一个阕值，不管你的User-Agent是什么都会给你屏蔽掉，会给你
发个验证码。
这时有两种方法解决，一种是延迟访问时间，一种是使用代理。
延迟访问就是通过time模块的time.sleep(seconds)
使用代理，就是使用多个外部电脑帮你做事，并将结果返回给你。
步骤：
1.参数是一个字典{'类型':http等，'代理ip:端口号'}
proxy_support =urllib.request.ProxyHandler({})
2.定制、创建一个opener
opener =urllib.request.build_opener(proxy_support)
3.安装opener
urllib.request.install_opener(opener)
在此之后，只要你是用urlopen()函数，就默认调用这个定制的opener工作
若想用原来的urlopen的方式，可以用以下代码。
3.调用opener
opener.open(url)

可以建立一个iplist，随机选择ip
'''
import urllib.request 
url ='http://www.whatismyip.com.tw'
proxy_support =urllib.request.ProxyHandler({'http':'119.6.144.73:81'})
opener =urllib.request.build_opener(proxy_support)
opener.addheader= [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')]
urllib.request.install_opener(opener)
response =urllib.request.urlopen(url)
html =response.read().decode('utf-8')
print(html)
