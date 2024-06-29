'''Represent 2D matrix of dimensions M x N, by taking M, N and matrix elements as input from the
user. Perform following operations on these 2D matrices.
2. Multiply 2 matrices. Note that the input matrices need to be checked for compatible 
multiplication, i.e., 2 matrices with M x N and N x P dimensions can be multiplied, if number 
of columns in 1st matrix is equal to the number of rows in the 2nd matrix. Consider all the 
valid and invalid test cases and display the results.'''

n_rows1, n_cols1 = map(int, input().split())
rows1 = []
for i in range(n_rows1):
    cols1 =[]
    for j in range(n_cols1):
        values = int(input("Enter the value of first matrice= "))
        cols1.append(values)
    rows1.append(cols1)


n_rows2, n_cols2 = map(int, input().split())
rows2 = []
for i in range(n_rows2):
    cols2 =[]
    for j in range(n_cols2):
        values = int(input("Enter the value of second matrice = "))
        cols2.append(values)
    rows2.append(cols2)

print(rows1)
print(rows2)
'''
if n_cols1==n_rows2:
    print("It is compatible of mutiplication. ")
else:
    print("It is not compatible of mutiplication. ")'''

res_rows = []
for i in range(n_rows1):
    res_cols = []
    for j in range(n_cols2):
        for k in range(n_cols1):
            res = rows1[i][k]*rows2[k][j]
            res_rows.append(res)
print(res_rows)