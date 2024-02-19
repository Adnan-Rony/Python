number=int(input('enter the int  number :'))

if number%3==0 and number%5==0:
    print('i got the number')
elif number%5==0 and number%7==0:
    print('nice number')
else:
    print('try another')            