# k=[1001,1002,1003,1004]
# v=["USA","CANADA","CHINA","DOTTOPARA","UK"]

# keyvalue=zip(k,v)

# dictconvert=dict(keyvalue)
# print('list to dist',dictconvert)

# spring 2023-03-B
def listToDist(k,v):
    keyvalue=zip(k,v)
    dictconvert=dict(keyvalue)
    return dictconvert
k=[1001,1002,1003,1004]
v=["USA","CANADA","CHINA","DOTTOPARA","UK"]
result=listToDist(k,v)
print(result)

