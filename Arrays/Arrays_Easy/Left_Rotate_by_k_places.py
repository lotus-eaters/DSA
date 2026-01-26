def left_rotate_array_by_k_brute(nums,k):
    n= len(nums)
    k%=n
    if n==0:
        return
    # store k elements in temp arr
    temp=nums[:k]
    # move remaining n to k elements of nums by k positions
    for i in range(k,n):
        nums[i-k]=nums[i]
    # first k stored in temp elements will have to be placed at the end of org array
    for i in range(k):
        nums[n-k+i]=temp[i]
    return nums

def left_rotate_array_by_k_optimal(nums,k):
    n= len(nums)
    k%=n
    if n==0:
        return
    #first k elements to be reversed
    nums[:k]=reversed(nums[:k])
    #last k elements to be reversed
    nums[k:]=reversed(nums[k:])
    #whole array to be reversed
    nums.reverse()
    return nums
    

nums = [3, 5, 7, 9, 2, 4]
k = 2


#Time Complexity: O(n), We are performing a constant number of linear operations copying `k` elements and shifting up to `n-k` elements.
#Space Complexity: O(k) ,A temporary array of size `k` is used to store either the first `k` or last `k` elements depending on the direction of rotation.
print(left_rotate_array_by_k_brute(nums.copy(),k)) 
print(left_rotate_array_by_k_optimal(nums.copy(),k)) 


    
