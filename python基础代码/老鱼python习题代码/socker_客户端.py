#coding=UTF-8
#Author:Winyn

import socket
#初始化socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接目标的ＩＰ和端口
s.connect(('127.0.0.1',9989))
#接收消息
print('--->>'+s.recv(1024).decode('utf-8'))
#发送消息
s.send(b'Hello,I am a Client')
print('--->>'+s.recv(1024).decode('utf-8'))
s.send(b'i love you')
#关闭socket
s.close()
