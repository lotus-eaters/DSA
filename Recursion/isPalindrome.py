def isPalindromeIterative(s):
	s=''.join(c.lower() for c in s if c.isalnum())
	left=0
	right=len(s)-1
	while left<right:
		if s[left]!=s[right]:
			return False
		left+=1
		right-=1
	return True

def isPalindromeRecursive(s,l,r):
	if l>=r:
		return True

	if s[l]==s[r] and isPalindromeRecursive(s,l+1,r-1):
		return True

s = "A man, a plan, a canal: Panama"

print(isPalindromeIterative(s))
a='abcba'
print(isPalindromeRecursive(a,0,len(a)-1))