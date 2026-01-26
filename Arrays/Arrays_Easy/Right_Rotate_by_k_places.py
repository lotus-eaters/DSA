def right_rotate_k_places_brute(nums,k):
    n=len(nums) 
    if n==0: 
        return
    k%=n
    #store last k elements in temp
    temp=nums[-k:]
    #iterate from reverse direction starting from n-k-1 element and push it k positions to right
    for i in range(n-k-1,-1,-1):
        nums[i+k]=nums[i]
    #copy elements from temp to org array
    for i in range(k):
        nums[i]=temp[i]
    return nums

def right_rotate_k_places_optimal(nums, k):
    n = len(nums)
    k %= n
    #reverse the entire array first
    nums.reverse()
    #reverse first k elements
    nums[:k] = reversed(nums[:k])
    #reverse last k elements
    nums[k:] = reversed(nums[k:])
    return nums

def reverse_array(a,start,end):
    while start<end:
        a[start], a[end]=a[end],a[start]
        start+=1
        end-=1
    return a


def right_rotate_k_places_helper_function(nums,k):
    n = len(nums)
    k %= n
    reverse_array(nums,0,n-1)
    reverse_array(nums,0,k-1)
    reverse_array(nums,k,n-1)
    return nums

nums = [3, 5, 7, 9, 2, 4]
k = 2


#Time Complexity: O(n), We are performing a constant number of linear operations copying `k` elements and shifting up to `n-k` elements.
#Space Complexity: O(k) ,A temporary array of size `k` is used to store either the first `k` or last `k` elements depending on the direction of rotation.
print(right_rotate_k_places_brute(nums.copy(),k)) 
print(right_rotate_k_places_optimal(nums.copy(),k)) 
print(right_rotate_k_places_helper_function(nums.copy(),k)) 

#Time Complexity: O(N), We reverse parts of the array each reverse takes linear time. So total work is 3 × O(N) = O(N).
#Space Complexity: O(1) All modifications are done in-place, using only a few temporary variables.