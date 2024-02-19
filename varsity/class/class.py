num=int(input("enter the number "))

if (num>=100) and (num <=200):
    if num%2==0:
        print("event ",num*num)
    elif num%2!=0:
        print("odd ",num*num*num)
else:
    print("anything is wrong")            