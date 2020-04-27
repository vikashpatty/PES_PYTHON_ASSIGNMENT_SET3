#!/usr/bin/env python
# coding: utf-8

# 41.Using calendar module perform following operations.
# 
# a) Print the 2016 calendar with space between months as 10 characters.
# 
# b) How many leap days between the years 1980 to 2025.
# 
# c) Check given year is leap year or not. 
# 
# d) print calendar of any specified month of the year 2016.

# In[23]:


import calendar

for i in range(1,13):
    print(calendar.month(2016,i))

print('-'*50)
print(calendar.leapdays(1980,2025))

print('-'*50)
x=int(input('Enter Year to check if leap or not: '))
if calendar.isleap(x)==True:
    print(str(x)+' is leap year')

print('-'*50)
print(calendar.month(2016,3))


# 42.Write a program to generate a Fibonacci series using a function called fib(n),
# 
# a) Where ‘n’ is user specified argument specifies number of elements in the series.

# In[29]:


def fib(n):
    first = 0
    second= 1
    third = 0
    while(n>third):
        print(first)
        total = first + second
        first = second
        second = total
        third += 1   
x=int(input('Enter the number of elemnt for fibonacci series: '))        
fib(x)


# 43.Write a program to search given element from the list. Use your own function to search an element from list. 
# 
# Note: Function should receive variable length arguments and search each of these arguments present in the list.

# In[51]:


def ele(list1,x):
    for i in list1: 
        if i in list1: 
            print('Element found')
            break
        else:
            print('Element not found')
            break
list2=[1,2,3,4,5,6,7,8,9,10]
print(list2)
print('-'*50)
z=int(input('Write a Number to find in the list: '))
ele(list2,z)


# 44.Write a program with lambda function to perform following.
# 
# a) Perform all the operations of basic calculator (Add, Sub, Multiply, Divide, Modulus, Floor division)
# 

# In[59]:


sumlambda = lambda x,y: x+y
sublambda = lambda x,y: x-y
mullambda = lambda x,y: x*y
divlambda = lambda x,y: x/y
modlambda = lambda x,y: x%y
fldlambda = lambda x,y: x//y

z=int(input('Enter 1st number: '))
k=int(input('Enter 2nd number: '))
print('Sum using lambda: '+str(sumlambda(z,k)))
print('Sub using lambda: '+str(sublambda(z,k)))
print('Mul using lambda: '+str(mullambda(z,k)))
print('Div using lambda: '+str(divlambda(z,k)))
print('Mod using lambda: '+str(modlambda(z,k)))
print('Fld using lambda: '+str(fldlambda(z,k)))


# 45.Write a program to check given string is Palindrome or not. 
# 
# (Use function Concepts and Required keyword, Default parameter concepts) i.e Reverse the given string and check whether it is same as original string, if so then it is palindrome. 
# 
# Example: String "malayalam" when reversed will be "malayalam" hence palindrome.

# In[60]:


def pal(x):
    if x == x[::-1]:
        print('Palindrome')
    else:
        print('Not Palindrome')

y=str(input('Enter the string to check palindrome: '))
pal(y)


# 46.Write a function to find the biggest of 4 numbers.
# 
# a) All numbers are passed as arguments separately (Required argument)
# 
# b) use default values for arguments (Default arguments)

# In[62]:


def bada(a,b,c,d):
    if a>b and a>c and a>d:
        print(str(a)+' is biggest number')
    elif b>a and b>c and b>d:
        print(str(b)+' is biggest number')
    elif c>a and c>b and c>d:
        print(str(c)+' is biggest number')
    else:
        print(str(d)+' is biggest number')
        
e=int(input('enter 1st number: '))
f=int(input('enter 2nd number: '))
g=int(input('enter 3rd number: '))
h=int(input('enter 4th number: '))
bada(e,f,g,h)


# 47.Write function to extend the tuple with elements of list. 
# 
# Pass list and Tuple as parameter to the function.

# In[65]:


def tupext(tup1,list1):
    return tup1+tuple(list1)

tup=(1,2,3,4)
lis=[5,6,7,8]
tupext(tup,lis)    


