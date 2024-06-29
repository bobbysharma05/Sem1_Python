n = int(input("Enter the number of lines = "))

h = 1
while h<=n:
    i=n-1
    while i>=h:
        print(" ", end="" )
        i-=1
    j = 1
    while j<=h:
        print("*", end= " ")
        j+=1
    h+=1
    print()
