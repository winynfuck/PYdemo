'''
re.findall()是找出所有匹配的字符并加入到一个列表中再返回列表。
正则表达式中要注意空格的使用。
*匹配前面的子表达式零次或多次，等价于{0,}
+匹配前面的子表达式一次或多次，等价于{1,}
?匹配前面的子表达式零次或一次，等价于{0,1}
'''
import re
print(re.findall(r'[a-z]','Fish.com'))
#\放在字符类中会出错，\表示转义符.脱字符^放在字符类中是取反的意思。
print(re.findall(r'[\n]','Fish.com\n'))
print(re.findall(r'[^a-z]','Fish.com\n'))#只能放在最前面，放在最后面表示脱字符本身
print(re.findall(r'[a-z^]','Fish.com\n^'))

#{m,n}表示重复m到n次{m,n}?表达非贪婪模式。
print(re.findall(r'c{3}','Fish.ccccom\n^'))

'''
#\序号，引用序号对应的子组所匹配的字符串，子组的序号从1开始计算
如果序号是以0开头，或者3个数字的长度。那么不会被用于引用对应的子组，而是用于匹配八进制数字
所表示的ASCII码值对应的字符。
'''
print(re.search(r'(Fish)(eat)\2','FishFisheateat.com\n^'))
print(re.search(r'(Fish)(eat)\060','FishFisheat0.com\n^'))

'''
临框断言，定位一个位置。
\A匹配输入字符串的开始位置
\Z匹配输入字符串的结束位置
\b匹配一个单词，单词被定义为Unidcode的字母数字或下划横线字符。
\B匹配非单词边界。

编译正则表达式：
如果你需要重复地私用某个正则表达式，那么你可以先将该正则表达式编译成模式对象。再使用re.compile()方法来编译。
'''
p = re.compile(r'[A-Z]')
p.search('i LOVE FISHc')
print(p.findall('i LOVE FISHc'))
