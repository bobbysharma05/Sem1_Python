'''Take a paragraph as input and find the count of digits, alphabets, and special characters present 
in the paragraph. For alphabets, also check how many of them are upper case and how many 
are lower case alphabets. Use inbuilt string functions to check. '''

para = str(input())
A = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
B = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U",'V','W',"X","Y","Z"]
count_digits = 0
alphabets = 0
special_chr = 0
space_dig = 0
for i in para:
    if i in A or i in B:
        alphabets+=1
    elif i == " ":
        space_dig+=1
    else:
        special_chr+=1
    count_digits+=1
print("Count = ",count_digits)
print("Alphabets = ",alphabets)
print("Special Chr = ",special_chr)
print("Spaces = ",space_dig)