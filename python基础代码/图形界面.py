'''
easygui的使用
'''
import easygui as g
import sys

# while 1:
	# g.msgbox("嗨，欢迎进入第一个界面小游戏^_^",'开始')

	# msg ="请问你希望在鱼C工作室学习到什么知识呢？"
	# title = "小游戏互动"
	# choices = ["谈恋爱", "编程", "OOXX", "琴棋书画"]
	
	# choice = g.choicebox(msg, title, choices)

	# # 注意，msgbox的参数是一个字符串
	# # 如果用户选择Cancel，该函数返回None
	# g.msgbox("你的选择是: " + str(choice), "结果")

	# msg = "你希望重新开始小游戏吗？"
	# title = "请选择"

	# # 弹出一个Continue/Cancel对话框
	# if g.ccbox(msg, title):
			# pass            # 如果用户选择Continue
	# else:
			# sys.exit(0)     # 如果用户选择Cancel，该函数返回None
			
choices =['愿意','不愿意','还在考虑']
msg = '你愿意和我在一起吗'
reply = g.choicebox(msg,choices = choices )
if reply == '愿意':
	g.msgbox('我爱你',ok_button ='结束')
elif reply == '不愿意':
	g.msgbox('我还是会好好的生活',ok_button = '结束')
else:
	g.msgbox('我等你',ok_button = '结束')
	
	
	
	
	
	
	
'''
GUI 编程中一个常见的场景就是要求用户设置一下参数，然后保存下来，以便下次用户使用你的程序的时候可以记住他的设置。

为了实现对用户的设置进行存储和恢复这一过程，EasyGUI 提供了一个叫做 EgStore 的类。

为了记住某些设置，你的应用程序必须定义一个类（下面案例中的 “Settings”）继承自 EgStore 类。

然后你的应用程序必须创建一个该类的实例化对象（下面案例中的 “settings”）。

设置类的构造函数（__init__ 方法）必须初始化所有的你想要它所记住的那些值。

一旦你这样做了，你就可以在 settings 对象中通过设定值去实例化变量，从而很简单地记住设置。

之后使用 settings.store() 方法在硬盘上持久化保存。

下面创建一个叫做 “Settings” 的类：

'''
	
	
	
from easygui import EgStore

# 定义一个叫做“Settings”的类，继承自EgStore类
class Settings(EgStore):

	def __init__(self, filename):  
		# 需要指定文件名
		# 指定要记住的属性名称
		self.author = ""
		self.book = ""

		# 必须执行下面两个语句
		self.filename = filename
		self.restore()

# 创建“Settings”的实例化对象“settings”
settingsFilename = "settings.txt"
settings = Settings(settingsFilename)

author = "小甲鱼"
book = "《零基础入门学习Pyhon》"

# 将上面两个变量的值保存到“settings”对象中
settings.author = author
settings.book = book
settings.store()
print("\n保存完毕\n")


'''
使用 EasyGUI 编写 GUI 程序，有时候难免会产生异常。当然这取决于你如何运行你的应用程序，当你的应用程序崩溃的时候，堆栈追踪可能会被抛出，或者被写入到 stdout 标准输出函数中。

EasyGUI 通过 exceptionbox() 函数提供了更好的方式去处理异常。

当异常出现的时候，exceptionbox() 会将堆栈追踪显示在一个 codebox() 中，并且允许你做进一步的处理。

exceptionbox() 很容易使用，下面举个例子：
'''
try:
		print('I Love FishC.com!')
		int('FISHC') # 这里会产生异常
except:
		g.exceptionbox()
	