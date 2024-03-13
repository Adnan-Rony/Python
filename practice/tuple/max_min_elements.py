
my_tuple = (3, 7, 1, 9, 2, 5)

# Find the maximum element
max_element = max(my_tuple)

# Find the minimum element
min_element = min(my_tuple)

print("Maximum element:", max_element)
print("Minimum element:", min_element)




# another...........

def max_min_element(tup):
    return max(tup),min(tup)
tup = (5, 8, 2, 10, 3)
max,min=max_min_element(tup)

print('maximum',max)
print('minimum',min)
