matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

flatten=[matrix [i][j] for i in range(len(matrix)) for j in range(len(matrix[i]))]

print(flatten)