# 48.Create a Calculator with the following functions.
# 
# a) Addition/subtraction/multiplication and division of two numbers (Note: Create separate function for each operation)
# 
# b) Find square root of a given number. (Use keyword arguments in your function)
# 
# c) Create a list of sub strings from a given string, such that sub strings are created with given character.
# i.e. String = "Pack: My: Box: With: Good: Food"
# 
# Create sub strings with the delimiter character ":" such that the following sub strings are created. 
# 
# substrlist=[Pack, My, Box, With, Good, Food] Note : Function should take at least 2 parameters ( Main string and delimiter character) return value from function will be list of substring.

# In[70]:


sumlambda = lambda x,y: x+y
sublambda = lambda x,y: x-y
mullambda = lambda x,y: x*y
divlambda = lambda x,y: x/y
modlambda = lambda x,y: x%y
fldlambda = lambda x,y: x//y

z=int(input('Enter 1st number: '))
k=int(input('Enter 2nd number: '))
print('Sum using lambda: '+str(sumlambda(z,k)))
print('Sub using lambda: '+str(sublambda(z,k)))
print('Mul using lambda: '+str(mullambda(z,k)))
print('Div using lambda: '+str(divlambda(z,k)))
print('Mod using lambda: '+str(modlambda(z,k)))
print('Fld using lambda: '+str(fldlambda(z,k)))
print('-'*50)
import math

sqrlambda = lambda x:math.sqrt(x)

a=int(input('Enter number to get squrroot: '))
print('-'*50)
print('Square root is: '+str(sqrlambda(a)))

String = "Pack: My: Box: With: Good: Food"
def sublist(string,k):
    return string.split(k)
print('-'*50)
print(sublist(String, ": "))


# 49.Write a program to perform following file operations
# 
# a) Open the file in read mode and read all its contents on to STDOUT.
# 
# b) Open the file in write mode and enter 5 new lines of strings in to the new file.
# 
# c) Open file in Append mode and add 5 lines of text into it.

# In[73]:


fyle = open("out.txt", "r")
print(fyle.read())
fyle.close()

fyle = open("sam.txt", "w")
fyle.write("Hi i'm vikash")
fyle.write("love python")
fyle.write("doing this to")
fyle.write("gain more handson")
fyle.write("so i can get some project")
fyle.close()

fyle = open("out.txt", "a")
fyle.write("Hi i'm vikash")
fyle.write("love python")
fyle.write("doing this to")
fyle.write("gain more handson")
fyle.write("so i can get some project")
fyle.close()


# 50.Write a program to open the existing file in read mode and perform following tasks,
# 
# a) Rad 10 character at a time and then print its current position of file object. Repeat this operation till the EOF.
# 
# b) Reset the file pointer after reading 100 Character from file (Use Seek function to reset)
# 
# c) Open the file in read mode and start printing the contents from 5th line onwards.

# In[75]:


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


# 51.In a given directory search all text files for the pattern "Treasure".
# 
# a) Find how many text files has the pattern.
# 
# b) Count how many times pattern repeats in each file Note: Create at least 4 text files in a directory and keep the pattern in at least 2 files. Repeat the pattern in the file many times.
# 

# In[77]:


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


# 52.Open existing text file and reverse its contents. i.e
# 
# a) print the last line as first line and first line as last line (Reverse the lines of the file)
# 
# b) print characters of file from last character of file till the first character of the file.(Reverse entire contents of  file )

# In[79]:


strlist = list()
for line in reversed(open("file4.txt").readlines()):
    print(line.rstrip())
    strlist.append(line.rstrip())
    
for string in strlist:
    print(string[::-1])


# 53.Open the file is read & write mode and apply following functions
# 
# a) All 13 functions mentioned in Tutorial File object table.
# 

# In[99]:


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


# 54.Write a program to handle the following exceptions in you program.
# 
# a) KeyboardInterrupt
# 
# b) NameError 
# 
# c) ArithmeticError Note: Make use of try, except, else: block statements.

# In[100]:


try:
    x = int(input("Enter 1st number : "))
    y = int(input("Enter 2nd number : "))
    print ("The result of two divided numbers are ", x/y)
except KeyboardInterrupt:
    print('KeyboardInterrupt Occured')
except NameError:
    print('NameError occured')
