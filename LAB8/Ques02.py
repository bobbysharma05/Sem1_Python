'''Take a list of integers as input and sort the elements of the list by taking another list and 
incrementally appending values in the 2nd list. (Do not use the inbuilt sorting function)'''
aq = list(map(int, input().split()))
aq2 = []
num=len(aq)

for i in range(num):
    aq2.append(min(aq))
    aq.remove(min(aq))
    
print(aq2)
    
  