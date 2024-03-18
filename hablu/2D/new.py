# stack=[]
# stack.append(1)
# stack.pop(0)
# print(stack)
# print(type(stack))

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

newlist=[x for x in fruits if "c" in x]
print(newlist)



new=[x for x in range(1,10) if  x>5]
print(new)        