def Factorial(n):
    fact=1
    i=1
    while i<=n:
        fact=fact*i
        i+=1
    return fact

inp = int(input())
if inp==0:
    print("Invalid Input")
elif inp<0:
    print("0")
else:
    print(Factorial(inp))