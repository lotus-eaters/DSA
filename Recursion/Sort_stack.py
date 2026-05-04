def sortstack(stack):
	if not stack:
		return 
	val = stack.pop()
	sortstack(stack)
	insert(stack,val)
def insert(stack,temp):
	if not stack or stack[-1]<=temp:
		stack.append(temp)
		return
	val=stack.pop()
	insert(stack,temp)
	stack.append(val)
stack=[5,4,7,3,8]
sortstack(stack)
print(stack)

