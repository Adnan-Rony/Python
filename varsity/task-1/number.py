h=int(input('enter the hight'))
w=int(input('enter the width'))
l=int(input('enter the lenth'))

volume=h*w*l

if  volume>=50 and volume<=500:
    print('small')
elif volume>=501 and volume<=1500:
    print('medium')
elif volume>=1501:
    print('large')
else:
    print('another else')    