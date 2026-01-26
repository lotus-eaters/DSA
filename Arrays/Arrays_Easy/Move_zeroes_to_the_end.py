def move_zeroes_to_end_brute(nums):
    n=len(nums)
    temp=[0]*n
    index=0
    for num in nums:
        if num !=0:
            temp[index]=num
            index+=1
    for i in range(n):
        nums[i]=temp[i]
    return nums

def move_zeroes_to_end_better(nums):
    n=len(nums)
    index=0
    for i in range(n):
        if nums[i]!=0:
            nums[index]=nums[i]
            index+=1
    for i in range(index,n):
        nums[i]=0
    return nums

def move_zeroes_to_end_optimal(nums):
    n=len(nums)
    index=0
    for i in range(n):
        if nums[i]!=0:
            nums[i],nums[index],=nums[index],nums[i]
            index+=1
    return nums


nums=[2,4,0,6,0,5,7]
# Time Complexity: O(N), we can move all zeroes to end in linear time.
# Space Complexity: O(N), additional space used for temporary array.
print(move_zeroes_to_end_brute(nums.copy()))
# Time Complexity: O(N), we can move all zeroes to end in linear time.
# Space Complexity: O(1), inplace memory
print(move_zeroes_to_end_better(nums.copy()))
print(move_zeroes_to_end_optimal(nums.copy()))


