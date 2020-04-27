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