except ArithmeticError:
    print('ArithmeticError occured')    


# 55.Write a program for converting weight from Pound to Kilo grams.
# 
# a) Use assertion for the negative weight.
# 
# b) Use assertion to weight more than 100 KG

# In[108]:


def conv(x):
    try:
        assert x>=0
        kg=x*0.45359237
        assert kg>100
        print("Weigh in KG: ",kg)
    except AssertionError:
        print("Either negative or less than 100kg")
        
Y=int(input('Write the value in Pound to get in KG: '))
conv(Y)


# 56.Write a program to handle following exceptions using Try block.
# 
# a) IO Error while you try writing contents into the file that is opened in read mode only.
# 
# b) ValueError

# In[113]:


try:
    fyle = open('file1.txt','r')
    print(fyle.read())
    fyle.write("Vikash")
except IOError:
    print('File Opened Read mode only')

try:
    n = int(input("Enter value:"))
except ValueError:
    print('ValueError')


# 57.Try implementing atleast any 5 exceptions in you program.

# In[115]:


try:
    fyle = open('file1.txt','r')
    print(fyle.read())
    fyle.write("Vikash")
except IOError:
    print('File Opened Read mode only')

try:
    n = int(input("Enter value:"))
except ValueError:
    print('ValueError')
    
try:
    x = int(input("Enter 1st number : "))
    y = int(input("Enter 2nd number : "))
    print ("The result of two divided numbers are ", x/y)
except KeyboardInterrupt:
    print('KeyboardInterrupt Occured')
except NameError:
    print('NameError occured')
except ArithmeticError:
    print('ArithmeticError occured') 


# 58.Create file called  "calc.py" which has following functions
# 
# i) functions to add 2 numbers
# 
# ii) function to find diff of 2 numbers
# 
# iii) function to multiply 2 numbers
# 
# iv) all maths operations ( sqrt, div, floor div, modulus, primenumber)
# 
# v) Fibonacci series
#         
# a) Write a new program in file "maths.py" such that you import functions of file "calc.py" to your new program
# 
# b) Use From <module> import <function> statement to import only few function  from calc module.

# In[3]:


#program for calc.py
def Add(num1,num2):
    return(num1+num2)


def Subtract(num1,num2):
    return(num1-num2)


def Multiply(num1,num2):
    return(num1*num2)


def SquareRoot(num):
    import math
    return math.sqrt(num)


def Divide(num1,num2):
    return(num1/num2)


