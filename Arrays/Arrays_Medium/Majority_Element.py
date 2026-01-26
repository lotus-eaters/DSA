def majority_element_brute(nums):
    n=len(nums)
    for i in range(n):
        count=0
        for j in range(i,n):
            if nums[j]==nums[i]:
                count+=1
        if count>n//2:
            return nums[i]
    return -1

def majority_element_better(nums):
    n=len(nums)
    freq={}
    for num in nums:
        if num not in freq:
            freq[num]=1
        else:
            freq[num]+=1
    for k,v in freq.items():
        if v>n//2:
            return k
    return -1

def majority_element_optimal(nums):
    count=0
    element=0
    n=len(nums)
    for num in nums:
        if count==0:
            count+=1
            element=num
        if element==num:
            count+=1
        else:
            count-=1
    count1=nums.count(element)
    if count1>n//2:
        return element
    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
print(majority_element_brute(arr))
print(majority_element_better(arr))
print(majority_element_optimal(arr))
