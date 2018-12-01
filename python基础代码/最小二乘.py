#coding=UTF-8
#@Author:winyn
'''
最小二乘拟合
'''
import numpy as np
import scipy
from scipy.optimize import leastsq
import pylab as pl
#确定最小二乘拟合的次数
n = 9

#确定拟合的数据。本应该写入一个文件中读取，但为了方便以y = sin(x)为例，随机生成一系列的(x,y)
x = np.linspace(0,1,10)
x_print = np.linspace(0,1,1000)
#确定目标函数
def target_func(x):
	return np.sin(2*np.pi*x)
	
#确定基函数，此处为了简便，选择平凡基，1,x,x**2...x**n.此处用np.ploy1d多项式函数比较简单。
def s_func(p,x):
	f = np.poly1d(p)#多项数函数，p为系数
	return f(x)
p_init = np.random.randn(n)
#确定残差函数
def r_func(x):
	return target_func(x)-s_func(x)

plsq = leastsq(r_func,p_init)




print('拟合函数:')
pl.plot(x_print,target_func(x_print),label = 'real')
pl.plot(x_print,s_func(plsq[0],x_print),label = 'fitted curve')
pl.legend()
pl.show()