# Matrix Multiplication
A = [[6, 9],
    [6, 7]]

B = [[3, 6],
    [3, 42]]

result = [[0, 0],
         [0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("Product of matrices:")
for row in result:
    print(row)