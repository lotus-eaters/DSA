def threesum_brute(nums):
    res=[]
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==0:
                    triplet = sorted([nums[i],nums[j],nums[k]])
                    if triplet not in res:
                        res.append(triplet)
    return res

def threesum_better(nums):
    set_res=set()
    n=len(nums)
    for i in range(n):  
        seen=set()
        for j in range(i+1,n):
            complement=-(nums[i]+nums[j])
            if complement in seen:
                triplet=tuple(sorted((nums[i],nums[j],complement)))
                set_res.add(triplet)
            seen.add(nums[j])
    return list(set_res)

def threesum_optimal(nums):
    nums.sort()
    res=[]
    n=len(nums)
    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left,right=i+1,n-1
        while left<right:
            total=nums[i]+nums[left]+nums[right]
            if total==0:
                res.append([nums[i],nums[left],nums[right]])
                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-=1
                left+=1
                right-=1
            elif total<0:
                left+=1
            else:
                right-=1
    return res

nums=[-1,0,1,2,-1,-4]
print(threesum_brute(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
print(threesum_better(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
print(threesum_optimal(nums)) # Output: [[-1, -1, 2], [-1, 0, 1]]
# Time Complexity: O(N^3) for brute force, O(N^2) for better and optimal solutions.
# Space Complexity: O(N) for better solution due to the set, O(N) for optimal solution due to sorting, O(1) for brute force.