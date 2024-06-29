def myadd(a,b):
    return a+b
def mydifference(a,b):
    return a-b
def mymutiply(a,b):
    return a*b
def mydividion(a,b):
    return a/b
def myremainder(a,b):
    return a%b
def myexponential(a,b):
    return a**b

print("Coose the Operation:")
print("1. Addition.")
print("2. Subtraction.")
print("3. Multiplication.")
print("4. Division.")
print("5. Modulus")
print("6. Exponentiation.")
print("7. Exit")
  
v = int(input())
  
while v<7 and v>=1:
    fst_operand = int(input("Enter the the first operand : "))
    second_operand = int(input("Enter the the second operand : "))
    if v==1:
        print(myadd(fst_operand,second_operand))
    elif v==2:
        print(mydifference(fst_operand,second_operand))
    elif v==3:
        print(mymutiply(fst_operand,second_operand))
    elif v==4:
        print(mydividion(fst_operand,second_operand))
    elif v==5:
        print(myremainder(fst_operand,second_operand))
    elif v==6:
        print(myexponential(fst_operand,second_operand))
    print("Coose the Operation:")
    print("1. Addition.")
    print("2. Subtraction.")
    print("3. Multiplication.")
    print("4. Division.")
    print("5. Modulus")
    print("6. Exponentiation.")
    print("7. Exit")
    v = int(input())
else:
    print("You have exited from the calculator, Goodbye")
   
  