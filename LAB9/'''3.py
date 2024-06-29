'''3. Represent 2D square matrix of dimensions N x N, by taking N and matrix elements as input from 
the user. Perform following operations on these 2D matrices. 
1. Check if the matrix is a symmetric matrix or not.
2. Find the sum of the two diagonal elements. Principle diagonal and non-principle diagonal.
3. Check if the matrix is an upper triangular matrix or a lower triangular matrix.
4. Find the transpose of the matrix'''

n = int(input())
lst = []
for i in range(n):
    row = []
    for j in range(n):
        ele = int(input())
        row.append(ele)
    lst.append(row)
print(lst)

if lst[0][1]==lst[1][0]  and lst[0][2]==lst[2][0]  and lst[1][2]==lst[2][1]:
   print("This is symmetric matrix") 
else:
    print("This is non symmetric matrix") 
   
sum1 = lst[0][0] + lst[1][1] + lst[2][2]
sum2 = lst[0][2] + lst[1][1] + lst[2][0]
print("Sum of diagnol elements",sum1)
print("Sum of non - diagnol elements",sum2)
print("Find the sum of the two diagonal elements. Principle diagonal and non-principle diagonal.",sum1+sum2)


if lst[1][0]==0  and lst[2][0]==0  and lst[2][1]==0:
   print("This is Uper triangular matrix") 
else:
    print("This is lower triangular matrix")

