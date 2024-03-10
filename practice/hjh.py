def name(x):
    even=0
    odd=0
    for i in x:
        if(i%2==0):
            even +=1
        else:
            odd +=1    
    return even,odd
x=(1,2,3,4,5,6,8)
even,odd=name(x)
print('event:  ',even)
print('odd : ',odd)



        
    

