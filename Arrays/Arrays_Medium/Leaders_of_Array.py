def leaders_of_array_brute(nums):
    ans=[]
    n=len(nums)
    for i in range(n):
        leader=True
        for j in range(i+1,n):
            if nums[j]>nums[i]:
                leader=False
                break
        if leader:
            ans.append(nums[i])
    return ans

def leaders_of_array_optimal(nums):
    ans=[]
    n=len(nums)
    max=nums[n-1]
    ans.append(nums[n-1])
    for i in range(n-2,-1,-1):
        if nums[i]>max:
            ans.append(nums[i])
            max=nums[i]

    ans.reverse()
    return ans


nums = [10, 22, 12, 3, 0, 6]
print(leaders_of_array_brute(nums))
print(leaders_of_array_optimal(nums))

