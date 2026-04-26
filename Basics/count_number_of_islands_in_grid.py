def dfs(i,j,rows,cols,visited):
    if i<0 or i>=rows or j<0 or j>=cols:
        return
    if grid[i][j]==0 or visited[i][j]:
        return
    visited[i][j]=True
    dfs(i+1,j,rows,cols,visited)
    dfs(i-1,j,rows,cols,visited)
    dfs(i,j+1,rows,cols,visited)
    dfs(i,j-1,rows,cols,visited)

def count_islands(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False]* cols for _ in range(rows)]
    count=0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]!=0 and not visited[i][j]:
                dfs(i,j,rows,cols,visited)
                count+=1
    return count

grid = [
  [1, 1, 0, 0],
  [1, 0, 0, 1],
  [0, 0, 1, 1],
  [0, 0, 0, 0]
]
print(count_islands(grid))