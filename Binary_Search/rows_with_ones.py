#Brute force solution
def find_max_ones_in_a_row(a,m,n):
	max_count=0
	index=-1
	for i in range(m):
		count_ones=0
		for j in range(n):
			count_ones+=a[i][j]
		if count_ones>max_count:
			max_count=count_ones
			index=i
	return index

a=[[0,0,1,1,1],[0,0,0,0,0],[0,1,1,1,1],[0,0,0,0,0],[0,1,1,1,1]]
m=len(a)
n=len(a[0])
print(find_max_ones_in_a_row(a,m,n))

#Optimal Solution Binary Search
def findFirstOcurence(a,m,k):
	low=0
	high=m-1
	ans=-1
	while low<=high:
		mid=(low+high)//2
		if a[mid]==k:
			ans=mid
			high=mid-1
		elif a[mid]>k:
			high=mid-1
		else:
			low=mid+1
	return ans

def lowerBound(a,m,k):
	low=0
	high=m-1
	ans=high
	while low<=high:
		mid=(low+high)//2
		if a[mid]>=k:
			ans=mid
			high=mid-1
		else:
			low=mid+1
	return ans

def BinsearchmaxOnes(a,m,n):
	max_count=0
	index=-1

	for i in range(m):
		count_ones=0
		# count_ones=n-findFirstOcurence(a[i],m,1)
		count_ones=n-lowerBound(a[i],m,1)
		if count_ones>max_count:
			max_count=count_ones
			index=i
	return index

print(BinsearchmaxOnes(a, m, n))
