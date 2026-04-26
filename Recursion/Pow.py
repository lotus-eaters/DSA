def pow(a,b):
	if b==0:
		return 1
	return pow(a,b-1)*a
print(pow(2,5))

def halfpow(a,b):
	if a==0:
		return 0
	if b==0:
		return 1
	hp=halfpow(a,b//2)
	if b%2==0:
		return hp*hp
	else:
		return hp*hp*a

def calcPow(x,n):
	ans = halfpow(x,abs(n))
	if n>0:
		return ans
	return 1/ans

print(halfpow(2,5))
print(calcPow(2,-5))
