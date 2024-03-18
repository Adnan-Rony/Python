# #spring-2022-1-B
list1=[1,2,3,5]
list2=[2,4,5,3]

common_elements = set(list1) and set(list2)
if common_elements:
    print("Common elements:", list(common_elements))
else:
    print("No common elements")
    
list1 = [1, 2, 3]
list2 = [2, 4, 5]

# Initialize an empty list to store common elements
common_elements = []

for li1 in list1:
    if li1 in list2:
        common_elements.append(li1)
if len(common_elements)>0:
    print("common elements :",common_elements)
else:
    print("no comment elements")                