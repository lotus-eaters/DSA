def permute(arr):
	ans=[]

	def helper(used):
		if len(arr)==len(used):
			ans.append(used.copy())
			return
		for i in range(len(arr)):
			if arr[i] not in used:
				used.append(arr[i])
				helper(used)
				used.pop()
	helper([])
	return ans
print(permute([1,2,3]))