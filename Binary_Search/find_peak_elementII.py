# def findMaxEle(a,n,col):
# 	max_row=0
# 	index=-1
# 	for i in range(n):
# 		if a[i][col]>a[max_row][col]:
# 			max_row=i
# 	return max_row


# def findPeakElement(a):
# 	n=len(a)
# 	m=len(a[0])
# 	low=0
# 	high=m-1 #no of cols-1
# 	while low<=high:
# 		mid=(low+high)//2
# 		row=findMaxEle(a,n,mid)
# 		left = a[row][mid-1] if mid-1>=0 else float('-inf')
# 		right = a[row][mid+1] if mid+1<m else float('-inf')
# 		if a[row][mid]>=left and a[row][mid]>=right:
# 			return [row,mid]
# 		elif left>a[row][mid]:
# 			high=mid-1
# 		else:
# 			low=mid+1
# 	return [-1,-1]

# mat = [
#   [4, 2, 5, 1, 4, 5],
#   [2, 9, 3, 2, 3, 2],
#   [1, 7, 6, 0, 1, 3],
#   [3, 6, 2, 3, 7, 2]
# ]

# print(findPeakElement(mat))

def findMaxEle(a, row):
    max_col = 0
    for j in range(1, len(a[0])):
        if a[row][j] > a[row][max_col]:
            max_col = j
    return max_col


def findPeakElement(a):
    n = len(a)
    m = len(a[0])
    low, high = 0, n - 1

    while low < high:
        mid = (low + high) // 2
        col = findMaxEle(a, mid)

        if a[mid][col] > a[mid + 1][col]:
            high = mid
        else:
            low = mid + 1

    col = findMaxEle(a, low)
    return [low, col]

mat = [
  [4, 2, 5, 1, 4, 5],
  [2, 9, 3, 2, 3, 2],
  [1, 7, 6, 0, 1, 3],
  [3, 6, 2, 3, 7, 2]
]

print(findPeakElement(mat))


