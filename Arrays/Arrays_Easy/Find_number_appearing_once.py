def find_number_appearing_once_brute(nums):
    n=len(nums)
    for i in range(n):
        num=nums[i]
        count=0
        for j in range(n):
            if nums[j]==num:
                count+=1
        if count==1:
            return num
    return -1

def find_number_appearing_once_better(nums):
    max_ele=max(nums)
    hash_array=[0]*(max_ele+1)
    for num in nums:
        if num in hash_array:
            hash_array[num]+=1
        else:
            hash_array[num]=1
    for num in nums:
        if hash_array[num]==1:
            return num
    return -1

def find_number_appearing_once_optimal(nums):
    xor_all=0
    for x in nums:
        xor_all^=x
    return xor_all

arr= [4,1,2,1,2]

print(find_number_appearing_once_brute(arr))
print(find_number_appearing_once_better(arr))
print(find_number_appearing_once_optimal(arr))

