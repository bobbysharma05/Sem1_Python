'''Represent 2D matrix of dimensions M x N, by taking M, N and matrix elements as input from the
user. Perform following operations on these 2D matrices.
1. Add 2 matrices. Display the values in the input matrices as well as the summation matrix.
'''

n_rows, n_cols = map(int, input().split())
rows1 = []
for i in range(n_rows):
    cols1 =[]
    for j in range(n_cols):
        values = int(input("Enter the value of first matrice= "))
        cols1.append(values)
    rows1.append(cols1)

rows2 = []
for i in range(n_rows):
    cols2 =[]
    for j in range(n_cols):
        values = int(input("Enter the value of second matrice = "))
        cols2.append(values)
    rows2.append(cols2)

rows_result = []
for i in range(n_rows):
    cols_result =[]
    for j in range(n_cols):
        sum = rows1[i][j]+ rows2[i][j]
        cols_result.append(sum)
    rows_result.append(cols_result)

print(rows_result)
        
        