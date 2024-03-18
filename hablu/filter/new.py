num=[1,2,3,4,5,6]
def is_even(x):
    return x%2==0

result=list(filter(is_even,num))
print(result) 