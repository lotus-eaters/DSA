def max_consecutive_ones(nums):
    maxi=0
    count=0
    for num in nums:
        if num==1:
            count+=1
        else:
            count=0
    return max(maxi,count)
nums=[1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1]
print(max_consecutive_ones(nums))