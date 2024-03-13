thislist=[1,2,3,4]

maax=thislist[0]

for a in thislist:
   if a>maax:
       maax=a
        

print(maax)


def largestNumber(list):
    max=list[0]
    for x in list:
        if x>max:
            max=x
    return max

result=largestNumber([1,2,3,4,5]) 
print(result)       