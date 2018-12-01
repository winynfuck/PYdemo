#coding=UTF-8
#Author:winyn
'''
给定一个函数，和积分上下限，用机械求积Romberg公式求积分。

'''
import numpy as np
# def func(x):
	# return sinx/x
	
class Romberg:
	def __init__(self,integ_uplimit,integ_dowlimit,func):
		'''
		初始化积分上限integ_uplimit和积分下限integ_dowlimit
		输入一个函数，输出函数在积分上下限的积分
		
		'''
		self.integ_uplimit = integ_uplimit
		self.integ_dowlimit = integ_dowlimit
		self.func = func
	def calc(self):
		'''
		计算Richardson外推算法的四个序列
		
		'''
		t_seq1 = np.zeros(5,'f')
		s_seq2 = np.zeros(4,'f')
		c_seq3 = np.zeros(3,'f')
		r_seq4 = np.zeros(2,'f')
		print(r_seq4)
		#循环生成hm间距序列
		hm = [(self.integ_uplimit-self.integ_dowlimit)/(2**i)for i in range(0,4)]
		#循环生成t_seq1
		t0 = (1/2)*(self.integ_uplimit-self.integ_dowlimit)\
		*(self.func(self.integ_uplimit)+self.func(self.integ_dowlimit))
		t_seq1[0] = t0
		sum = 0
		for i in range(1,4):
			#累加和
			for each in range(1,2*i-1):
				sum = sum +self.func(self.integ_dowlimit + (2*each-1)*hm[i])
			temp = 1/2 * t_seq1[i-1] + hm[i]*sum
			#求t_seql的1-4位
			t_seq1[i] = temp
		print(t_seq1)
		#循环生成s_seq2
		s_seq2 = [ (4**1*t_seq1[i+1]- t_seq1[i])/(4**1 -1) for i in range(0,3)]
		print(s_seq2)
		#循环生成c_seq3
		c_seq3 = [ (4**2*s_seq2[i+1]- s_seq2[i])/(4**2 -1) for i in range(0,2)]
		#循环生成r_seq4
		r_seq4 = [ (4**3*c_seq3[i+1]- c_seq3[i])/(4**3 -1) for i in range(0,1)]
		print(r_seq4)
		if (r_seq4[0]-r_seq4[1])<=0.0001:
			return r_seq4[0]
		else:
			print('wrong')
			


			
rom = Romberg(0,1,lambda x:np.sin(x)/x )
rom.calc()
		
			
		
		
		
		
		