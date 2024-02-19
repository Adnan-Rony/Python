#python byte array total range is 0-256
#not extra space of any line

#its immutable
number=[1,2,3,4,5,255]


b = bytes(number)  #list to bytes convert(its not changeable)
 
print(type(b)) 




#Binary types data byteArray

numberlist=[1,2,3,4,5,6,10]

b1=bytearray(numberlist )  #list to bytesArray convert(its changeable)

b1[1]=50

print(type(b1))

print(b1[1])



