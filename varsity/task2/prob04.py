str=input("enter the string ")
uppor=0
lower=0
for i in str:
    if i.islower():
        lower+=1
    else:
        uppor+=1
print("lower case",lower)
print("upper ",uppor)        