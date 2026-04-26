def validate_parenthesis(s:str)-> bool:
    stack=[]
    mapping = {')':'(','}':'{',']':'['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1]!=mapping[char]:
                return False
            stack.pop()
    return len(stack)==0

s = "()[]{}"
print(validate_parenthesis(s))  # Output: True
s = "([)]"
print(validate_parenthesis(s))  # Output: False
s = "{[]}"
print(validate_parenthesis(s))  # Output: True
