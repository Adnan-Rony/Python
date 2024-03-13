def count_even_odd(tup):
    event_count=0
    odd_count=0
    for x in tup:
        if x %2==0:
            event_count +=1
        else:
            odd_count +=1
    return event_count,odd_count

tup= (1, 2, 3, 4, 5, 6, 7, 8, 9) 

even,odd=count_even_odd(tup)

print('event:  ',even)
print('odd : ',odd)