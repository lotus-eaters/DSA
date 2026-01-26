# Time Complexity: O(N), We traverse the entire array and insert elements into set.
# Space Complexity: O(N), additional space used to store elements in set.

def removeduplicatesBrute(nums):
    seen=set()
    index=0
    for num in nums:
        if num not in seen:
            seen.add(num)
            nums[index]=num
            index+=1
    return index

def removeduplicatesOptimal(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


a1 = [1,2,3,3,4,4,4,5,5]
a2 = [1,2,3,3,4,4,4,5,5]

print(removeduplicatesBrute(a1))     # works on any array
print(removeduplicatesOptimal(a2))   # works only on sorted array
