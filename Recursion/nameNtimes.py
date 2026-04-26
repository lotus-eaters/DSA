def nameNtimes(name,n):
	if n==0:
		return 
	print(name)
	nameNtimes(name,n-1)

nameNtimes('name',5)