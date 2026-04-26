def SumofFirstNumbers(n):
	if n==1:
		return 1
	return n+SumofFirstNumbers(n-1)

print(SumofFirstNumbers(5))
