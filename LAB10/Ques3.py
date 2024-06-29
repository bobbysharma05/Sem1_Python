#n =input("Enter the number = ")
n = None
Odd={}
Even = {}

while True:
    n = input("Enter the number (else 'over' to exit) : ")
    if n == 'over':
        break
    n = int(n)
    if n%2 == 0:
        Even[n] = [n**2, n**3]
    else:
        Odd[n] = [n**2, n**3]

#while str(n).lower()=="over":
#    print("You are out")
#    break
#else:
#    if int(n)%2==0:
#        Even[int(n)] = [int(n)**2, int(n)**3]
#    elif int(n)%2==1:
#        Odd[int(n)] = [int(n)**2, int(n)**3]
#    inp = int(input("Enter the number = "))
#    while str(inp).lower()=="over":
#        print("You are out")
#    else:    
#        if inp%2==0:
#            Even[inp] = [inp**2,inp**3]
#        else:
#            Odd[inp] = [inp**2, inp**3]
print(Odd)
print(Even)
