def two_sum_brute(nums,target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
    return -1

def two_sum_better(nums,target):
    n=len(nums)
    twosum={} #dict to store the num,index key,value
    for i,num in enumerate(nums):
        complement=target-num
        if complement in twosum:
            return [twosum[complement],i]
        twosum[num]=i
    return -1

def two_sum_optimal(nums,target):
    nums_with_indexes=sorted(enumerate(nums), key=lambda x:x[1])
    left,right=0,len(nums)-1
    while left<right:
        current_sum=nums_with_indexes[left][1]+nums_with_indexes[right][1]
        if current_sum==target:
            return [nums_with_indexes[left][0],nums_with_indexes[right][0]]
        elif current_sum<target:
            left+=1
        else:
            right-=1
arr = [2, 6, 5, 8, 11]
target = 14
print(two_sum_brute(arr,target))
print(two_sum_better(arr,target))
print(two_sum_optimal(arr,target))