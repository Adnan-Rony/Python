def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def functionn(*kid):
    print("the youngest child is ",kid[1])
functionn('adnan','rony','adnansami','adnanrony')


def my_function(num1,num2,num3):
    print("most powerfull languages is : ",num2)
my_function(num2="python",num1="c++",num3="java")        



def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")