def print1N(n,rev):
	if n==0:
		return
	if rev:
		print1N(n-1,True)
		print(n)
	else:
		print(n)
		print1N(n-1,False)

print1N(5,rev=True)
print1N(5,rev=False)