def isPalindrome(s):
	s=''.join(c.lower() for c in s if c.isalnum())
	left=0
	right=len(s)-1
	while left<right:
		if s[left]!=s[right]:
			return False
		left+=1
		right-=1
	return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))