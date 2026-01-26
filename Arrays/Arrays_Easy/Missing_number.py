def missing_number_brute(nums):
    n=len(nums)+1
    for i in range(1,n+1):
        found=False
        for num in nums:
            if num==i:
                found=True
                break
        if not found:
            return i
# TC=O(N^2) SC= O(1)
def missing_number_sorting(nums):
    nums.sort()
    for i in range(len(nums)+2):
        if nums[i]!=i+1:
            return i+1
# TC=O(NlogN) SC= O(1)

def missing_number_boolean(nums):
    n=len(nums)+1
    boolarr=[False]*(n+1)
    for i in range(1,n+1):
        if i in nums:
            boolarr[i]=True
    for i in range(1,n+1):
        if boolarr[i]==False:
            return i
# TC=O(NlogN) SC= O(N) 

def missing_number_set(nums):
    seen=set(nums)
    n=len(nums)+1
    for i in range(1,n+1):
        if i not in seen:
            return i
# TC=O(NlogN) SC= O(N)     
 
def missing_number_sumofnaturalnumbers(nums):
    n=len(nums)+1
    expected =  n*(n+1)//2
    actual = sum(nums)
    return expected-actual
# TC=O(N) SC= O(1) 

def missing_number_xor(nums):
    xor_all=0
    n=len(nums)+1
    for i in range(1,n+1):
        xor_all^=i
    for num in nums:
        xor_all^=num
    return xor_all
# TC=O(N) SC= O(1) 

nums=[1,2,4,5]
print(missing_number_brute(nums))
print(missing_number_sorting(nums))
print(missing_number_sumofnaturalnumbers(nums))
print(missing_number_set(nums))
print(missing_number_boolean(nums))
print(missing_number_xor(nums))
