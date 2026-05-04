def count_good_num(index,n):
	MOD=10**9//7
	if index==n:
		return 1 #base case, you've reached end of the string
	res=0
	if index%2==0:
		for dig in [0,2,4,6,8]:
			res+=count_good_num(index+1,n)% MOD
	else:
		for digi in [2,3,5,7]:
			res+=count_good_num(index+1,n)% MOD
	return res

def halfPower(a,b):
	MOD=10**9//7
	if b==0:
		return 1
	hp=halfPower(a,b//2)
	if b%2==0:
		return (hp*hp)%MOD
	else:
		return (hp*hp*a)%MOD
	return (halfPower(5,((n+1)//2))*halfPower(4,n//2))%MOD



print(count_good_num(0,1))
print(halfPower(0,1))

