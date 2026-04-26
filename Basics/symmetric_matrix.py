# a symmetric matrix is one which is equal to transpose of matrix
def is_symmetric(mat):
    n=len(mat)
    for i in range(n):
        for j in range(n):
            if mat[i][j]==mat[j][i]:
                return True
    return False

matrix = [
  [1, 2, 3],
  [2, 4, 5],
  [3, 5, 6]
]
print(is_symmetric(matrix))

