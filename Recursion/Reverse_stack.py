def rev_stack(stack):
	if not stack:
		return 
	top_val=stack.pop()
	rev_stack(stack)
	insert(stack,top_val)

def insert(stack,val):
	if not stack:
		stack.append(val)
		return
	top_val=stack.pop()
	insert(stack,val)
	stack.append(top_val)

stack = [4,3,2,1]
rev_stack(stack)
print(stack)