''' Find the count of vowels and consonants, words in a string using a loop.
 Assume there is a single space between consecutive words in a sentence.'''

statment = str(input("Enter the Statment = "))
vowels = ('aeiou')
space=0
vow_ = 0
cons = 0
for i in statment:
    if i in vowels:
        vow_+=1
    elif i==" ":
        space+=1
    else:
        cons+=1
print("Vowels are : ",vow_)
print("Consonants are : ",cons)
print("Space between them : ",space)
