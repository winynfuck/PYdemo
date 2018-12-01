
from bs4 import BeautifulSoup
from selenium import webdriver  
import urllib.request
 
urls = ('http://jandan.net/ooxx/page-{}#comments'.format(i) for i in range(233,238))
x = 1  
  
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'  
  
  
driver = webdriver.Chrome('E:\CENTbro\CentBrowser\Application\chromedriver.exe')
 
for url in urls:  
    print ("正在访问{}".format(url))   
    try:  
        driver.get(url)  
        driver.implicitly_wait(10)
        data = driver.page_source  
        soup = BeautifulSoup(data, 'lxml')  
        hrefs = soup.find_all('a',class_="view_img_link")  
    except:  
        print ("访问异常！")    
        continue  
  
    print ("开始下载")   
    for href in hrefs:  
        img = href.get('href')  
        img = "http:" + img  
        if img[-3:] != 'jpg':  
            continue  
        print ("正在下载第{}张图片".format(x))
        #保存文件
        urllib.request.urlretrieve(img,'G:\\pyth\\' + '%s.jpg' %(x))  
        x = x+1   