#coding:utf-8
'''
在python中，比较运算符有> , < , >= , <= , != , == ,但这些都是双目运算符，说到双目运算符
，就不得不提单目运算符，其中有: - , ** (幂运算),有趣的是：**运算符的优先级和-有关，比如：
-3**2 = -9，如果-在左边，则**优先级高；
3**-2 = 0.1111111111111111，如果-在右边，则**优先级低；

再来说三目运算符，python本着简洁的原则，本来是没有三目运算符的，因为开创者觉得太复杂，但
后来应众多开发者要求，还是创造了属于python的三目运算符

x if 条件 y
条件为真，值为x,否则为y。
'''
#三目运算符如下

x = 3
y = 4
small = x if x < y else y
print(small)