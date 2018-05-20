#!/usr/bin/python3

import time
import webbrowser
import datetime
from bs4 import BeautifulSoup
import requests
import  socket,time 

#import re
#import urllib.requests
option='''
Press  1 :  to  enter any thing - split each word and search on google 
Press  2 :  same  but find URL
Press  3 :  current time and date 
ptess  4 :  open any url
Press  5 :  open default browser 
Press  6 :  same  but find  images answer 
Press  7 :  all Network IP 
Press  8 :  enter domain name and find owner , email , contact 
'''
print  (option)

ch= input()
#--------------------------------------------------------------------------------

if   ch ==  '1'  :
	search_data= input("enter data : ")
	final_data=search_data.strip()
	#  above removing  leading and trailing space 
	done_data=final_data.split()
        #  spliting each word by space 
	for  i  in  done_data:
		webbrowser.open_new_tab('https://www.google.com/search?q='+i)

else :

	print  ("no chance !!")

#------------------------------------------------------------------------------------
if ch=='2':
	search_data1= input("enter data : ")
	final_data1=search_data1.strip()
	#  above removing  leading and trailing space 
	done_data1=final_data1.split()

	#scrapping the data to extract the urls

	for  i  in  done_data1:
		
		r=requests.get('https://www.google.com/search?q='+i)
		data=r.content
		#print (data)
		#print(data.cookies)
        	
	
		soup=BeautifulSoup(data,'html.parser')
		for link in soup.find_all('a'):
			print (link.get('href'))


else :
 	print("ohhooo")
#-------------------------------------------------------------------------------------

if   ch == '3' :
	now=datetime.datetime.now()
	print (now)
	print ("current month :",now.month )
	print ("current year  :",now.year )
	print ("current iso   :",now.isoformat())


else :	
	print("Aaaaiiiillaaa ye kya ho gya")

#----------------------------------------------------------------------------------------

if  ch == '4':
	url="https://www.google.com"
	webbrowser.open(url)
else :
	print("koi na hota h")

#---------------------------------------------------------------------------------------
	
if ch =='5':
	search_data1= input("enter data : ")
	final_data2=search_data1.strip()
	#  above removing  leading and trailing space 
	done_data2=final_data2.split()

	#scrapping the data to extract the urls

	for  i  in  done_data2:
		webbrowser.open_new_tab('https://www.google.com/images?q='+i)		
		
		'''r=requests.get('https://www.google.com/images?q='+i)
		data=r.content
	
		soup=BeautifulSoup(data,'html.parser')
		for link in soup.find_all('img'):
			print (link.get('src'))'''
#---------------------------------------------------------------------------
if ch == '6' :
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		
	
	ip_domain=input("enter domain name")
	
	#host_ip=socket.gethostbyname(ip_domain)
	for i in ip_domain:
		
		all_ip=s.connect((ip_domain))
		#ip_add=socket.gethostbyname(socket.gethostname())
		print (ip_add)
        
	#ip_add=socket.gethostbyname(socket.gethostname())
	#print ("ip address :",ip_add)


#--------------------------------------------------------------------------

if ch == '7':
	
	search_data2= input("enter data : ")
	final_data3=search_data2.strip()
	#  above removing  leading and trailing space 
	done_data3=final_data3.split()

	for i in done_data3:

		r=requests.get("https://myaccount.google.com/search"+i)
		data=r.content	
		#print (data)	


		soup=BeautifulSoup(data,'html.parser')
		for link in soup.find_all('email'):
				print (link.get('href'))




#-----------------------------------------------------------------------------
'''
if ch == '7':


	print((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), 		s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0])
'''

