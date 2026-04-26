def find_peak_element_brute(a):
	n=len(a)
	max_ele=0
	maxi=0
	for i in range(n):
		if a[i]>max_ele:
			max_ele=a[i]
			index=i
	return i

def find_peak_element_optimal(a):
	n=len(a)
	low=0
	high=n
	while low<high:
		mid=(low+high)//2
		if a[mid]>a[mid+1]:
			high=mid
		else:
			low=mid+1
	return low

a=[1,2,1,3,5,6,4]
print(find_peak_element_brute(a))
print(find_peak_element_optimal(a))
