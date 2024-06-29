'''Find the length of an input string without using the inbuilt len() function'''
string = str(input("enter the statement = "))
count=0
for i in string:
    count+=1
print("Count is ",count)