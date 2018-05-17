#!/usr/bin/python

import  socket,time
from collections import Counter
 
rec_ip="192.168.43.84"
myport=8888
#                 ipv4       ,  for UDP   
#   only  for rec                      
#  below method with argument creating a socket called  s 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  now connecting ip  and port 
s.bind((rec_ip,myport)) 
#  buffer size 
list=[]
t=time.time()+10
while time.time()<t:
	data=s.recvfrom(1000)
	print "data from client : ",data[0]
	list.append(data[0])
	print list 
'''
ab=[]
word=list
for i in word:
	a=word.count(i)
	ab.append(a)
print ab
'''
print Counter(list)






		
	
	
		
	#print "ip of client : ",data[1][0]
	#p=raw_input("enter reply msg")
	#s.sendto(p,Data[1])'''
	