def FloorDiv(num1,num2):
    return(num1//num2) 


def Modulus(num1,num2):
    return(num1%num2)


def Prime(num1):
    x=2;flag=0
    while x<=num1/2:
        if num1%x==0:
            flag=flag+1
        x=x+1
      
    return(flag) 
    if flag==0:
        print('Prime:')
    else:
        print('not prime')
    

def fib(num1):
    if num1==1:
        print('0')
    elif num1==2:
        print('0,1')
    else:
        print('0,1')
        a=0;b=1
        for x in range(3,num1+1):
            c=a+b
            print(c)
            a=b
            b=c
#program for maths.py            
import calc

num1=20;num2=10
print(calc.Add(num1,num2))
print(calc.Subtract(num1,num2))
print(calc.Multiply(num1,num2))
print(calc.SquareRoot(num1))
print(calc.Divide(num1,num2))
print(calc.FloorDiv(num1,num2))
print(calc.Modulus(num1,num2))
print(calc.Prime(num1))
print(calc.fib(num1))

from calc import SquareRoot,Prime,fib
print(calc.SquareRoot(num1))
print(calc.Prime(num1))
print(calc.fib(num2))


# 59.Create file called "stringop.py" which has following functions
# 
# i) functions to sort numbers (Use loops for  sorting, do not use built in function)
# 
# ii) function to search given element through binary search method.(Refer to net for the Binary search algorithm)
# 
# iii) function to reverse the given string 
# 
# Write new program in file strpackage.py such that you import functions of file "stringop.py" to your new program

# In[3]:


#stringop.py code
def SortList(num):
    for x in range(len(num)-1,0,-1):
        for i in range(x):
            if num[i]>num[i+1]:
                temp = num[i]
                num[i] = num[i+1]
                num[i+1] = temp
    print(num)


def binary_search(list_1,x):
    
    findex = 0
    lindex = len(list_1)-1
    f = 0
    while( findex<=lindex and not f):
        mid = (findex + lindex)//2
        if list_1[mid] == x :
            f = 1
        else:
            if x < list_1[mid]:
                lindex = mid - 1
            else:
                findex = mid + 1
    return f


def ReverseString(string):
    reverse=string[::-1]
    print(reverse)

#program for strpackge.py
import stringop


n=[23,24,67,1,0,21]
stringop.SortList(n)

s=input("Enter element to search:")
res=int(stringop.binary_search(n,s))
if res==1:
    print('found')
else:
    print('Not found')


z=str(input("Enter string to reverse"))
stringop.ReverseString(z)


# 60.Create a package of all programs you have done in earlier.
# 
# a. All programs related to strings - Stringpackage
# 
# b. All programs related to Lists -ListPackage
# 
# c. All programs related to Tuple - TuplePackage
# 
# d. All programs related to Dictionary -DictionaryPackage
# 
# e. All programs related to Functions - FunctionPackage
# 
# f. All programs related to Files  -- FilePackage

# In[6]:


#----------------------------------------------------------------------------------------------------------------------------
#stringpackage
def Stringpackage():
    x=str(input("Enter The string to perform 1st five builtin function:"))
    #give input This is 1st string
    
    #Return a capitalized version of the string.
    #More specifically, make the first character have upper case and the rest lower case.
    print(x.capitalize())
    
    #Return a version of the string suitable for caseless comparisons.
    print(x.casefold())
    
    #Return a centered string of length width.
    #Padding is done using the specified fill character (default is a space).
    print(x.center(10,'z'))
    
    #Return the number of non-overlapping occurrences of substring sub in
    #string S[start:end].  Optional arguments start and end are
    #interpreted as in slice notation.
    sub='i'
    print(x.count(sub,1,10))
    
    sub='lol'
    print(x.count(sub))
    
    #encode(self, /, encoding='utf-8', errors='strict')
    #Encode the string using the codec registered for encoding.
    #The encoding in which to encode the string.
    #errors
    #The error handling scheme to use for encoding errors.
    #The default is 'strict' meaning that encoding errors raise a
    #UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
    #'xmlcharrefreplace' as well as any other name registered with
    #codecs.register_error that can handle UnicodeEncodeErrors.
    print(x.encode('utf-8','strict'))
    
    0
    
    y=str(input("Enter string to perform next 5 function:"))
    #give input this is 2nd string
    
    z='ing'
    
    #Return True if S ends with the specified suffix, False otherwise.
    #With optional start, test S beginning at that position.
    #With optional end, stop comparing S at that position.
    #suffix can also be a tuple of strings to try.
    
    print(y.endswith(z))
    print(y.endswith(z,10))
    z='s'
    print(y.endswith(z, 1, 4))
    print(y.endswith(z, 2, 6))
    
    #Return a copy where all tab characters are expanded using spaces.
    #If tabsize is not given, a tab size of 8 characters is assumed.
    
    print("\noriginal string:",y)
    print(y.expandtabs())
    print(y.expandtabs(16))
    
    #Return the lowest index in S where substring sub is found,
    # that sub is contained within S[start:end].  Optional
    #arguments start and end are interpreted as in slice notation.
    #Return -1 on failure.
    
    k='tr'
    print(y.find(k))
    print(y.find(k, 10))
    print(y.find(k, 40))
    
    #Return a formatted version of S, using substitutions from args and kwargs.
    #The substitutions are identified by braces ('{' and '}').
    
    l="Hi i'm {age:.2f} year old!"
    print(l.format(age = 200))
    
    #Return a formatted version of S, using substitutions from mapping.
    #The substitutions are identified by braces ('{' and '}').
    #print(l.format_map())
    
    #Return the lowest index in S where substring sub is found, 
    #such that sub is contained within S[start:end].  Optional
    #arguments start and end are interpreted as in slice notation.
    #Raises ValueError when the substring is not found.
    print(l.index("old"))
     
    #Return True if the string is an alpha-numeric string, False otherwise.
    #string is alpha-numeric if all characters in the string are alpha-numeric and
    #there is at least one character in the string.
    print(y.isalnum())
    
    #Return True if the string is an alphabetic string, False otherwise.
    #A string is alphabetic if all characters in the string are alphabetic and there
    #is at least one character in the string.
    print(y.isalpha()) 
    
    
    
    #Return True if all characters in the string are ASCII, False otherwise.
    #ASCII characters have code points in the range U+0000-U+007F.
    #Empty string is ASCII too.
    print(y.isascii())
    
    
    #Return True if the string is a decimal string, False otherwise.
    #A string is a decimal string if all characters in the string are decimal and
    #there is at least one character in the string.
    print(y.isdecimal())
    
    #Return True if the string is a digit string, False otherwise.
    #A string is a digit string if all characters in the string are digits and there
    #is at least one character in the string.
    print(y.isdigit())
    
    #Return True if the string is a valid Python identifier, False otherwise.
    #Use keyword.iskeyword() to test for reserved identifiers such as "def" and
    #"class".
    print(y.isidentifier())
        
    
    #Return True if the string is a lowercase string, False otherwise.
    #A string is lowercase if all cased characters in the string are lowercase and
    #there is at least one cased character in the string.    
    print(y.islower())    
        
    
    #Return True if the string is a numeric string, False otherwise.
    #A string is numeric if all characters in the string are numeric and there is at
    #least one character in the string.
    print(y.isnumeric())
    
    #Return True if the string is printable, False otherwise.
    #A string is printable if all of its characters are considered printable in
    #repr() or if it is empty.
    print(y.isprintable()) 
     
    #Return True if the string is a whitespace string, False otherwise.
    #A string is whitespace if all characters in the string are whitespace and there
    #is at least one character in the string.
    print(y.isspace())    
        
    #Return True if the string is a title-cased string, False otherwise.
    #In a title-cased string, upper- and title-case characters may only
    #follow uncased characters and lowercase characters only cased ones.
    print(y.istitle())    
        
        
    #Return True if the string is an uppercase string, False otherwise.
    #A string is uppercase if all cased characters in the string are uppercase and
    #there is at least one cased character in the string.    
    print(y.isupper())
    
    
    #Concatenate any number of strings.
    #The string whose method is called is inserted in between each given string.
    #The result is returned as a new string.
    j='  Wipro Sarjapur  '
    print("#".join(j)) 
    
    #Return a left-justified string of length width.
    #Padding is done using the specified fill character (default is a space).
    print(j.ljust(20))
    
    #Return a copy of the string converted to lowercase.
    print(j.lower())
    
    #Return a copy of the string with leading whitespace removed.
    #If chars is given and not None, remove characters in chars instead.
    print(j.lstrip())
    
    #Partition the string into three parts using the given separator.
    #
    #This will search for the separator in the string.  If the separator is found,
    #returns a 3-tuple containing the part before the separator, the separator
    #itself, and the part after it.
    #
    #If the separator is not found, returns a 3-tuple containing the original string
    #and two empty strings.
    print(j.partition(" "))
      
    #replace(self, old, new, count=-1, /)
    #Return a copy with all occurrences of substring old replaced by new.
    #
    #  count
    #    Maximum number of occurrences to replace.
    #    -1 (the default value) means replace all occurrences.
    #
    #If the optional argument count is given, only the first count occurrences are
    #replaced.
    print(j.replace("a","b"))
        
        
    #rfind(...)
    #S.rfind(sub[, start[, end]]) -> int
    #
    #Return the highest index in S where substring sub is found,
    #such that sub is contained within S[start:end].  Optional
    #arguments start and end are interpreted as in slice notation.
    #
    #Return -1 on failure.
    print(j.rfind('Wipro'))
    
    
    #rindex(...)
    #S.rindex(sub[, start[, end]]) -> int
    #
    #Return the highest index in S where substring sub is found,
    #such that sub is contained within S[start:end].  Optional
    #arguments start and end are interpreted as in slice notation.
    #
    #Raises ValueError when the substring is not found.
    print(j.rindex('Wipro'))
    
    
    #rjust(self, width, fillchar=' ', /)
    #Return a right-justified string of length width.
    #
    #Padding is done using the specified fill character (default is a space).
    print(j.rjust(20))
    
    
    #rpartition(self, sep, /)
    #Partition the string into three parts using the given separator.
    #
    #This will search for the separator in the string, starting at the end. If
    #the separator is found, returns a 3-tuple containing the part before the
    #separator, the separator itself, and the part after it.
    #
    #If the separator is not found, returns a 3-tuple containing two empty strings
    #and the original string.
    #print(j.rpartinion("a"))
    
    
    
    #rsplit(self, /, sep=None, maxsplit=-1)
    #Return a list of the words in the string, using sep as the delimiter string.
    #
    #  sep
    #    The delimiter according which to split the string.
    #    None (the default value) means split according to any whitespace,
    #    and discard empty strings from the result.
    #  maxsplit
    #    Maximum number of splits to do.
    #    -1 (the default value) means no limit.
    #
    #Splits are done starting at the end of the string and working to the front.
    print(j.rsplit(' '))
    
    
    #rstrip(self, chars=None, /)
    #Return a copy of the string with trailing whitespace removed.
    #
    #If chars is given and not None, remove characters in chars instead.
    print(j.rstrip())
    
    #split(self, /, sep=None, maxsplit=-1)
    #Return a list of the words in the string, using sep as the delimiter string.
    #  sep
    #  The delimiter according which to split the string.
    #  None (the default value) means split according to any whitespace,
    #  and discard empty strings from the result.
    #  maxsplit
    #  Maximum number of splits to do.
    #  -1 (the default value) means no limit.
    print(j.split(' '))
    
    #splitlines(self, /, keepends=False)
    #Return a list of the lines in the string, breaking at line boundaries.
    #
    #Line breaks are not included in the resulting list unless keepends is given and
    #true.
    #print(j.splitlines(' '))
    
    
    #startswith(...)
    #S.startswith(prefix[, start[, end]]) -> bool
    #
    #Return True if S starts with the specified prefix, False otherwise.
    #With optional start, test S beginning at that position.
    #With optional end, stop comparing S at that position.
    #prefix can also be a tuple of strings to try.
    print(j.startswith('Sarjapur'))
    
    
    #strip(self, chars=None, /)
    #Return a copy of the string with leading and trailing whitespace remove.
    #
    #If chars is given and not None, remove characters in chars instead.
    print(j.strip())
    
    #swapcase(self, /)
    #Convert uppercase characters to lowercase and lowercase characters to uppercase.
    print(j.swapcase())
    
    #title(self, /)
    #Return a version of the string where each word is titlecased.
    #
    #More specifically, words start with uppercased characters and all remaining
    #cased characters have lower case.
    print(j.title())
    
    
    #translate(self, table, /)
    #    Replace each character in the string using the given translation table.
    #    
    #      table
    #        Translation table, which must be a mapping of Unicode ordinals to
    #        Unicode ordinals, strings, or None.
    #    
    #    The table must implement lookup/indexing via __getitem__, for instance a
    #    dictionary or list.  If this operation raises LookupError, the character is
    #    left untouched.  Characters mapped to None are deleted.
    #print(j.translate())
    
    #upper(self, /)
    #    Return a copy of the string converted to uppercase.
    print(j.upper())
    
    
    #zfill(self, width, /)
    #    Pad a numeric string with zeros on the left, to fill a field of the given width.
    #    
    #    The string is never truncated.
    #print(j.zfill())

#----------------------------------------------------------------------------------------------------------------------------
#listpackage
def ListPackage():
    import numpy
    x=numpy.arange(1,11)
    print(x)
    print(x[1:4])
    print(x*2)
    y=numpy.arange(12,22)
    print(y)
    print(x+y)

#----------------------------------------------------------------------------------------------------------------------------
#tuplepackage    
def tuplepackage():    
    b=(10,20,30,40,50) #taken from example shown in tutorial
    print(b)
    print(b[1:4])
    print(b*2)
    c=(11,22,33,44,55)
    print(b+c

#----------------------------------------------------------------------------------------------------------------------------
#dictpackage
def dictpackage():
    dict1={'hi':1,'bye':2,'hello':3}
    dict2={'ram':30,'vikash':24,'sahil':45}
    dict3={'gaya':'bihar','howrah':'kolkata'}
    
    if dict1.items()>dict2.items() and dict1.items()>dict3.items() :
        print("dict1 is bigger")
    elif dict2.items()>dict3.items() and dict2.items()>dict3.items():
        print("dict2 is bigger")
    else:
        print("dict3 is bigger")
        
    dict1['adding']=99999
    dict2['wipro']='added'
    print(dict1)
    print(dict2)
    
    
    print(str(dict1)+str(dict2)+str(dict3))
    
#---------------------------------------------------------------------------------------------------------------------------
#functionspackage

def functionpackage(n):
    first = 0
    second= 1
    third = 0
    while(n>third):
        print(first)
        total = first + second
        first = second
        second = total
        third += 1   
x=int(input('Enter the number of elemnt for fibonacci series: '))        
functionpackage(x)

def functionpackage1(list1,x):
    for i in list1: 
        if i in list1: 
            print('Element found')
            break
        else:
            print('Element not found')
            break
list2=[1,2,3,4,5,6,7,8,9,10]
print(list2)
print('-'*50)
z=int(input('Write a Number to find in the list: '))
functionpackage1(list2,z)

def functionpackage3():
    sumlambda = lambda x,y: x+y
    sublambda = lambda x,y: x-y
    mullambda = lambda x,y: x*y
    divlambda = lambda x,y: x/y
    modlambda = lambda x,y: x%y
    fldlambda = lambda x,y: x//y
    
    z=int(input('Enter 1st number: '))
    k=int(input('Enter 2nd number: '))
    print('Sum using lambda: '+str(sumlambda(z,k)))
    print('Sub using lambda: '+str(sublambda(z,k)))
    print('Mul using lambda: '+str(mullambda(z,k)))
    print('Div using lambda: '+str(divlambda(z,k)))
    print('Mod using lambda: '+str(modlambda(z,k)))
    print('Fld using lambda: '+str(fldlambda(z,k)))
    
def functionpackage4(x):
    if x == x[::-1]:
        print('Palindrome')
    else:
        print('Not Palindrome')

y=str(input('Enter the string to check palindrome: '))
functionpackage4(y)

def functionpackage5(a,b,c,d):
    if a>b and a>c and a>d:
        print(str(a)+' is biggest number')
    elif b>a and b>c and b>d:
        print(str(b)+' is biggest number')
    elif c>a and c>b and c>d:
        print(str(c)+' is biggest number')
    else:
        print(str(d)+' is biggest number')
        
e=int(input('enter 1st number: '))
f=int(input('enter 2nd number: '))
g=int(input('enter 3rd number: '))
h=int(input('enter 4th number: '))
functionpackage4(e,f,g,h)

def functionpackage5(tup1,list1):
    return tup1+tuple(list1)

tup=(1,2,3,4)
lis=[5,6,7,8]
functionpackage5(tup,lis)  

def functionpackage6()
    sumlambda = lambda x,y: x+y
    sublambda = lambda x,y: x-y
    mullambda = lambda x,y: x*y
    divlambda = lambda x,y: x/y
    modlambda = lambda x,y: x%y
    fldlambda = lambda x,y: x//y
    
    z=int(input('Enter 1st number: '))
    k=int(input('Enter 2nd number: '))
    print('Sum using lambda: '+str(sumlambda(z,k)))
    print('Sub using lambda: '+str(sublambda(z,k)))
    print('Mul using lambda: '+str(mullambda(z,k)))
    print('Div using lambda: '+str(divlambda(z,k)))
    print('Mod using lambda: '+str(modlambda(z,k)))
    print('Fld using lambda: '+str(fldlambda(z,k)))
    print('-'*50)
    import math
    
    sqrlambda = lambda x:math.sqrt(x)
    
    a=int(input('Enter number to get squrroot: '))
    print('-'*50)
    print('Square root is: '+str(sqrlambda(a)))
    
    String = "Pack: My: Box: With: Good: Food"
    def sublist(string,k):
        return string.split(k)
    print('-'*50)
    print(sublist(String, ": "))
    
    
#------------------------------------------------------------------------------------------------------------------------------
#filepackage

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


# In[ ]:




