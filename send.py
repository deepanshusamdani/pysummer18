#!/usr/bin/python

import  socket,time 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#t=time.time()+10
t=0
while t<10:
	msg=raw_input("enter a message to send : ")
	q=s.sendto(msg,("192.168.43.84",8888))
	t=t+1
	#print s.recvfrom(100)
