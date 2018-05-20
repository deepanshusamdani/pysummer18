#!/usr/bin/python

import cgi
#import commands
print "Content-type:web.html"

print " "

web_data=cgi.FieldStorage()

out=web_data.getvalue('x')

#running as os command
#commands.getoutput(out)
#print ("<h1>")
print out
#print ("</h1>")
