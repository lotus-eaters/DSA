def longestSubarraySumUltraBrute(nums,d):
    n=len(nums)
    length=0
    res=0
    for i in range(n):
        for j in range(i,n):
            res=0
            for k in range(i,j+1):
                res+=nums[k]
            if res==d:
                length =max(length,j-i+1)
    return length
#O(N^3)

def longestSubarraySumBrute(nums,d):
    n=len(nums)
    max_len=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=nums[j]
            if sum==d:
                max_sum=max(max_len,j-i+1)
    return max_sum
#O(N^2)

def longestSubArraySumHashMap(nums,d):
    max_len=0
    n=len(nums)
    prefix_sum=0
    map_prefix={}
    # traverse through the array
    for i in range(n):
        # add the elements to prefix_sum
        prefix_sum+=nums[i]
        #if prefix sum is equal to key then update the maxlen and return
        if prefix_sum==d:
            max_len=i+1
        #if prefix_sum-key is found in hashmap then get the index, calculate subarray [i-index],update the max_len
        if prefix_sum-d in map_prefix:
            max_len=max(max_len,i-map_prefix[prefix_sum-d])
        #if prefix_sum not in hashmap, add it and store its index as value
        if prefix_sum not in map_prefix:
            map_prefix[prefix_sum]=i
    return max_len

# Metric	Value
# Time Complexity	O(N)
# Space Complexity	O(N)
        
def longestSubArraySumTwoPointers(nums,d): #this works only for positive numbers O(N) O(1)
    n=len(nums)
    maxlen=0
    sum=nums[0]
    left,right=0,0
    while right<n:
        while left<=right and sum>k:
            sum-=nums[left]
            left+=1
        if sum==k:
            maxlen=max(maxlen,right-left+1)
        right+=1
        if right<n:
            sum+=nums[right]
    return maxlen


nums = [10, 5, 2, 7, 1, 9]
k = 15          
print(longestSubarraySumUltraBrute(nums,k))
print(longestSubarraySumBrute(nums,k))
print(longestSubArraySumTwoPointers(nums,k))
print(longestSubArraySumHashMap(nums,k))

