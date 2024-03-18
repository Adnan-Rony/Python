# def myfunc(a, b):
#   return a + b

# x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

# print(x)
# print(list(x))

def square(x):
    return x*x
num=[1,2,3,4]

result=list(map(square,num))
print(result)