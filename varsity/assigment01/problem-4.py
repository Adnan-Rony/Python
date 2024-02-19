x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
z=int(input("Enter the value of z: "))
sum=x+y+z
if sum==180:
    if x==y==z:
        print("Equilateral Triangle")
    elif x==y or x==z or y==z:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")

else:
    print("Not a valid triangle")