#阶乘的迭代实现
def jiecheng(x):
	sum = 1
	for i in list(range(1,x+1)):
			sum = sum * i
	return sum
print(jiecheng(5))
#阶乘的递归实现
def jiecheng2(x):
	if x =1:
		return 1
	else:
		return x *jiecheng2(x-1)
			

#斐波那契数列的迭代实现			
def feibonaqi(n):
	data = [1,1]
	for i in range(1,n+1):
		temp = data[i] + data[i-1]
		data.append(temp)
	return data[n-1]
print(feibonaqi(35))
		
	
#斐波那契数列的递归实现
def feibonaqi2(n):
		if n ==1 or n ==2:
			return 1
		else:
			return (feibonaqi2(n-1)+feibonaqi2(n-2))
print(feibonaqi2(35))

#汉诺塔的递归实现
def hanoi(n , x , y , z):
	if n == 1:
		print(x+ '->' + z)
	else:
		hanoi(n-1,x , z , y)#第一步将n-1个塔从x放到y
		print(x + '->' + z)#第二步将第n层的塔从x放到z
		print(y + '->' + z)#第三步将n-1层塔从y放到z
hanoi(3 , 'X' , 'Y' , 'Z')
		