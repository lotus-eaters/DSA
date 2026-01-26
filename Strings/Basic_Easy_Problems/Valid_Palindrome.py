def valid_palindrome_cleaned_string(s):
    s=''.join(c.lower() for c in s if c.isalnum())
    left = 0
    right = len(s)-1
    
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

def valid_palindrome_optimal(s):
    left = 0
    right = len(s)-1
    while left<right:
        while left<right and not s[left].isalnum():
            left+=1
        while left<right and not s[right].isalnum():
            right-=1
        if s[left].lower()!=s[right].lower():
            return False
        left+=1
        right-=1
    return True

s = "A man, a plan, a canal: Panama"
print(valid_palindrome_cleaned_string(s))
print(valid_palindrome_optimal(s))