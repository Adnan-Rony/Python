
thislist=[1,2,3,4]
sum=0
for i in thislist:
    
    sum =sum+i
print(sum) 


def sumList(items):
    sum=0
    for x in items:
        sum=sum+x
    return sum
result=sumList([1,2,3,4,5])
print(result)