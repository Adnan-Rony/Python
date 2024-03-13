thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

print('no sorting ',thislist)



thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist) 




thislist = [100, 50, 65, 82, 23]

print('no sorting ',thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print('number sort',thislist)

thislist = [100, 50, 65, 82, 23]
thislist.reverse()
print('number reverse',thislist)




thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
    
    
thislist = ["banana", "Orange", "KiWi", "cherry"]
thislist.sort(key = str.lower)
print('key',thislist)
   
    
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)