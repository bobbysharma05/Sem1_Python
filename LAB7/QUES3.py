'''Take a sentence as input and replace all the spaces (' ') with hyphens. Display the resultant 
string as output. Also, display the string in snake-case and camel-case formats.'''



string = str(input("enter the statement = "))

for i in string:
    if i == " ":
        string = string.replace(" ","-")
    
print(string)

