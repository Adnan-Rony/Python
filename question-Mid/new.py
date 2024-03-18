def new(d):
    newlist=d.copy()
    newlist.reverse()
    Numbersorted=sorted(newlist)
    return newlist,Numbersorted


d=[1,12,5,3,66,12,23]
reverse,sorted=new(d)
print('reverse',reverse)
print('sorted',sorted)


input_string = "You are from Daffodil International University. You are currently studying 5th semester."
outputSting=input_string.replace("5th","7th")
print(outputSting)

def even(num):
    return num % 2 == 0

def odd(num):
    return num % 2 != 0

def list_numbers(L):
    even_nums = []
    odd_nums = []
    for i in L:
        if even(i):
            even_nums.append(i)
        else:
            odd_nums.append(i)
    print("The list of odd numbers are :", odd_nums)
    print("The list of even numbers are :", even_nums)

L = [12, 15, 33, 7, 1, 92, 53, 4, 0]
print("The list is ")
print(L)
list_numbers(L)

def evenOdd(num):
    even=[]
    odd=[]
    for e in num:
        if e%2==0:
            even.append(e)
        else:
            odd.append(e)
    return even,odd
num=[12, 15, 33, 7, 1, 92, 53, 4, 0]
even,odd=evenOdd(num)
print("even ",even)
print("odd ",odd)
        
    
    
    

    