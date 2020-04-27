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