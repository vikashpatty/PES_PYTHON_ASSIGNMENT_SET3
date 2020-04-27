import stringop

n=[23,24,67,1,0,21]
stringpop.SortList(n)

s=input("Enter element to search:")
res=stringpop.binarySearch(n,0,7,s)
if res==-1:
    print('Not found')
else:
    print('found')


z=str(input("Enter string to reverse"))
stringpop.ReverseString(z)