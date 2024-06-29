error = float(input("Enter the error : "))
if error<0:
    print("Invalid Input") 
i=2
count_=0
while True:
    Func = (1/2)**i
    Sunc = (1/2)**(i-1)
    i+=1
    count_+=1
    if abs(Func - Sunc) < error:
        print("Invalid Input")
        break
print(count_)
print("The sum of this series is ",Func)
 
         