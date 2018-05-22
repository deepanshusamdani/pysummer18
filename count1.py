#!/usr/bin/python

import  socket,time
from collections import Counter
import matplotlib.pyplot as plt
import backports.functools_lru_cache
 
rec_ip="192.168.43.84"
myport=8888
#                 ipv4       ,  for UDP   
#   only  for rec                      
#  below method with argument creating a socket called  s 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  now connecting ip  and port 
s.bind((rec_ip,myport)) 
#  buffer size 


def func():
	count_v=Counter(list)
	values=count_v.values()
	keys=count_v.keys()
	plt.bar(keys,values,color='r')
	plt.grid(True,color='b')
	plt.show()


list=[]
t=0

while t<10:
	data=s.recvfrom(1000)
	list.append(data[0])
	print list 
	if t==5:
		func()
	t=t+1


func()
		

	                      									
