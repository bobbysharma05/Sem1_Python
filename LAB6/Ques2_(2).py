terms = int(input("Enter the number of terms = "))
sum=0
fact=1
for j in range(1,terms+1):
    fact*=j
    sum+=(1/fact)
print("Sum till", terms, "terms are :",sum)

            