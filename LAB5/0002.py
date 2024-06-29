n = int(input("Enter the number ="))
i=1

while i>=1 and i<1000:
    i+=1
    if (i%n) != 0:
       print(i)
        
    elif (i%n) == 0:
        continue
