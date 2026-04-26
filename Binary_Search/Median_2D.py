import bisect

def findlessEqualTo(row,mid):
	return bisect.bisect_right(row,mid)

def findMedian(mat):
	rows=len(mat)
	cols=len(mat[0])
	low = min(row[0] for row in matrix)
	high= max(row[-1] for row in matrix)
	reqd=(rows*cols+1)//2
	while low<high:
		mid=(low+high)//2
		count=0
		for row in matrix:
			count+=findlessEqualTo(row,mid)
		if count<reqd:
			low=mid+1
		else:
			high=mid
	return low

matrix = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
print(findMedian(matrix))

