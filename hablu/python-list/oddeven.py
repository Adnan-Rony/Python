num=int(input("enter the number "))
if num in range(1,100):
    if num%2==0:
        print("even ",num*num)
    elif num%2!=0:
        print('odd ',num*num*num)    
else:
    print("something is wrong")    