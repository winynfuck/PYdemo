#coding=UTF-8
#Author:Winyn
'''
题目一： 写一个网页数据操作类。完成下面的功能：

提示：需要用到urllib模块

get_httpcode()获取网页的状态码，返回结果例如：200,301,404等 类型为int 

get_htmlcontent() 获取网页的内容。返回类型:str

get_linknum()计算网页的链接数目。

'''
import urllib
class Get_web_date():
	def __init__(self,url):
		self.url = url
	def get_httpcode(self):
		'该方法获取网页的状态码'
		try:
			f = urllib.request.urlopen(self.url)
		except urllib.error.HTTPError:
			return '访问页面出错!'
		except urllib.error.URLError:
			return '访问页面出错!'
		else:
			return f.code
	def get_htmlcontent(self):
		'该方法获取网页的内容'
		try:
			f = urllib.request.urlopen(self.url)
		except urllib.error.HTTPError:
			return '访问页面出错!'
		except urllib.error.URLError:
			return '访问页面出错!'
		else:
			return str(f.readlines())
	def get_linknum(self):
		'该方法计算网页中链接数目'
		text = get_htmlcontent()
		return text.split('<a href=')-1
		
'''
体会下面一段代码，并用自己的话理解

'''
		
		
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print ('(Initialized SchoolMember父类的: %s)' % self.name)

    def tell(self):
        '''Tell my details.'''
        print ('Name:"%s" Age:"%s"' % (self.name, self.age),)

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print ('(Initialized Teacher: %s)' % self.name)

    def tell(self):
        print ('Salary: "%d"' % self.salary)

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print ('(Initialized Student子类的: %s)' % self.name)

    def tell(self):
        print ('Marks: "%d"' % self.marks)

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)

members = [t, s]
for member in members:
    member.tell()
'''
对一个类的子类进行实例化，继承的一些实例化参数会返回到父类中去执行。

'''
	
	
