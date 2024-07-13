
print("Multiplication Table")
try:
    a = int(input("Enter Num: "))
    for i in range(10):
         print(str(a) +" * " + str(i+1) + " = " + str(a*(i+1)))
except:
    print("error Occured ")
    