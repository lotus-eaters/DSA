def foursum_brute(nums,target):
    res=[]
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if nums[i]+nums[j]+nums[k]+nums[l]==target:
                        quad = sorted([nums[i],nums[j],nums[k],nums[l]])
                        if quad not in res:
                            res.append(quad)
    return res

def four_sum_better(nums,target):
    set_res=set()
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            seen=set()
            for k in range(j+1,n):
                complement = target - nums[i] -nums[j] -nums[k]
                if complement in seen:
                    quads = sorted([nums[i],nums[j],nums[k],complement])
                    set_res.add(tuple(quads))
                seen.add(nums[k])
    return list(set_res)

def four_sum_optimal(nums,target):
    nums.sort()
    res=[]
    n=len(nums)
    for i in range(n):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n):
            if j+1>0 and nums[j]==nums[j-1]:
                continue
            left=j+1
            right=n-1
            while left<right:
                total = nums[i]+nums[j]+nums[left]+nums[right]
                if total==target:
                    res.append([nums[i],nums[j],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                elif total<target:
                    left+=1
                else:
                    right-=1
    return res

nums=[1,0,-1,0,-2,2]
target=0
print(foursum_brute(nums,target))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(four_sum_better(nums,target))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(four_sum_optimal(nums,target)) # Output: [[-2, -1,
                    