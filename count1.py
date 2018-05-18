#!/usr/bin/python

import  socket,time
from collections import Counter
import matplotlib.pyplot as plt
import Tkinter
 
rec_ip="192.168.0.104"
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

dist=Counter(list)                                                                             
count_v= dist.values()
keys_k= dist.keys()

print dist
print count_v
print  keys_k

#print "value type :",type(count_v)
#print  "keys type :",type(keys_k)

plt.plot(keys_k,count_v,label="string",color='r')
plt.bar(keys_k,count_v)
plt.show()

time.sleep(4)


		
	
	
		
	#print "ip of client : ",data[1][0]
	#p=raw_input("enter reply msg")
	#s.sendto(p,Data[1])'''
	                      									
