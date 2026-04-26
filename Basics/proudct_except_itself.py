def product_except_itself(nums):
    n=len(nums)
    res=[1]*n
    left=1
    right=1
    for i in range(n):
        res[i]=left
        left*=nums[i]
    
    for i in range(n-1,-1,-1):
        res[i]*=right
        right*=nums[i]
    
    return res

nums=[1, 2, 3, 4]
print(product_except_itself(nums))
        
        
