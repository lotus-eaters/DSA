def first_occurence(a,k):
	low=0
	high=len(a)-1
	ans=-1
	while low<=high:
		mid=(low+high)//2
		if a[mid]==k:
			ans=mid
			high=mid-1
		elif a[mid]<k:
			low=mid+1
		else:
			high=mid-1
	return ans


def lowerBound(a,k):
	low=0
	high=len(a)-1
	ans=-1
	while low<=high:
		mid=(low+high)//2
		if a[mid]>=k:
			ans=mid
			high=mid-1
		else:
			low=mid+1
	return ans
a=[1,2,3,4,5,5,6,7,8,8,8,9,0]
k=8
print(first_occurence(a,k))
print(lowerBound(a,k))
