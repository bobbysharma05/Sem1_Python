'''Take a list of integers as input and sort the elements of the list in-place, i.e., do not use any 
other list for storing the result, only the values in the list are swapped to form the sorted list. 
(Do not use the inbuilt sorting function). '''


list_1 = list(map(int, input().split()))

j=0
for j in range(len(list_1)):
    i=0
    while i<(len(list_1)-1-j):
        if list_1[i]>list_1[i+1]:
            temp = list_1[i]
            list_1[i] = list_1[i+1]
            list_1[i+1] = temp
        i+=1
    j+=1
    print(list_1)
    