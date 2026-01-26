def sort_zero_one_two_brute(nums):
    counter0=counter1=counter2=0
    for num in nums:
        if num==0:
            counter0+=1
        elif num==1:
            counter1+=1
        else:
            counter2+=1
    index=0
    for _ in range(counter0):
        nums[index]=0
        index+=1
    for _ in range(counter1):
        nums[index]=1
        index+=1
    for _ in range(counter2):
        nums[index]=2
        index+=1
    return nums

def sort_zero_one_two_better(nums):
    # Count of 0s, 1s, and 2s
    cnt0 = cnt1 = cnt2 = 0

    # First pass: Count the number of 0s, 1s, and 2s
    for num in nums:
        if num == 0:
            cnt0 += 1
        elif num == 1:
            cnt1 += 1
        else:
            cnt2 += 1

    # Second pass: Fill the array with 0s, then 1s, then 2s

    # Fill first 'cnt0' elements with 0
    for i in range(cnt0):
        nums[i] = 0

    # Fill next 'cnt1' elements with 1
    for i in range(cnt0, cnt0 + cnt1):
        nums[i] = 1

    # Fill remaining elements with 2
    for i in range(cnt0 + cnt1, len(nums)):
        nums[i] = 2
    return nums

# Time Complexity: O(n) The array is traversed only once using the `mid` pointer. Each element is checked at most once, and swaps are done in constant time.

# Space Complexity: O(1) Only a few integer pointers (`low`, `mid`, `high`) are used. Sorting is done in-place, requiring no additional space.
def sort_zero_one_two_optimal(nums):
    low,mid,high=0,0,len(nums)-1
    while mid<=high:
        if nums[mid]==0:
            nums[mid],nums[low]=nums[low],nums[mid]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums
            

nums = [1, 0, 2, 1, 0]
# Time Complexity: O(n),We traverse the array twice: once to count, once to overwrite. Each operation is O(n).
# Space Complexity: O(1), We use only a constant number of counters regardless of the input size. No extra array is used.
print(sort_zero_one_two_brute(nums))
print(sort_zero_one_two_better(nums))
print(sort_zero_one_two_optimal(nums))

  
