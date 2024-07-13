print("simple Calculator")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    try:
        return a/b
    except:
        print("err")


def values():
    try:
        x=int(input("Enter first value: "))
        y=int(input("Enter second value: "))
        return x,y
    except:
        print("not a valid number")
    
print("1.Add\n2.Substitution\n3.Multiplicatin\n4.Division")

A=input("Choose One Option: ")
if(A=="1"):
    print("Addition")
    v=values()
    print(add(v[0],v[1]))
elif(A=="2"):
    print("Substitution")
    v=values()
    print(sub(v[0],v[1]))
elif(A=="3"):
    print("Multiplication")
    v=values()
    print(multi(v[0],v[1]))
elif(A=="4"):
    print("Division")
    v=values()
    print(divide(v[0],v[1]))    
else:
    print("not valide")

        
    
    
    
    
