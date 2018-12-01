#字符串的格式化
'''


方法一:位置参数i,fishC,com传递给format方法，再由format方法对字符串:进行格式化
"{}.花括号里面写上数字".format(依次将字符串赋给相应次序的数字所在的位置)
方法二:关键字参数a,b,c,
"{},花括号里面写上字母".format(a = 字符串一 , b = 字符串二.......)
'''
strs = "{0} love {1}.{2}".format('i','fishC','com')
strs2 = "{a} love {b}.{c}".format(a = "i don\'t " , b = "fishC", c = "com")
print(strs)
print(strs2)
str3 = "{0:.1f}{1}".format(27.658,'GB')#注意这里的27.658是浮点数，不是字符串
print(str3) 


#当百分号%遇到字符串，就会发生神奇的化学反应
print('%c' % 97)
print('%c %c %c' % (97, 98, 99))