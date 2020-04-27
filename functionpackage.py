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