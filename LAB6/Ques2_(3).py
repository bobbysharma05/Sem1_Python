terms = int(input("Enter the number of terms = "))
x= float(input("Enter the value of x"))
sum=1
for i in range(1,terms):
    sum+=((x**i)/i)
print("Sum till", terms, "terms are :",sum)
