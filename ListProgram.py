def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(doe,bi):
    return doe*bi
def divide(s,v):
    return s/v
def exponent(s,v):
    return s**v
a=int(input("Enter a "))
b=int(input("Enter b "))
opmethod=input("Enter operation. ")
if opmethod=="multiply":
    print(multiply(a,b))
elif opmethod=="divide":
    print(divide(a,b))
elif opmethod=="add":
    print(add(a,b))
elif opmethod=="subtract":
    print(minus(a,b))
else:
    print(opmethod + " is an invalid operator. Goodbye. Boom!")
    exit(0)


print("steve")
x=True
if x:
    print("hello")
else:
    print("good-bye")
a=.065
b=89.0
b=b+(b*a)
print("$"+str(b))

colors=["yellow","purple","pink","blue"]
availablecolors=", ".join(colors)
usercolor = input("What's your favorite color? Available colors are " + availablecolors + ".")

if usercolor not in colors:
    print(usercolor + " is not a color. I'm outta here")
    exit(0)
userage = input("What's your age?")
if int(userage) < 18:
    print("You are " + userage + " years old. Go away youngling!")
    exit(0)
#answer1=in 
#in=input("How old are you?")
