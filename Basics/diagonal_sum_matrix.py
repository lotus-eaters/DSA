def diagonal_sum(mat):
    n=len(mat)
    total=0
    for i in range(n):
        total+=mat[i][i] #top left to bottom right
        total+=mat[i][n-1-i] #top right to bottom left
    if n%2!=0:
        total-=mat[n//2][n//2]  # Subtract center if counted twice (for odd-sized matrices)
    return total

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonal_sum(matrix))


# import numpy as np

# m = np.array(matrix)

# primary   = np.trace(m)                  # sum of main diagonal
# secondary = np.trace(np.fliplr(m))       # flip matrix, then trace
# total     = primary + secondary

# if len(m) % 2 != 0:
#     total -= m[len(m)//2][len(m)//2]    # remove double-counted center