'''Take a list of positive integers as input in a list and perform the following operations:
1. Remove duplicate elements. Do not use sets or any other in-built functions except len().
2. Remove duplicate elements by typecasting into sets and displaying resulting elements in the
same order as they appear in the input list. '''

list_1 = list(input("Input the list = "))
list_2 = []
for i in list_1:
    if i not in list_2:
        list_2.append(i)
print(list_2)


my_list = list(map(int, input().split()))
new_my_list = []
duplicate_ones = set()
for i in my_list:
    if i not in new_my_list:
        new_my_list.append(i)
    else:
        duplicate_ones.add(i)
print(new_my_list)
print(duplicate_ones)
