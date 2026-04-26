def revArray(a):
	left=0
	right=len(a)-1
	while left<right:
		a[left],a[right]=a[right],a[left]
		left+=1
		right-=1
	print(a)

a=[2,4,6,8]
revArray(a)
