def majority(nums):
    count=0
    element=0
    n=len(nums)-1
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
arr = [2, 2, 1, 1, 1, 2, 2]
print(majority(arr))