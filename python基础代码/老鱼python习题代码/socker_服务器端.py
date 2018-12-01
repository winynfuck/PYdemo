#coding=UTF-8
#Author:Winyn

import socket
#第一步：创建一个基于IPV4和TCP协议的Socket
#Socket绑定的ＩＰ（127.0.0.1为本机IP）与端口9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9989))
	
#第二步：监听连接
s.listen(5)
	
print('Waiting for connection...')

while True:
	#第三步：接收一个新连接
	sock,addr=s.accept()
	#创建新线程来处理TCP连接
	#第四步：接收传来的数据，并发送给对方数据
	print('Accept new connection from %s:%s'%addr)
	data = sock.recv(1024)
	sock.send(('Loop_Msg:%s'%data.decode('utf-8')).encode('utf-8'))
	#第五步：关闭socket
	sock.close()


	