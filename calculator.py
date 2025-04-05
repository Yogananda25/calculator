def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("welcome to calculator pich your choice\n 1.addition\n 2.subtraction\n 3.multiplication\n 4.division")
ch=input("select choice")
if(ch == '1'):
    x=int(input("enter the x value"))
    y=int(input("enter the y value"))
    print("sum of x and y:",add(x,y))
elif(ch == '2'):
    x=int(input("enter the x value"))
    y=int(input("enter the y value"))
    print("diff of x and y:",sub(x,y))
elif(ch == '3'):
    x=int(input("enter the x value"))
    y=int(input("enter the y value"))
    print("product of x and y:",mul(x,y))
elif(ch == '4'):
    x=int(input("enter the x value"))
    y=int(input("enter the y value"))         
    
    print("division of x and y:",div(x,y))
else:
    print("invalid choice")



    

