from itertools import permutations
def next_permutation_brute(nums):
    perms=sorted(set(permutations(nums)))
    current=tuple(nums)
    for i in range(len(perms)):
        if current==perms[i]:
            if i == len(perms)-1:
                return list(perms[0])
            return list(perms[i+1])
# Time Complexity: O(N!*N), since we are generating all possible permutations, it takes N! time.
# Space Complexity: O(N!), storing all permutations.          

# The Algorithm (3 Steps):

# Find the "pivot" - rightmost position where number is smaller than its next
# Swap with next larger - find the smallest number to the right that's larger than pivot
# Reverse the suffix - reverse everything after the pivot position

def next_permutation_optimal(nums):
    index=0
    for i in range(len(nums)-2,-1,-1):
        if nums[i]<nums[i+1]:
            index=i
            break
    if index==-1:
        nums.reverse()
        return
    for i in range(len(nums)-1,index,-1):
        if nums[i]>nums[index]:
            nums[i],nums[index]=nums[index],nums[i]
            break
    nums[index+1:]=reversed(nums[index+1:])
    return nums

nums=[2,1,5,4,3,0,0]
print(next_permutation_brute(nums))
print(next_permutation_optimal(nums))