#!/usr/bin/python

import  socket,time 
import thread ,os
import pyttsx
import speech_recognition as sr

#from gtts import gTTS
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#t=time.time()+10
#li=[2,4,5,6,7,9]
#print li
#max_li=max(li)
#print max_li
#for i in li:

#def sender_th():

while True:
	#msg=raw_input("enter a message to send : ")
	#get audio  from the microphone

	r=sr.Recognizer()
	q=s.sendto(r,("192.168.43.84",8888))
	with sr.Microphone() as source:
		print ("speak : ")
	audio=r.listen(source)
	try:
		print("you speak : " +r.recognize_google(audio))
	except sr.UnKnownValueError:
		print("could not understand audio")
	except sr.rzequestError as e:
		print("could not request results; {0}".format(e))	

#thread.start_new_thread(sender_th,())

#while True:
#	pass












