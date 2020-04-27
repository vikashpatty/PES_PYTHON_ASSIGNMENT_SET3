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
            print(',',c)
            a=b
            b=c