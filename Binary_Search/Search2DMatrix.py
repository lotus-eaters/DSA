#Brute Force

def Search2DMatrixBrtueForce(a,m,n,k):
	for i in range(m):
		for j in range(n):
			if a[i][j]==k:
				return True
	return False

#Better solution is to perform binary search regarding every row as an indivual array

#Individual rows and colums are sorted, not entire matrix
def Search2DMatrixII(a,m,n,k):
	row=0
	col=n-1
	while row<=m and col>=0:
		if a[row][col]==k:
			return True
		elif a[row][col]>k:
			col-=1
		else:
			row+=1
	return False
#entire matrix is sorted flatten it out to 1D array
def Search2DMatrixI(a,m,n,k):
	low = 0
	high=m*n-1
	while low<=high:
		mid = (low+high)//2
		row=mid//m
		col=mid%m
		if a[row][col]==k:
			return True
		elif a[row][col]<k:
			low=mid+1
		else:
			high=mid-1
	return False
a=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(Search2DMatrixBetter(a,len(a),len(a[0]),3))
print(Search2DMatrixOptimal(a,len(a),len(a[0]),3))
print(Search2DMatrixBrtueForce(a,len(a),len(a[0]),3))

