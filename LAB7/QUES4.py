''' Take a string as input and check if it is palindrome or not. Do not use any inbuilt functions except
len().'''

inp1 = str(input("Enter the  string: "))
inp = inp1.lower()
count_itis = 0
count_itisnot = 0
for i in range(len(inp)//2):
    if inp[i] == inp[len(inp)-i-1]:
        count_itis+=1
    else:
        count_itisnot+=1

if count_itisnot>0:
    print("it is not pallindrome")
else:
    print("It is ") 