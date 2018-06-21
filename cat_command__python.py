#!/usr/bin/python3

import os 
import sys
import fileinput

#function for creating file
def create_file(mkfile):
	os.system('cat '+mkfile)
	#if mkfile == True:
	#	f=open(mkfile,'a+')	
	#	#f.write(" ")
	#	print(f)
	#	f.close()	
	#mkfile.write()
	for line in fileinput.input(mkfile,'w+'):
		if line.rstrip():
			print(line)

	
def read_file(filename):
	fopen=open(filename,'r+')
	f_read=fopen.read()
	print(f_read)
	fopen.close()


#copy the content of one file into another
def copy_file(source_file,dest_file):
	fopen=open(source_file,'r+')
	f_read=fopen.read()

	fo=open(dest_file,'w+')
	fo.write(f_read)
	fo.close()


#display the content of file with line number
def display_content(filename):
	with open(filename) as file:
		line =file.readline()
		count=1
		while line:
			print("line {}: {}".format(count,line.strip()))
			line = file.readline()
			count +=1
	
		

#cat highlight line-ends
def highlight_end(end_marker):
	with open(end_marker) as file:
		count=0		
		line =file.readline()
		
		while line:
			line =file.readline()
			
			
			print(line ,end=" ")
			print("@", end =' ')
			sys.stdout.flush()			
			#concat=line+'@'
			#for line in file:
			#	line+='@'
			#	print(line)
			#print(line + '@')				
			#print(line, '@')
			count +=1
		


#cat suppress repeated empty lines
def supress_repeated(supress_lines):
	for line in fileinput.hook_compressed(supress_lines,'r+'):
		if line.rstrip():
			print(line)



#main part of program

def main():
	file=sys.argv[0:4]
	length=len(file)
	print(length)

	if length == 4:
		if '-c' in file:
			source_file=sys.argv[2]
			dest_file=sys.argv[3]
			copy_file(source_file,dest_file)
			print("done")
		else:
			print("sorry")

	if length == 2:
		filename=sys.argv[1]
		read_file(filename)

	if length == 3:
		if  '>' in file :
			mkfile=sys.argv[2]
			create_file(mkfile)
		
		elif '>>' in file:
			mkfile=sys.argv[2]
			create_file(mkfile)


		elif '-n' in file:
			filename=sys.argv[2]
			display_content(filename)
			print("done")

		elif '-E' in file:
			end_marker=sys.argv[2]
			highlight_end(end_marker)

		elif '-s' in file:
			supress_lines=sys.argv[2]
			supress_repeated(supress_lines)
			print("done")
			
		else:
			for f in sys.argv[1:]:
				data=f
				read_file(data)
		

if __name__ == '__main__':
	main()
