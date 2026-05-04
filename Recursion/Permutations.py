def permutations(ques:str,ans:str):
	if len(ques)==0:
		print(ans)
		return
	for i in range(len(ques)):
		ch = ques[i]
		nq = ques[:i]+ques[i+1:]
		permutations(nq,ans+ch)
permutations("abc","")