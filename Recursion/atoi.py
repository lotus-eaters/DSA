INT_MIN=-2**31
INT_MAX=2**31-1
def helper(s,i,num,sign):
	if i>=len(s) or not s[i].isdigit():
		return num*sign

	num=num*10+int(s[i])

	if num*sign >= INT_MAX: return INT_MAX
	if num*sign <= INT_MIN: return INT_MIN

	return helper(s,i+1,num,sign)

def atoi(s):
	i=0
	while i<len(s) and s[i]==' ':
		i+=1
	sign =1
	if i<len(s) and(s[i]=='-' or s[i]=='+'):
		sign=-1 if s[i]=='-' else 1
		i+=1
	return helper(s,i,0,sign)

print(atoi('   -8764 negatibf'))