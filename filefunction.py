def filefunction():
	fyle = open("out.txt", "r")
	init = 0
	while(True):
		c = fyle.read(10)
		if not c:
			break
		else:
			print(c)
			init += 10
			print(init)
	
	fyle = open("out.txt", "r")
	init = 0
	while(init<100):
		c = fyle.read(10)
		if not c:
			break
		else:
			print(c)
			init += 10
			print(init)
			
	fyle.seek(0,0)
	print(fyle.read(10))
	
	fyle = open("out.txt", "r")
	for i in range(5):
		fyle.readline()
		
	for line in fyle:
		print(line)
		
		
def filefunction1():
	import glob
	import re
	tot = 0
	for i in glob.glob("*.txt"):
		myfile = open(i, "r")
		strlist = myfile.read().split()
		if "Treasure" in strlist:
			print(i, strlist.count("Treasure"))
			tot += strlist.count("Treasure")
		else:
			print(i,0)
		myfile.close()
			
	print("Total count: ", tot)
	
def filefunction2():
	strlist = list()
	for line in reversed(open("file4.txt").readlines()):
		print(line.rstrip())
		strlist.append(line.rstrip())
		
	for string in strlist:
		print(string[::-1])

def filefunction4():
	fyle = open("file1.txt", "r+")
	print('File Name:', fyle.name)
	fyle.close()
	print('-'*50)
	
	fyle = open("file1.txt", "r")
	print('Name of the file:', fyle.name)
	fyle.flush()
	fyle.close()
	print('-'*50)
	
	fyle = open("file1.txt", "r+")
	print('Name of the file: ', fyle.name)
	fid = fyle.fileno()
	print("File Descriptor: ", fid)
	fyle.close()
	print('-'*50)
	
	
	fyle = open("file1.txt", "r+")
	print("Name of the file:", fyle.name)
	ret = fyle.isatty()
	print("Return value : ", ret)
	fyle.close()
	print('-'*50)
	
	fyle = open("file1.txt", "r+")
	print("Name of the file: ", fyle.name)
	for index in range(1):
	line = fyle
	print("Line No" ,index, line)
	fyle.close()
	print('-'*50)
	
	fyle = open("file1.txt", "r+")
	print("Name of the file: ", fyle.name)
	line = fyle.read(100)
	print("Read Line: " ,line)
	fyle.close()
	print('-'*50)
	
	fyle = open("file1.txt", "r+")
	print("Name of the file: ", fyle.name)
	line = fyle.readline()
	print("Read Line: ", line)
	line = fyle.readline(5)
	print("Read Line: ",line)
	fyle.close()
	print('-'*50)
	
	fyle = open("file1.txt", "r+")
	print("Name of the file: ", fyle.name)
	line = fyle.readlines()
	print("Read Line: ", line)
	line = fyle.readlines(2)
	print("Read Line: ",line)
	fyle.close()
	print('-'*50)
	
	fyle = open("file1.txt", "w+")
	print("Name of the file: ", fyle.name)
	line = fyle.readline()
	print("Read Line: ",line)
	print('-'*50)
	
	fyle.seek(0, 0)
	line = fyle.readline()
	print("Read Line: ",line)
	fyle.close()
	print('-'*50)
	
	fyle = open("file1.txt", "w+")
	print("Name of the file: ", fyle.name)
	line = fyle.readline()
	print("Read Line: " ,line)
	
	print('-'*50)
	pos = fyle.tell()
	print("Current Position: ",pos)
	fyle.close()
	print('-'*50)
	
	
	fyle = open("file1.txt", "w+")
	print("Name of the file: ", fyle.name)
	line = fyle.readline()
	print("Read Line: " ,line)
	print('-'*50)
	
	fyle.truncate()
	
	line = fyle.readline()
	print("Read Line: " ,line)
	fyle.close()
	print('-'*50)
	
	fyle = open("file1.txt", "w+")
	print("Name of the file: ", fyle.name)
	str = "This is 6th line"
	print('-'*50)
	
	#fyle.seek(0, 1)
	line = fyle.write( str )
	fyle.seek(0,0)
	lines=fyle.read()
	print(lines)
	fyle.close()
	print('-'*50)
	
	fyle = open("file1.txt", "w+")
	print("Name of the file: ", fyle.name)
	str = "This is 6th line"
	print('-'*50)
	
	#fyle.seek(0, 1)
	line = fyle.writelines( str )
	fyle.seek(0,0)
	lines=fyle.read()
	print(lines)
	fyle.close()
	print('-'*50)	