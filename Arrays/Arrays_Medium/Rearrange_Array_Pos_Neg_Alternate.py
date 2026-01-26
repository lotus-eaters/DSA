def rearrange_pos_neg_brute(nums):
    n=len(nums)
    pos=[]*n//2
    neg=[]*n//2
    for i in range(n):
        if nums[i]<0:
            pos[i]=nums[i]
        else:
            neg[i]-nums[i]
    for i in range(n//2):
        nums[2*i]=pos[i]
        nums[2*i+1]=neg[i]
    return nums
# Time Complexity: O(N+N/2) { O(N) for traversing the array once for segregating positives and negatives and another O(N/2) for adding those elements alternatively to the array, where N = size of the array A}.
# Space Complexity: O(N/2 + N/2) = O(N) { N/2 space required for each of the positive and negative element arrays, where N = size of the array A}.

def rearrange_pos_neg_optimal(nums):
    n=len(nums)
    ans=[]*0
    pos=0
    neg=1
    for i in range(n):
        if nums[i]>0:
            ans[pos]=nums[i]
            pos+=2
        else:
            ans[neg]=nums[i]
            neg+=2

# Time Complexity: O(N) { O(N) for traversing the array once and substituting positives and negatives simultaneously using pointers, where N = size of the array A}.

# Space Complexity: O(N) { Extra Space used to store the rearranged elements separately in an array, where N = size of array A}.

