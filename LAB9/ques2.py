list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# #part1
set1 = set(list1)
set2 = set(list2)

#part2
a = set1 | set2
b = set1 & set2 
c = set1 - set2
d = set1 ^ set2
print(a)
print(b) 
print(c)
print(d)

#part3
new_list1 = []
for i in list1:
    if i not in new_list1:
        new_list1.append(i)

new_list2 = []
for i in list2:
    if i not in new_list2:
        new_list2.append(i)

print(new_list1)
print(new_list2)

intersection_list = []
for i in new_list1:
    if i in new_list2:
        intersection_list.append(i)

print(set(intersection_list))

#part4
n_list1 = []
for i in list1:
    if i not in n_list1:
        n_list1.append(i)

n_list2 = []
for i in list2:
    if i not in n_list2:
        n_list2.append(i)

print(n_list1)
print(n_list2)

union_list = list1+list2
print(set(union_list))