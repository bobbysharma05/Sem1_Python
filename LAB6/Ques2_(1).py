terms = int(input("Enter the number of terms = "))
sum=0
for i in range(1,terms+1):
    sum+=(1/i)
print("Sum till", terms, "terms are :",sum)
