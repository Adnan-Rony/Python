thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
# print(thisdict)

# x=thisdict.items()
# print(x)

# thisdict.update({"model":"adnan"})
# print("update ",thisdict)

# thisdict.pop("brand")
# print(thisdict)

# del thisdict["model"]
# print(thisdict)

# def neww(k,v):
#     new=dict(zip(k,v))
#     return new
# k=[1,2,3,4]
# v=[2,4,6,8]
# result=neww(k,v)
# print(result)
listt=[]
for i in thisdict.values():
    listt.append(i)
print(listt)    